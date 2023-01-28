from logger_lib import logger
import re
import random


class NpcSingleton(object):
    def __new__(cls):
        """ creates a singleton object, if it is not created, or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(NpcSingleton, cls).__new__(cls)
        return cls.instance
    def __init__(self):
        self.sex = None               # [str] 'Male' or 'Female'
        self.species = None           # [str] "Human", "Dwarf", "Halfling", "High Elf", "Wood Elf", "Gnome"
        self.age_str = None           # [str] 'Young', 'Middle', 'Old'
        self.age = None               # [int] in years
        self.height = None            # [float] in meters
        self.name = None              # [str] Name and Surname
        self.desc_gen_look = None     # [str]
        self.desc_traits = None       # [list of str]
        self.desc_reactions = None    # [list of str]
        self.desc_appearance = None   # [list of str]
        self.ch_class = None          # [str]
        self.career_main_name = None  # [str]
        self.career_main = None       # [class from careers_nps.py]
        self.career_level = None      # [int]
        self.career_current = None    # [CareerClass]
        self.status = None            # [str]
        self.trapping = None          # [str]
        self.money = None             # [str]
        self.dooming = None           # [str]
        self.xp_start = None          # [int]
        self.xp_left = None           # [int]
        self.attributes = {           # {stat_name: [base, advance, total]} e.g.: "WS": [0, 0, 0]
            "WS": None, "BS": None, "S": None, "T": None, "AG": None, "I": None, "DEX": None, "INT": None, "WP": None, "FEL": None,
            "Wounds": None, "MoveSpeed": None, "Fate": None, "Fortune": None, "Resilience": None, "Resolve": None}
        self.skills_basic = {}        # {skill_name: [stat_str, stat_total, skill_advances, skill_total]}
        self.skills_advanced = {}     # {skill_name: [stat_str, stat_total, skill_advances, skill_total]}
        self.talents = {}             # {talent_name: (test, advance, description)}

    def get_init_values(self, **kwargs):
        from constants import age_by_species, careers_all, skills_all_basic
        """
        set: sex, species, age, class, main career, current carrer, status, xp, basic skills
        """
        self.sex = kwargs.get('sex')
        self.species = kwargs.get('species')
        # roll age in boundaries
        self.age_str = kwargs.get('age')
        age_range = age_by_species[self.species]
        if self.age_str == 'Young':
            low =  age_range[0]
            high = age_range[0]+abs(age_range[1]-age_range[0])//4
            self.age = random.randint(low, high)
        elif self.age_str == 'Middle':
            low =  age_range[1]-abs(age_range[2]-age_range[1])//4
            high = age_range[1]+abs(age_range[2]-age_range[1])//4
            self.age = random.randint(low, high)
        else:   # 'Old':
            low =  age_range[2]-abs(age_range[2]-age_range[1])//5
            high = age_range[2]+abs(age_range[2]-age_range[1])//5
            self.age = random.randint(low, high)

        self.ch_class = kwargs.get('class')
        self.career_main_name = kwargs.get('career')
        self.career_main = careers_all[self.career_main_name]()
        self.career_level = 0
        self.career_current = self.career_main.lvl[self.career_level]
        self.status = self.career_current.status
        self.xp_start = kwargs.get('xp')
        self.xp_left = self.xp_start
        for skill_name in skills_all_basic.keys():
            [stat_str, _, _] = skills_all_basic[skill_name]  # ["FEL", "basic", []]
            self.skills_basic.update({skill_name: [stat_str, 0, 0, 0]})

    def roll_npc(self):
        #0  roll descriptions
        self.roll_height()
        self.roll_name()
        self.roll_description()
        #1  roll attributes
        self.roll_attributes()
        #2  advance stats
        self.advance_stats()
        #3  roll skills and talents by species
        self.roll_skills_species()
        self.roll_talents_species()
        #4  set skills and talents by career
        self.set_skills_career()
        self.set_talents_career()
        #5  roll_other_things
        self.roll_other_things()
        # update
        self.update_all()
    def check_npc_1(self):
        """
        Check if npc has everything what it supposes to have after self.roll_npc()
        """
        pre_desc = f'NpcSingleton.check_npc_1: '

        # INIT
        if self.height is None:
            error = f'{pre_desc}Height not set'
            logger.error(error)
            raise Exception(error)
        if self.name is None:
            error = f'{pre_desc}Name not set'
            logger.error(error)
            raise Exception(error)
        if None in [self.desc_gen_look, self.desc_traits, self.desc_reactions, self.desc_appearance]:
            error = f'{pre_desc}Description not set'
            logger.error(error)
            raise Exception(error)
        if self.trapping is None:
            error = f'{pre_desc}Trapping not set'
            logger.error(error)
            raise Exception(error)
        if self.money is None:
            error = f'{pre_desc}Money not set'
            logger.error(error)
            raise Exception(error)
        if 'Doomed' in self.talents.keys() and self.dooming is None:
            error = f'{pre_desc}Dooming not set'
            logger.error(error)
            raise Exception(error)

        # ATTRIBUTES
        for stat_name, val in self.attributes.items():
            if val is None:
                error = f'{pre_desc}Attribute ({stat_name}) - value not set'
                logger.error(error)
                raise Exception(error)
        #   exactly 5 advances points (self.advance_stats)
        if sum([advance for [base, advance, total] in self.attributes.values() if advance > 0]) != 5:
            error = f'{pre_desc}Attributes - sum of advance points !=5'
            logger.error(error)
            raise Exception(error)

        # SKILLS
        sum_advances = 0
        for skill_name, [stat_str, stat_total, skill_advances, skill_total] in self.skills_basic.items():
            if skill_total == 0:
                error = f'{pre_desc}Skill ({skill_name}) - value not set'
                logger.error(error)
                raise Exception(error)
            sum_advances += skill_advances
        for skill_name, [stat_str, stat_total, skill_advances, skill_total] in self.skills_advanced.items():
            if skill_total == 0:
                error = f'{pre_desc}Skill ({skill_name}) - value not set'
                logger.error(error)
                raise Exception(error)
            sum_advances += skill_advances
        #   exactly 64 advances points (self.roll_skills_species, self.set_skills_career)
        if sum_advances != 64:
            error = f'{pre_desc}Skills - sum of advance points !=64'
            logger.error(error)
            raise Exception(error)

        # TALENTS
        #   advance value can be == 0 at this point (even intended!)
        sum_advances = sum([1 for (test, advance, description) in self.talents.values() if advance > 0])
        #   for Halfling, Gnome: exactly 7 talents with advance points == 1 (self.roll_talents_species, set_talents_career)
        if self.species in ["Halfling", "Gnome"]:
            if sum_advances != 7:
                error = f'{pre_desc}Talents - number of advanced talents !=7'
                logger.error(error)
                raise Exception(error)
        #   for rest species: exactly 6 talents with advance points == 1 (self.roll_talents_species, set_talents_career)
        else:
            if sum_advances != 6:
                error = f'{pre_desc}Talents - number of advanced talents !=6'
                logger.error(error)
                raise Exception(error)

    def roll_height(self):
        from functions import random_pick, rollXd10
        from constants import age_by_species, height_by_species
        # consider age
        init_height = 0
        if self.age_str == 'Young':
            init_height = height_by_species[self.species][0]
        elif self.age_str == 'Middle':
            init_height = height_by_species[self.species][1]
        else:   # 'Old
            init_height = height_by_species[self.species][2]
        # roll height
        if self.species == "Human":
            self.height = init_height + rollXd10(4)/100
        elif self.species == "Dwarf":
            self.height = init_height + rollXd10(2)/100
        elif self.species == "Halfling":
            self.height = init_height + rollXd10(2)/100
        elif self.species == "High Elf":
            self.height = init_height + rollXd10(3)/100
        elif self.species == "Wood Elf":
            self.height = init_height + rollXd10(3)/100
        elif self.species == "Gnome":
            self.height = init_height + rollXd10(2)/100
    def roll_name(self):
        from functions import random_pick, roll1d100
        from constants import names_by_sex, surnames_by_species, surname_Suffix_Male_Dwarf, surname_Suffix_Female_Dwarf

        out_name = random_pick(names_by_sex[self.sex][self.species])
        out_surname = random_pick(surnames_by_species[self.species])

        # Dwarves could get Icelandic style surnames: 66% Male 33% Female
        if self.species == 'Dwarf':
            roll_val = roll1d100()
            if self.sex == 'Male' and roll_val <= 66:
                out_surname += random_pick(surname_Suffix_Male_Dwarf)
            if self.sex == 'Female' and roll_val <= 33:
                out_surname += random_pick(surname_Suffix_Female_Dwarf)

        # Noble - handles later

        self.name = out_name + ' ' + out_surname
    def roll_description(self):
        from functions import get_traits, get_appearance
        (self.desc_gen_look, self.desc_traits, self.desc_reactions), self.desc_appearance = get_traits(self), get_appearance(self)
    def roll_attributes(self):
        from functions import roll2d10
        from constants import attributes_by_species
        pre_desc = f'NpcSingleton.roll_attributes: '
        # roll base stats by species e.g. 2d10+20
        for stat_name in ["WS", "BS", "S", "T", "AG", "I", "DEX", "INT", "WP", "FEL"]:
            species_val = attributes_by_species[self.species][stat_name]
            self.attributes.update({stat_name: [roll2d10()+species_val, 0, 0]})     # {stat_name: [base, advance, total]}
        # roll wounds
        bonusS = self.attributes['S'][0] // 10      # base
        bonusT = self.attributes['T'][0] // 10      # base
        bonusWP = self.attributes['WP'][0] // 10    # base
        if self.species == "Human":
            wounds_val = bonusS + 2 * bonusT + bonusWP
        elif self.species == "Dwarf":
            wounds_val = bonusS + 2 * bonusT + bonusWP
        elif self.species == "Halfling":
            wounds_val = 2 * bonusT + bonusWP
        elif self.species == "High Elf":
            wounds_val = bonusS + 2 * bonusT + bonusWP
        elif self.species == "Wood Elf":
            wounds_val = bonusS + 2 * bonusT + bonusWP
        elif self.species == "Gnome":
            wounds_val = 2 * bonusT + bonusWP
        else:
            error = f'{pre_desc}Unknown species: {self.species}'
            logger.error(error)
            raise Exception(error)

        self.attributes.update({'Wounds': [wounds_val, 0, 0]})
        # roll move speed
        self.attributes.update({'MoveSpeed': [attributes_by_species[self.species]['MoveSpeed'], 0, 0]})
        # roll fate
        extra_val = attributes_by_species[self.species]['Extra']
        roll_val = random.randint(0, extra_val)
        self.attributes.update({'Fate': [attributes_by_species[self.species]['Fate'] + roll_val, 0, 0]})
        # roll fortune == fate
        self.attributes.update({'Fortune': [self.attributes['Fate'][0], 0, 0]})
        # roll resilience
        rest_val = extra_val - roll_val
        self.attributes.update({'Resilience': [attributes_by_species[self.species]['Resilience'] + rest_val, 0, 0]})
        # roll resolve == resilience
        self.attributes.update({'Resolve': [self.attributes['Resilience'][0], 0, 0]})
        # update
        self.update_attributes()
    def advance_stats(self):
        # add 5 advances points by career
        choice_list = [[5, 0, 0], [4, 1, 0], [3, 1, 1], [3, 2, 0], [2, 2, 1]]
        roll_list = choice_list[random.randint(0, 4)]
        #   self.career_current.advances == list of str, e.g. ['T', 'DEX', 'INT']
        for stat_name, value in zip(self.career_current.advances, roll_list):
            [base, advance, total] = self.attributes[stat_name]
            advance += value
            self.attributes.update({stat_name: [base, advance, total]})
        # update
        self.update_attributes()
    def roll_skills_species(self):
        """
        :return: out_skills: {skill_name: advance}
        """
        from constants import skills_by_species

        # roll 6 skills
        in_skills = skills_by_species[self.species]
        skills = []     # [(skill_name: advance_value) ]
        indexes = []
        while len(indexes) < 6:
            idx = random.randint(0, len(in_skills) - 1)
            if idx not in indexes:
                indexes.append(idx)
                skills.append((in_skills[idx], 0))

        # advance skills values
        for i in range(len(skills)):
            skill_name, advance = skills[i]
            if i < 3:
                skills[i] = (skill_name, 5)     # advance 3 skills by value: 5
            else:
                skills[i] = (skill_name, 3)     # advance 3 skills by value: 3

        # parse
        out_skills = self.parse_skill_words(skills)     # {skill_name: advance}
        # add
        self.add_skills(out_skills)
        # update
        self.update_skills()
    def roll_talents_species(self):
        from constants import talents_by_species

        # roll 5 talents
        in_talents = talents_by_species[self.species]
        talents = [(talent_name, 1) for talent_name in in_talents]  # [(talent_name, advance), ...]
        # parse
        out_talents = self.parse_talent_words(talents)  # {talent_name: advance}
        # add
        self.add_talents(out_talents)
        # modify
        self.modify_stats_by_talents(out_talents)
    def set_skills_career(self):
        from functions import random_pick
        # add 8 skills from career
        skills = [(skill_name, 0) for skill_name in self.career_current.skills]  # [(skill_name: value), ...]
        # pick one of advance option (in sum 40 points)
        example = [
            [5, 5, 5, 5, 5, 5, 5, 5],
            [7, 6, 5, 5, 5, 5, 4, 3],
            [6, 6, 6, 5, 5, 4, 4, 4],
            [8, 7, 6, 5, 5, 4, 3, 2],
            [8, 8, 7, 7, 4, 2, 2, 2],
            [9, 8, 5, 5, 5, 5, 2, 1],
            [10, 8, 7, 5, 5, 3, 2, 0],
            [10, 9, 8, 7, 3, 2, 1, 0],
            [10, 10, 10, 6, 1, 1, 1, 1],
            [10, 10, 10, 10, 0, 0, 0, 0]]
        out_values = example[random_pick(list(range(len(example))))]
        # advance skills values
        for i in range(len(skills)):
            skill_name, advance = skills[i]
            skills[i] = (skill_name, out_values[i])
        # parse
        out_skills = self.parse_skill_words(skills)     # {skill_name: advance}
        # add
        self.add_skills(out_skills)
        # update
        self.update_skills()
    def set_talents_career(self):
        from functions import random_pick

        # get unique talent names
        talent_names = list(set(self.career_current.talents) - set(self.talents.keys()))
        talents = [(name, 0) for name in talent_names]  # [(talent_name, advance), ...]
        # parse
        out_talents = self.parse_talent_words(talents)    # {talent_name: advance_value}
        # advance (by 1) only one, randomly picked talent
        # the rest of talents will have 0 advances
        out_talents.update({random_pick(list(out_talents.keys())): 1})
        # add
        self.add_talents(out_talents)
        # modify
        self.modify_stats_by_talents(out_talents)
    def roll_other_things(self):
        from functions import random_pick
        from constants import surname_Suffix_Human, doomings_all, trappings_by_class

        # name - human Noble or Noble Blood?
        if (self.species == "Human") and ((self.career_main.lvl[1].name == "Noble") or ("Noble Blood" in self.talents.keys())):
            name, surname = self.name.split(' ')
            suffix = random_pick(surname_Suffix_Human)
            self.name = name + " von " + surname + suffix
        # skill - Dooming?
        if 'Doomed' in self.talents.keys():
            self.dooming = random_pick(doomings_all)
        else:
            self.dooming = '-'
        # trappings
        self.trapping = self.roll_trappings(trappings_by_class[self.ch_class] + ", " + self.career_current.trappings)
        # money
        self.money = self.roll_money(self.career_current.status)
    @staticmethod
    def roll_trappings(in_string):
        from functions import rollXd10
        indexes = [i.start() for i in re.finditer("[0-9]d10", in_string)]
        for index in indexes:
            number = int(in_string[index:index + 1])  # Xd10
            rolled_val = rollXd10(number)
            in_string = in_string.replace(in_string[index:index + 4], str(rolled_val))
        return in_string
    @staticmethod
    def roll_money(in_status):  # e.g. in_status="Brass 3"
        from functions import rollXd10
        social = in_status.split(" ")
        if social[0] == "Gold":
            money = social[1] + " Gold Coins"
        elif social[0] == "Silver":
            money = str(rollXd10(int(social[1]))) + " Silver Coins"
        elif social[0] == "Brass":
            money = str(rollXd10(int(social[1]) * 2)) + " Brass Coins"
        else:
            money = "0 coins."
        return money
    def update_all(self):
        self.update_attributes()
        self.update_skills()

    def advance_by_xp(self, xp_0=None):
        """
        Advance from career lvl 0 to lvl 3
        """
        from constants import talents_all
        def advance_talents(xp_val):
            """
            Advance (to max) all talents from current career
            :return: xp: int
            :return: boolean: Was there enough xp to fully advance in this domain?
            :return: reason
            """
            pre_desc = f'NpcSingleton.advance_by_xp.advance_talents: '
            cnt = 0
            reason = ''

            # get talents for current career
            talents = []            # [(talent_name, advance), ... ]
            missing_talents = []    # [(talent_name, advance), ... ]
            mapping = {}            # {talent_name_career: talent_name_npc}
            for talent_name, (talent_test, talent_advance, talent_description) in self.talents.items():
                if talent_name in self.career_current.talents:
                    talents.append((talent_name, talent_advance))
                    mapping.update({talent_name: talent_name})
                else:
                    short_name = talent_name.split(' (')[0]
                    for career_talent_name in self.career_current.talents:
                        if short_name == career_talent_name.split(' (')[0]:
                            talents.append((talent_name, talent_advance))
                            mapping.update({career_talent_name: talent_name})
            #   not all talents were found -> get missing ones, parse, add with advance=0, modify stats
            if len(mapping) < len(self.career_current.talents):
                for talent_name in self.career_current.talents:
                    if talent_name not in mapping.keys():
                        missing_talents.append((talent_name, 0))
            #   add new talents
            talents = talents + missing_talents
            out_talents = self.parse_talent_words(talents)  # {talent_name: advance}
            for talent_name, advance in out_talents.items():
                if talent_name not in self.talents.keys():
                    self.add_talents({talent_name: advance})

            # try to advance each talent to maximal value (defined in constants.all_talents)
            for talent_name, talent_advance in out_talents.items():
                short_name = talent_name.split(' (')[0]
                limit, _, _, _ = talents_all[short_name]
                if limit.isdecimal():
                    max_advance = int(limit)
                elif limit.find('Bonus') >= 0:
                    stat_name = limit[6:]
                    _, _, total = self.attributes[stat_name]     # base, advance, total
                    stat_bonus_val = total // 10
                    max_advance = stat_bonus_val
                else:
                    error = f'{pre_desc}Unknown talent max value: {limit}'
                    logger.error(error)
                    raise Exception(error)
                # advance
                for val in range(talent_advance+1, max_advance+1):
                    cost = 100 + (val-1)*100
                    if xp_val >= cost:
                        xp_val -= cost
                        talent_test, _, talent_description = self.talents[talent_name]   # (test, advance, description)
                        self.talents.update({talent_name: (talent_test, val, talent_description)})
                    else:
                        reason = f'To upgrade talent:{talent_name} to lvl: {val}/{max_advance} cost>xp: {cost}>{xp_val}'
                        break

                if len(reason) > 0:
                    break

                if self.talents[talent_name][1] >= max_advance:
                    cnt += 1
                else:
                    reason = f'Talent:{talent_name} advance<adv_sum: {self.talents[talent_name][1]}<{max_advance}'
                    break

            # modify
            self.modify_stats_by_talents(out_talents)

            # return advance not completed
            if len(reason) > 0:
                return xp_val, False, reason
            if cnt != len(out_talents):
                reason = f'Number of fully advanced talents: {cnt} != {len(out_talents)}'
                return xp_val, False, reason
            # return advance fully completed
            return xp_val, True, reason
        def advance_stats(xp_val):
            """
            ALL stats for current and previous careers -> advance to 'adv_sum' value
            :return: xp: int
            :return: boolean: Was there enough xp to fully advance in this domain?
            :return: reason
            """
            def get_cost(stat_val):
                if 0 <= stat_val <= 5:
                    return 25
                elif 6 <= stat_val <= 10:
                    return 30
                elif 11 <= stat_val <= 15:
                    return 40
                elif 16 <= stat_val <= 20:
                    return 50
                elif 21 <= stat_val <= 25:
                    return 70
                elif 26 <= stat_val <= 30:
                    return 90
                elif 31 <= stat_val <= 35:
                    return 120
                elif 36 <= stat_val <= 40:
                    return 150
                elif 41 <= stat_val <= 45:
                    return 190
                elif 46 <= stat_val <= 50:
                    return 320
                else:
                    return (stat_val-50)//5 * 30 + 350  # own formula
            cnt = 0
            reason = ''

            adv_sum = (self.career_level + 1) * 5
            # get all stat names
            stat_names = []
            for i in range(0, self.career_level+1):
                stat_names = stat_names + self.career_main.lvl[i].advances   # e.g. ['T', 'DEX', 'INT']
            # increase advance values
            for stat_name in stat_names:
                [base, advance, total] = self.attributes[stat_name]
                if advance < adv_sum:
                    for j in range(adv_sum - advance):
                        current_advance = self.attributes[stat_name][1]
                        cost = get_cost(current_advance)
                        if xp_val >= cost:
                            current_advance += 1
                            current_total = base + current_advance
                            # update!
                            self.attributes.update({stat_name: [base, current_advance, current_total]})
                            xp_val -= cost
                        else:
                            reason = f'To upgrade attribute:{stat_name} to lvl: {current_advance}/{adv_sum} cost>xp: {cost}>{xp_val}'
                            break

                    if len(reason) > 0:
                        break

                if self.attributes[stat_name][1] >= adv_sum:
                    cnt += 1
                else:
                    reason = f'Attribute:{stat_name} advance<adv_sum: {self.attributes[stat_name][1]}<{adv_sum}'
                    break

            # return advance not completed
            if len(reason) > 0:
                return xp_val, False, reason
            if cnt != len(stat_names):
                reason = f'Number of fully advanced attributes: {cnt} != {len(stat_names)}'
                return xp_val, False, reason
            # return advance fully completed
            return xp_val, True, reason
        def advance_skills(xp_val):
            """
            8 skills from current and previous careers -> advance to 'adv_sum' value
            :return: xp: int
            :return: boolean: Was there enough xp to fully advance in this domain?
            :return: reason
            """
            def get_cost(skill_val):
                if 0 <= skill_val <= 5:
                    return 10
                elif 6 <= skill_val <= 10:
                    return 15
                elif 11 <= skill_val <= 15:
                    return 20
                elif 16 <= skill_val <= 20:
                    return 30
                elif 21 <= skill_val <= 25:
                    return 40
                elif 26 <= skill_val <= 30:
                    return 60
                elif 31 <= skill_val <= 35:
                    return 80
                elif 36 <= skill_val <= 40:
                    return 110
                elif 41 <= skill_val <= 45:
                    return 140
                elif 46 <= skill_val <= 50:
                    return 180
                else:
                    return (skill_val-50)//5 * 30 + 210  # own formula
            pre_desc = 'NpcSingleton.advance_by_xp.advance.skills: '
            cnt = 0
            reason = ''

            adv_sum = (self.career_level + 1) * 5
            # get all skill names
            skill_names = []
            for i in range(self.career_level, -1, -1):
                skill_names = skill_names + self.career_main.lvl[i].skills   # e.g. ['Lore (Any)', 'Track']
            #   pick 8 randomly, without repetitions
            skill_names = random.sample(skill_names, 8)

            # get current advance values of skills
            skills = []  # [(skill_name, advance), ...]
            for skill_name in skill_names:
                name_short = skill_name.split(' (')[0]

                # in skill_basic?
                if name_short in self.skills_basic.keys():
                    [_, _, skill_advances, _] = self.skills_basic[name_short]  # [stat_str, stat_total, skill_advances, skill_total]
                    skills.append((skill_name, skill_advances))

                # in skill_advanced?
                else:
                    # try skill's full name
                    if skill_name in self.skills_advanced.keys():
                        [_, _, skill_advances, _] = self.skills_advanced[skill_name]  # [stat_str, stat_total, skill_advances, skill_total]
                        skills.append((skill_name, skill_advances))
                    else:
                        # skill name has '(Any one)' and there is according name in skill_advanced?
                        if skill_name.find('(Any one)') >= 0 and name_short in [name.split(' (')[0] for name in self.skills_advanced.keys()]:
                            # {skill_name: [stat_str, stat_total, skill_advances, skill_total]}
                            tmp = [(name, val) for name, [_, _, val, _] in self.skills_advanced.items() if name.find(name_short) >= 0]
                            tmp.sort()
                            final_name = tmp[-1][0]  # pick skill with the highest advance value
                            [_, _, skill_advances, _] = self.skills_advanced[final_name]
                            skills.append((final_name, skill_advances))

                        # skill name is new, even for skill_advanced
                        else:
                            skills.append((skill_name, 0))
            # parse
            out_skills = self.parse_skill_words(skills)  # {skill_name: advance_value}

            # check if 8 skills available
            if len(out_skills) != 8:
                error = f'{pre_desc}Less then 8 skills available. ' \
                        f'career={self.career_current.name}, skill_names={skill_names}, out_skills={out_skills}'
                logger.error(error)
                raise Exception(error)

            # advance
            for skill_name in out_skills.keys():
                advance = out_skills[skill_name]
                if advance < adv_sum:
                    for j in range(adv_sum - advance):
                        cost = get_cost(advance)
                        if xp_val >= cost:
                            advance += 1
                            # add to previous value!
                            self.add_skills({skill_name: 1})
                            xp_val -= cost
                        else:
                            reason = f'To upgrade skill:{skill_name} to lvl: {advance}/{adv_sum} cost>xp: {cost}>{xp_val}'
                            break
                    if len(reason) > 0:
                        break

                if advance >= adv_sum:
                    cnt += 1
                else:
                    reason = f'Skill:{skill_name} advance<adv_sum: {advance}<{adv_sum}'
                    break

            # return advance not completed
            if len(reason) > 0:
                return xp_val, False, reason
            if cnt != 8:
                reason = f'Number of fully advanced skills: {cnt} != 8'
                return xp_val, False, reason
            # return advance fully completed
            return xp_val, True, reason
        def advance_next_level(xp_val, npc):
            """
            To be able to advance to next career level, npc must have:
            -> all stats advanced: (already fulfilled)!
            -> 8 skills advanced: (already fulfilled)!
            -> at least 1 talent advanced: (already fulfilled)!
            -> 100 xp: ?
            Note: for npc's age=='Young' only career lvl 0 is available
            :return: xp: int
            :return: boolean: Was there enough xp to advance to next career level?
            :return: reason
            """
            if xp_val < 100:
                return xp_val, False, f'Not enough xp: {xp_val}<100'

            if self.age_str == 'Young' and self.career_level >= 2:
                return xp_val, False, f'Young npc cannot have high career level: {self.career_level+1}/4'

            if self.career_level == 3:
                return xp_val, False, f'Reached highest career level: 4/4'

            # deduct xp
            xp_val -= 100
            # switch to new career
            npc.career_level += 1
            npc.career_current = npc.career_main.lvl[npc.career_level]
            npc.status = npc.career_current.status

            # new skills - will be added in next iteration
            # new talents - will be added in next iteration

            # new trappings
            npc.trapping = npc.roll_trappings(npc.trapping + ", " + npc.career_current.trappings)
            # new money
            npc.money = npc.money + ', ' + npc.roll_money(npc.career_current.status)

            return xp_val, True, f''

        if xp_0 is None:
            xp_0 = self.xp_start

        if 0 <= self.career_level <= 3:
            logger.debug(f'\t- Career lvl {self.career_level+1}')
            # ---- Talents
            xp_1, f_1, reason_1 = advance_talents(xp_0)
            self.update_all()
            logger.debug(f'\t\ttalents, xp_spent={xp_0-xp_1}')
            if not f_1:
                self.xp_left = xp_1
                logger.debug(f'\t\t\tstopped! reason={reason_1}, xp_left={self.xp_left}')
                return
            # --- Stats
            xp_2, f_2, reason_2 = advance_stats(xp_1)
            self.update_all()
            logger.debug(f'\t\tstats, xp_spent={xp_1-xp_2}')
            if not f_2:
                self.xp_left = xp_2
                logger.debug(f'\t\t\tstopped! reason={reason_2}, xp_left={self.xp_left}')
                return
            # ---- Skills
            xp_3, f_3, reason_3 = advance_skills(xp_2)
            self.update_all()
            logger.debug(f'\t\tskills, xp_spent={xp_2-xp_3}')
            if not f_3:
                self.xp_left = xp_3
                logger.debug(f'\t\t\tstopped! reason={reason_3}, xp_left={self.xp_left}')
                return
            # ---- Advance to next level?
            xp_4, f_4, reason_4 = advance_next_level(xp_3, self)
            self.update_all()
            if f_4:
                logger.debug(f'\t\tadvance to next level, xp_spent={xp_0-xp_4}, xp_left={xp_4}')
                self.advance_by_xp(xp_4)  # repeat the function
            else:
                self.xp_left = xp_4
                logger.debug(f'\t\t\tstopped! reason={reason_4}, xp_left={self.xp_left}')
                return

    def advance_continue(self, xp_0):
        """
        Continue advancing, after reaching career lvl 3
        """
        from constants import talents_all

        def get_plan():
            pre_desc = 'NpcSingleton.advance_continue.get_plan: '

            # TALENTS - for current career level: value = max value
            plan_talents = []
            for talent_name, (talent_test, talent_advance, talent_description) in self.talents.items():
                # get limit
                short_name = talent_name.split(' (')[0]
                limit, _, _, _ = talents_all[short_name]
                if limit.isdecimal():
                    max_advance = int(limit)
                elif limit.find('Bonus') >= 0:
                    stat_name = limit[6:]
                    _, _, total = self.attributes[stat_name]  # base, advance, total
                    stat_bonus_val = total // 10
                    max_advance = stat_bonus_val
                else:
                    error = f'{pre_desc}Unknown talent max value: {limit}'
                    logger.error(error)
                    raise Exception(error)
                # add
                if talent_advance < max_advance:
                    plan_talents.append((talent_name, max_advance))

            # STATS - for all career levels: max_value + 10
            #   get all stat names
            plan_stats = []
            stat_names = []     # e.g. ['T', 'DEX', 'INT']
            for i in range(0, self.career_level+1):
                stat_names = stat_names + self.career_main.lvl[i].advances
            max_advance = max([self.attributes[stat_name][1] for stat_name in stat_names]) + 10
            # add
            for stat_name in stat_names:
                plan_stats.append((stat_name, max_advance))

            # SKILLS - all above 0: max_value + 10
            #   get all skills
            plan_skills = []
            skills = []     # e.g. [('Art', basic), ...]
            max_advance = 0
            for skill_name, [_, _, skill_advances, _] in self.skills_basic.items():
                if skill_advances > 0:
                    skills.append((skill_name, 'basic'))
                    if skill_advances > max_advance:
                        max_advance = skill_advances
            for skill_name, [_, _, skill_advances, _] in self.skills_advanced.items():
                if skill_advances > 0:
                    skills.append((skill_name, 'advanced'))
                    if skill_advances > max_advance:
                        max_advance = skill_advances
            max_advance = max_advance + 10
            # add
            for skill_name, skill_type in skills:
                plan_skills.append((skill_name, skill_type, max_advance))

            # final result
            out_plan = {'talents': plan_talents,  # [ (talent_name, max_advance) ]
                        'stats':   plan_stats,    # [ (stat_name, max_advance) ]
                        'skills':  plan_skills}   # [ (skill_name, skill_type, max_advance) ]

            return out_plan

        def advance_talents(xp_val):
            """
            :return: xp: int
            :return: boolean: Was there enough xp to fully advance in this domain?
            :return: reason
            """
            cnt = 0
            reason = ''

            # advance
            out_talents = {}
            for (talent_name, max_advance) in plan['talents']:
                (talent_test, talent_advance, talent_description) = self.talents[talent_name]
                for val in range(talent_advance+1, max_advance+1):
                    cost = 100 + (val-1)*100
                    if xp_val >= cost:
                        xp_val -= cost
                        self.talents.update({talent_name: (talent_test, val, talent_description)})
                        out_talents.update({talent_name: val})
                    else:
                        reason = f'To upgrade talent:{talent_name} to lvl: {val}/{max_advance} cost>xp: {cost}>{xp_val}'
                        break
                if len(reason) > 0:
                    break
                if self.talents[talent_name][1] >= max_advance:
                    cnt += 1
                else:
                    reason = f'Talent:{talent_name} advance<adv_sum: {self.talents[talent_name][1]}<{max_advance}'
                    break

            # modify
            self.modify_stats_by_talents(out_talents)

            # return advance not completed
            if len(reason) > 0:
                return xp_val, False, reason
            if cnt != len(plan['talents']):
                reason = f'Number of fully advanced talents: {cnt} != {len(plan["talents"])}'
                return xp_val, False, reason
            # return advance fully completed
            return xp_val, True, reason

        def advance_stats(xp_val):
            """
            :return: xp: int
            :return: boolean: Was there enough xp to fully advance in this domain?
            :return: reason
            """
            def get_cost(stat_val):
                if 0 <= stat_val <= 5:
                    return 25
                elif 6 <= stat_val <= 10:
                    return 30
                elif 11 <= stat_val <= 15:
                    return 40
                elif 16 <= stat_val <= 20:
                    return 50
                elif 21 <= stat_val <= 25:
                    return 70
                elif 26 <= stat_val <= 30:
                    return 90
                elif 31 <= stat_val <= 35:
                    return 120
                elif 36 <= stat_val <= 40:
                    return 150
                elif 41 <= stat_val <= 45:
                    return 190
                elif 46 <= stat_val <= 50:
                    return 320
                else:
                    return (stat_val-50)//5 * 30 + 350  # own formula
            cnt = 0
            reason = ''

            # advance
            for stat_name, adv_sum in plan['stats']:    # plan['stats'] = [(stat_name, max_advance), ... ]
                [base, advance, total] = self.attributes[stat_name]
                if advance < adv_sum:
                    for j in range(adv_sum - advance):
                        current_advance = self.attributes[stat_name][1]
                        cost = get_cost(current_advance)
                        if xp_val >= cost:
                            current_advance += 1
                            current_total = base + current_advance
                            # update!
                            self.attributes.update({stat_name: [base, current_advance, current_total]})
                            xp_val -= cost
                        else:
                            reason = f'To upgrade attribute:{stat_name} to lvl: {current_advance}/{adv_sum} cost>xp: {cost}>{xp_val}'
                            break
                    if len(reason) > 0:
                        break
                if self.attributes[stat_name][1] >= adv_sum:
                    cnt += 1
                else:
                    reason = f'Attribute:{stat_name} advance<adv_sum: {self.attributes[stat_name][1]}<{adv_sum}'
                    break

            # return advance not completed
            if len(reason) > 0:
                return xp_val, False, reason
            if cnt != len(plan['stats']):
                reason = f'Number of fully advanced attributes: {cnt} != {len(plan["stats"])}'
                return xp_val, False, reason
            # return advance fully completed
            return xp_val, True, reason

        def advance_skills(xp_val):
            """
            :return: xp: int
            :return: boolean: Was there enough xp to fully advance in this domain?
            :return: reason
            """
            def get_cost(skill_val):
                if 0 <= skill_val <= 5:
                    return 10
                elif 6 <= skill_val <= 10:
                    return 15
                elif 11 <= skill_val <= 15:
                    return 20
                elif 16 <= skill_val <= 20:
                    return 30
                elif 21 <= skill_val <= 25:
                    return 40
                elif 26 <= skill_val <= 30:
                    return 60
                elif 31 <= skill_val <= 35:
                    return 80
                elif 36 <= skill_val <= 40:
                    return 110
                elif 41 <= skill_val <= 45:
                    return 140
                elif 46 <= skill_val <= 50:
                    return 180
                else:
                    return (skill_val-50)//5 * 30 + 210  # own formula
            cnt = 0
            reason = ''

            # advance
            for skill_name, skill_type, adv_sum in plan['skills']:  # [(skill_name, skill_type, max_advance), ... ]
                if skill_type == 'basic':
                    _, _, advance, _ = self.skills_basic[skill_name]
                else:
                    _, _, advance, _ = self.skills_advanced[skill_name]
                if advance < adv_sum:
                    for j in range(adv_sum - advance):
                        cost = get_cost(advance)
                        if xp_val >= cost:
                            advance += 1
                            # add to previous value!
                            self.add_skills({skill_name: 1})
                            xp_val -= cost
                        else:
                            reason = f'To upgrade skill:{skill_name} to lvl: {advance}/{adv_sum} cost>xp: {cost}>{xp_val}'
                            break
                    if len(reason) > 0:
                        break
                if advance >= adv_sum:
                    cnt += 1
                else:
                    reason = f'Skill:{skill_name} advance<adv_sum: {advance}<{adv_sum}'
                    break

            # return advance not completed
            if len(reason) > 0:
                return xp_val, False, reason
            if cnt != len(plan["skills"]):
                reason = f'Number of fully advanced skills: {cnt} != {len(plan["skills"])}'
                return xp_val, False, reason
            # return advance fully completed
            return xp_val, True, reason

        plan = get_plan()

        if len(plan['talents']) > 0:
            # ---- Talents
            xp_1, f_1, reason_1 = advance_talents(xp_0)
            self.update_all()
            logger.debug(f'\t\ttalents, xp_spent={xp_0-xp_1}')
            if not f_1:
                self.xp_left = xp_1
                logger.debug(f'\t\t\tstopped! reason={reason_1}, xp_left={self.xp_left}')
                return
        else:
            xp_1 = xp_0

        # --- Stats
        xp_2, f_2, reason_2 = advance_stats(xp_1)
        self.update_all()
        logger.debug(f'\t\tstats, xp_spent={xp_1-xp_2}')
        if not f_2:
            self.xp_left = xp_2
            logger.debug(f'\t\t\tstopped! reason={reason_2}, xp_left={self.xp_left}')
            return

        # ---- Skills
        xp_3, f_3, reason_3 = advance_skills(xp_2)
        self.update_all()
        logger.debug(f'\t\tskills, xp_spent={xp_2-xp_3}')
        if not f_3:
            self.xp_left = xp_3
            logger.debug(f'\t\t\tstopped! reason={reason_3}, xp_left={self.xp_left}')
            return

        # ---- Continue (if not returned at this point)
        self.advance_continue(xp_3)

    def update_attributes(self):
        # stats - calculate all total values
        for stat_name in self.attributes.keys():
            [base, advance, total] = self.attributes[stat_name]   # {stat_name: [base, advance, total]}
            total = base + advance
            self.attributes.update({stat_name: [base, advance, total]})

        # wounds - calculate based on new stats
        bonusS = self.attributes['S'][2] // 10  # total
        bonusT = self.attributes['T'][2] // 10  # total
        bonusWP = self.attributes['WP'][2] // 10  # total
        if self.species == "Human":
            wounds_val = bonusS + 2 * bonusT + bonusWP
        elif self.species == "Dwarf":
            wounds_val = bonusS + 2 * bonusT + bonusWP
        elif self.species == "Halfling":
            wounds_val = 2 * bonusT + bonusWP
        elif self.species == "High Elf":
            wounds_val = bonusS + 2 * bonusT + bonusWP
        elif self.species == "Wood Elf":
            wounds_val = bonusS + 2 * bonusT + bonusWP
        elif self.species == "Gnome":
            wounds_val = 2 * bonusT + bonusWP
        self.attributes.update({'Wounds': [wounds_val, 0, wounds_val]})

    @staticmethod
    def parse_skill_words(in_skills):
        """
        :param in_skills:     [(skill_name, advance), ...]
        :return: out_skills:  {skill_name: advance_value}
        """
        from functions import random_pick
        from constants import skills_all
        pre_desc = f'NpcSingleton.parse_skill_words: '

        in_skills_names = [name for name, advance in in_skills]
        out_skills = {}
        # get all 'normal' names
        for skill_name, advance in in_skills:
            if skill_name.find("(Any one)") < 0:
                # unique!
                if skill_name in out_skills.keys():
                    error = f'{pre_desc}Parsed skill name: {skill_name} already exists: {out_skills.keys()}'
                    logger.error(error)
                    raise Exception(error)
                # add
                out_skills.update({skill_name: advance})

        # (Any one) -> choose one from list
        for skill_name, advance in in_skills:
            if skill_name.find("(Any one)") >= 0:
                short_name = skill_name[:skill_name.find('(Any one)') - 1]
                _, _, list_of_choices = skills_all[short_name]
                # unique!
                choose_list = list(set([short_name + ' (' + choice_name + ')' for choice_name in list_of_choices]) - set(in_skills_names) - set(out_skills.keys()))
                new_name = random_pick(choose_list)
                # unique!
                if new_name in out_skills.keys():
                    error = f'{pre_desc}Parsed skill name: {new_name} already exists: {out_skills.keys()}'
                    logger.error(error)
                    raise Exception(error)
                # add
                out_skills.update({new_name: advance})

        # check if same length
        if len(in_skills) != len(out_skills):
            error = f'{pre_desc}Length of input ({len(in_skills)}) != length of output ({len(out_skills)})'
            logger.error(error)
            raise Exception(error)

        return out_skills
    def add_skills(self, in_skills):
        """
        :param in_skills:     {skill_name: advance_value}
        Note: only unique names allowed!
        Note: if skill name already exists -> increase advance value!
        """
        from constants import skills_all_basic, skills_all_advanced
        pre_desc = f'NpcSingleton.add_skills: '

        # check if input unique
        if len(set(in_skills.keys())) != len(in_skills.keys()):
            error = f'{pre_desc}Input names are not unique: {in_skills.keys()})'
            logger.error(error)
            raise Exception(error)

        # {skill_name: [stat_str, stat_total, skill_advances, skill_total]}
        for skill_name, advance in in_skills.items():
            # skill belongs to basic group?
            name_short = skill_name.split(' (')[0]
            if name_short in skills_all_basic.keys():
                # skill must exists -> increase advance value
                [stat_str, stat_total, skill_advances, skill_total] = self.skills_basic[name_short]
                skill_advances += advance
                skill_total = stat_total + skill_advances
                self.skills_basic.update({name_short: [stat_str, stat_total, skill_advances, skill_total]})

            # skill belongs to advanced group?
            else:
                # skill already exists? -> increase value: skill_advances
                if skill_name in self.skills_advanced.keys():
                    [stat_str, stat_total, skill_advances, skill_total] = self.skills_advanced[skill_name]
                    skill_advances += advance
                    skill_total = stat_total + skill_advances
                    self.skills_advanced.update({skill_name: [stat_str, stat_total, skill_advances, skill_total]})
                # create new entry
                else:
                    [stat_str, _, _] = skills_all_advanced[name_short]  # ["INT", "advanced", ["Grey Order", "Guild"]
                    [_, _, stat_total] = self.attributes[stat_str]    # [base, advance, total]
                    skill_advances = advance
                    skill_total = stat_total + skill_advances
                    self.skills_advanced.update({skill_name: [stat_str, stat_total, skill_advances, skill_total]})
    def update_skills(self):
        # recalculate: stat_total, skill_advances, skill_total
        for skill_name, [stat_str, stat_total, skill_advances, skill_total] in self.skills_basic.items():
            [_, _, stat_total] = self.attributes[stat_str]  # [base, advance, total]
            skill_total = stat_total + skill_advances
            self.skills_basic.update({skill_name: [stat_str, stat_total, skill_advances, skill_total]})

        for skill_name, [stat_str, stat_total, skill_advances, skill_total] in self.skills_advanced.items():
            [_, _, stat_total] = self.attributes[stat_str]  # [base, advance, total]
            skill_total = stat_total + skill_advances
            self.skills_advanced.update({skill_name: [stat_str, stat_total, skill_advances, skill_total]})

        # filter only skills with at least 1 advance
        #out2 = {}
        #for skill_name, values_list in out.items():
        #    if values_list[2] > 0:
        #        out2.update({skill_name: values_list})
        #self.skills_advanced = out2
        #if len(found_total) != len(self._SkillNames): logger.debug("Not all skills were found", 'FOUND:', found_total, 'ALL:', self._SkillNames)

    @staticmethod
    def parse_talent_words(in_talents):
        """
        :param in_talents:     [(talent_name, advance), ...]
        :return: out_talents:  {talent_name: advance_value}
        """
        from functions import random_pick, roll1d100
        from constants import talents_random, talents_all
        pre_desc = f'NpcSingleton.parse_talent_words: '

        in_talents_names = [name for name, advance in in_talents]
        out_talents = {}    # {talent_name: advance_value}
        for talent_name, advance in in_talents:
            name = talent_name
            # sth " or " sth
            if name.find(" or ") >= 0:
                two_talents = name.split(" or ")
                # unique!
                choose_list = list(set(two_talents) - set(in_talents_names) - set(out_talents.keys()))
                name = random_pick(choose_list)  # pick one from two talents

            # Random
            if name == "Random":
                # unique!
                choose_list = list(set(talents_random) - set(in_talents_names) - set(out_talents.keys()))
                name = random_pick(choose_list)

            # (Any one)
            if name.find("(Any one)") >= 0:
                short_name = name[:name.find('(Any one)') - 1]
                [_, _, _, list_of_choices] = talents_all[short_name]  # ["Bonus I", "Perception", "Perception test...", ["Vision", "Taste"]]
                # unique!
                choose_list = list(set([short_name + ' (' + choice_name + ')' for choice_name in list_of_choices]) -
                                   set(in_talents_names) - set(out_talents.keys()))
                name = random_pick(choose_list)

            # check if unique
            if name in out_talents.keys():
                error = f'{pre_desc}Parsed talent name ({name}) already exists ({out_talents.keys()})'
                logger.error(error)
                raise Exception(error)
            # add
            out_talents.update({name: advance})

        # check if same length
        if len(in_talents) != len(out_talents):
            error = f'{pre_desc}Length of input ({len(in_talents)}) != length of output ({len(out_talents)})'
            logger.error(error)
            raise Exception(error)

        return out_talents
    def add_talents(self, in_talents):
        """
        :param in_talents:     {talent_name: advance}
        Note: only unique names allowed!
        Note: only new talents will be added!
        """
        from constants import talents_all
        pre_desc = f'NpcSingleton.add_talents: '

        # check if input unique
        if len(set(in_talents.keys())) != len(in_talents.keys()):
            error = f'{pre_desc}Input names are not unique: {in_talents.keys()})'
            logger.error(error)
            raise Exception(error)

        for talent_name, advance in in_talents.items():
            if talent_name not in self.talents.keys():
                short_name = talent_name.split(' (')[0]
                [_, test, description, _] = talents_all[short_name]  # ["Bonus I", "Perception", "Perception test...", ["Vision", "Taste"]]
                self.talents.update({talent_name: (test, advance, description)})  # {talent_name: (test, advance, description)}
    def modify_stats_by_talents(self, in_talents):
        """
        :param in_talents: {talent_name: advance_value}
        Note: only for the new ones
        """
        # add values to base stats
        # done for talents with max advance==1
        for talent_name, talent_advance in in_talents.items():
            if talent_advance > 0 and talent_name not in self.talents.keys():
                if talent_name == "Coolheaded":
                    # WP+5
                    [base, advance, total] = self.attributes['WP']  # {stat_name: [base, advance, total]}
                    self.attributes.update({'WP': [base+5, advance, total]})
                elif talent_name == "Fleet footed":
                    # MoveSpeed+1
                    [base, advance, total] = self.attributes['MoveSpeed']
                    self.attributes.update({'MoveSpeed': [base+1, advance, total]})
                elif talent_name == "Lightning Reflexes":
                    # AG+5
                    [base, advance, total] = self.attributes['AG']
                    self.attributes.update({'AG': [base+5, advance, total]})
                elif talent_name == "Marksman":
                    # BS+5
                    [base, advance, total] = self.attributes['BS']
                    self.attributes.update({'BS': [base+5, advance, total]})
                elif talent_name == "Nimble Fingered":
                    # DEX+5
                    [base, advance, total] = self.attributes['DEX']
                    self.attributes.update({'DEX': [base+5, advance, total]})
                elif talent_name == "Savvy":
                    # INT+5
                    [base, advance, total] = self.attributes['INT']
                    self.attributes.update({'INT': [base+5, advance, total]})
                elif talent_name == "Sharp":
                    # I+5
                    [base, advance, total] = self.attributes['I']
                    self.attributes.update({'I': [base+5, advance, total]})
                elif talent_name == "Suave":
                    # FEL+5
                    [base, advance, total] = self.attributes['FEL']
                    self.attributes.update({'FEL': [base+5, advance, total]})
                elif talent_name == "Very Resilient":
                    # T+5
                    [base, advance, total] = self.attributes['T']
                    self.attributes.update({'T': [base+5, advance, total]})
                elif talent_name == "Very Strong":
                    # S+5
                    [base, advance, total] = self.attributes['S']
                    self.attributes.update({'S': [base+5, advance, total]})
                elif talent_name == "Warrior Born":
                    # WS+5
                    [base, advance, total] = self.attributes['WS']
                    self.attributes.update({'S': [base+5, advance, total]})

        # update attributes
        self.update_attributes()

    def final_modifications(self):
        pre_desc = f'NpcSingleton.final_modifications: '

        # Modify by talent description
        for talent_name, (talent_test, talent_advance, talent_description) in self.talents.items():
            # Hardy:    Wounds += Toughness Bonus
            if talent_name == "Hardy":
                bonusT = self.attributes['T'][2] // 10
                attribute_base, attribute_advance, attribute_total = self.attributes['Wounds']
                self.attributes.update({'Wounds': [attribute_base, attribute_advance+bonusT, attribute_total]})

            # Luck:     Fortune max == Fate max + [lvl]
            elif talent_name == "Luck":
                attribute_base, attribute_advance, attribute_total = self.attributes['Fate']
                self.attributes.update({'Fortune': [attribute_base, attribute_advance+talent_advance, attribute_total]})

            # Strong-minded: Resolve max += [lvl]
            elif talent_name == "Strong-minded":
                attribute_base, attribute_advance, attribute_total = self.attributes['Resolve']
                self.attributes.update({'Resolve': [attribute_base, attribute_advance+talent_advance, attribute_total]})

            # Artistic: Add Trade (Artist) to any career
            elif talent_name == "Artistic":
                self.add_skills({"Trade (Artist)": talent_advance})

            # Craftsman: Add Trade (Any one) to any career
            elif talent_name == "Craftsman":
                in_skills = {"Trade (Any one)": talent_advance}
                in_skills = self.parse_skill_words(in_skills)
                self.add_skills(in_skills)

            # Perfect Pitch: Add Performer (Sing) to any career
            elif talent_name == "Perfect Pitch":
                self.add_skills({"Entertain (Sing)": talent_advance})

            # Seasoned Traveller: Add Lore (Local) to any career
            elif talent_name == "Seasoned Traveller":
                self.add_skills({"Lore (Local)": talent_advance})

            # Witch!:   Add Language (Magick) to any career
            elif talent_name == "Witch!":
                self.add_skills({"Language (Magick)": talent_advance})

            # talent_description includes: [lvl] or [lvl*number]
            lvl_idx = talent_description.find('[lvl')
            if lvl_idx >= 0:
                # [lvl]
                if talent_description[lvl_idx+4] == ']':
                    talent_description = talent_description.replace('[lvl]', str(talent_advance))
                # [lvl*number]
                elif talent_description[lvl_idx+4] == '*':
                    end_idx = lvl_idx+4 + talent_description[lvl_idx+4:].find(']')
                    val = int(talent_description[lvl_idx+5: end_idx])
                    lvl_str = talent_description[lvl_idx: end_idx+1]
                    talent_description = talent_description.replace(lvl_str, str(talent_advance*val))
                else:
                    error = f'{pre_desc}Talent description includes not handled "lvl" string -> {talent_description}'
                    logger.error(error)
                    raise Exception(error)
                # modify
                self.talents.update({talent_name: (talent_test, talent_advance, talent_description)})

        self.update_all()

        # Modify Money (sum up common coins)
        splits = self.money.split(', ')
        gold, silver, brass = 0, 0, 0
        for split in splits:
            idx = split.find('Gold')
            if idx >= 0:
                gold += int(split[:idx])
            idx = split.find('Silver')
            if idx >= 0:
                silver += int(split[:idx])
            idx = split.find('Brass')
            if idx >= 0:
                brass += int(split[:idx])
        out_str = ''
        for val, name in zip([gold, silver, brass], ['Gold', 'Silver', 'Brass']):
            if val > 0:
                if len(out_str) > 0:
                    out_str = out_str + ', '
                out_str = out_str + str(val) + ' ' + name + ' coins'
        if len(out_str) == 0:
            out_str = '0 coins'
        self.money = out_str

        # Remove Talents and Skills Advanced, if advance value == 0
        to_delete = [name for name, (_, advance, _) in self.talents.items() if advance == 0]
        for talent_name in to_delete:
            self.talents.pop(talent_name)
        if len(to_delete):
            logger.debug(f'\t\tremoved talents (advance value == 0): {to_delete}')
        to_delete = [name for name, [_, _, advance, _] in self.skills_advanced.items() if advance == 0]
        for skill_name in to_delete:
            self.skills_advanced.pop(skill_name)
        if len(to_delete):
            logger.debug(f'\t\tremoved skills (advance value == 0): {to_delete}')


# function "present" -> obsolete, not used
"""
    def present(self):
        # update
        self.update_all()
        logger.debug(f'Name: {self.name}')
        logger.debug(f'{self.sex_str}, {self.species}, Age: {self.age}, Height: {self.height:.2f}m')
        logger.debug(f'Class: {ClassAll[self._ClassN]}, Career: {self._CareerName}, Status: {CareerSocialL1[self._CareerN]}')
        logger.debug(f'Appearance: ')
        for text in self.desc_appearance: logger.debug(f'\t {text}')
        logger.debug(f'General: {self.desc_gen_look}')
        logger.debug(f'Traits:')
        for text in self.desc_traits[0:3]: logger.debug(f'\t {text}')
        logger.debug(f'Reactions:')
        for text in self.desc_reactions: logger.debug(f'\t {text}')
        logger.debug('------------------------------------------------------------------------------')
        # {skill_name: [stat_str, stat_total, skill_advances, skill_total]}
        logger.debug(f'Skills Basic:')
        for skill_name, values_list in self.skills_basic.items(): logger.debug(f'\t{skill_name}\t{values_list}')
        logger.debug(f'Skills Advanced:')
        for skill_name, values_list in self.skills_advanced.items(): logger.debug(f'\t{skill_name}\t{values_list}')
        # {talent_name: talent's description]}
        logger.debug(f'Talents:')
        for talent_name, talent_description in self.talents.items(): logger.debug(f'\t{talent_name}\t->\t{talent_description}')
        logger.debug(f'Stats:')
        for stat_name, stat_value in self.attributes.items(): logger.debug(f'\t{stat_name}\t{stat_value}')
        logger.debug('------------------------------------------------------------------------------')
        if self._Dooming is not None:
            logger.debug(f'Dooming: {self._Dooming}')
        logger.debug(f'Trapping: {self._Trapping}')
        logger.debug(f'Money: {self._Money}')
    """



