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
        self.attributes = {           # {stat_name: [base, advance, total]}
            "WS": [0, 0, 0], "BS": [0, 0, 0], "S": [0, 0, 0], "T": [0, 0, 0], "AG": [0, 0, 0],
            "I": [0, 0, 0], "DEX": [0, 0, 0], "INT": [0, 0, 0], "WP": [0, 0, 0], "FEL": [0, 0, 0],
            "Wounds": [0, 0, 0], "MoveSpeed": [0, 0, 0], "Fate": [0, 0, 0], "Resilience": [0, 0, 0]}
        self.skills_basic = {}        # {skill_name: [stat_str, stat_total, skill_advances, skill_total]}
        self.skills_advanced = {}     # {skill_name: [stat_str, stat_total, skill_advances, skill_total]}
        self.talents = {}             # {talent_name: (test, description)}

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
            [_, _, stat_total] = self.attributes[stat_str]  # [base, advance, total]
            self.skills_basic.update({skill_name: [stat_str, stat_total, 0, stat_total]})

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
        self.attributes.update({'Wounds': [wounds_val, 0, 0]})
        # roll move speed
        self.attributes.update({'MoveSpeed': [attributes_by_species[self.species]['MoveSpeed'], 0, 0]})
        # roll fate
        extra_val = attributes_by_species[self.species]['Extra']
        roll_val = random.randint(0, extra_val)
        self.attributes.update({'Fate': [attributes_by_species[self.species]['Fate'] + roll_val, 0, 0]})
        # roll resilience
        rest_val = extra_val - roll_val
        self.attributes.update({'Resilience': [attributes_by_species[self.species]['Resilience'] + rest_val, 0, 0]})
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
        from constants import skills_by_species

        # roll 6 skills
        in_skills = skills_by_species[self.species]
        out_skills = {}     # {skill_name: advance_value}
        indexes = []
        while len(indexes) < 6:
            idx = random.randint(0, len(in_skills) - 1)
            if idx not in indexes:
                indexes.append(idx)
                out_skills.update({in_skills[idx]: 0})

        # advance skills values
        for i, skill_name in enumerate(out_skills.keys()):
            if i < 3:
                out_skills.update({skill_name: 5})  # advance 3 skills by value: 5
            else:
                out_skills.update({skill_name: 3})  # advance 3 skills by value: 5

        # parse
        out_skills = self.parse_skill_words(out_skills)
        # add
        self.add_skills(out_skills)
        # update
        self.update_skills()
    def roll_talents_species(self):
        from constants import talents_by_species

        # roll 5 talents
        in_talents = talents_by_species[self.species]
        out_talents = {talent_name: 1 for talent_name in in_talents}    # {talent_name: advance_value}
        # parse
        out_talents = self.parse_talent_words(out_talents)
        # add
        self.add_talents(out_talents)
        # modify
        self.modify_stats_by_talents(out_talents)
    def set_skills_career(self):
        from functions import random_pick
        # add 8 skills
        out_skills = {skill_name: 0 for skill_name in self.career_current.skills}  # {skill_name: value}
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
        for i, skill_name in enumerate(out_skills.keys()):
            out_skills.update({skill_name: out_values[i]})

        # parse
        out_skills = self.parse_skill_words(out_skills)
        # add
        self.add_skills(out_skills)
        # update
        self.update_skills()
    def set_talents_career(self):
        from functions import random_pick
        # get unique talent names
        talent_names = list(set(self.career_current.talents) - set(self.talents.keys()))
        # pick only one
        out_talents = {random_pick(talent_names): 1}    # {talent_name: advance_value}
        # parse
        out_talents = self.parse_talent_words(out_talents)
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

    def advance_by_xp(self, xp=None):
        """
        Advance from career lvl 0 to lvl 3
        """
        def advance_talents(xp_val):
            """
            Advance (by 1 value) all missing talents from current career
            :return: xp: int
            :return: boolean: Was there enough xp to fully advance in this domain?
            """
            cnt = 0

            # get talents from current career
            out_talents = {talent_name: 1 for talent_name in self.career_current.talents}    # {talent_name: advance_value}
            #   remove already owned talents
            for talent_name in self.talents.keys():
                if talent_name in out_talents.keys():
                    del(out_talents[talent_name])
            # parse
            out_talents = self.parse_talent_words(out_talents)
            # add new talents
            for talent_name, advance in out_talents.items():
                if xp_val >= 100:
                    # add
                    self.add_talents({talent_name: advance})
                    # modify
                    self.modify_stats_by_talents({talent_name: advance})
                    xp_val -= 100   # advancing talent to 1 costs 100xp
                    cnt += 1

            if cnt == len(out_talents):
                return xp_val, True
            else:
                return xp_val, False
        def advance_stats(xp_val):
            """
            ALL stats for current and previous careers -> advance to 'adv_sum' value
            :return: xp: int
            :return: boolean: Was there enough xp to fully advance in this domain?
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

                if self.attributes[stat_name][1] >= adv_sum:
                    cnt += 1

            if cnt == len(stat_names):
                return xp_val, True
            else:
                return xp_val, False
        def advance_skills(xp_val):
            """
            8 skills from current and previous careers -> advance to 'adv_sum' value
            :return: xp: int
            :return: boolean: Was there enough xp to fully advance in this domain?
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

            adv_sum = (self.career_level + 1) * 5
            # get all skill names
            skill_names = []
            for i in range(self.career_level, -1, -1):
                skill_names = skill_names + self.career_main.lvl[i].skills   # e.g. ['Lore (Any)', 'Track']
            #   pick 8 randomly, without repetitions
            skill_names = random.sample(skill_names, 8)

            # get current advance values of skills
            out_skills = {}  # {skill_name: advance_value}
            for skill_name in skill_names:
                name_short = skill_name.split(' (')[0]

                # in skill_basic?
                if name_short in self.skills_basic.keys():
                    [_, _, skill_advances, _] = self.skills_basic[name_short]  # [stat_str, stat_total, skill_advances, skill_total]
                    out_skills.update({skill_name: skill_advances})

                # in skill_advanced?
                else:
                    # try skill's full name
                    if skill_name in self.skills_advanced.keys():
                        [_, _, skill_advances, _] = self.skills_advanced[skill_name]  # [stat_str, stat_total, skill_advances, skill_total]
                        out_skills.update({skill_name: skill_advances})
                    else:
                        # skill name has '(Any one)' and there is according name in skill_advanced?
                        if skill_name.find('(Any one)') >= 0 and name_short in [name.split(' (')[0] for name in self.skills_advanced.keys()]:
                            # {skill_name: [stat_str, stat_total, skill_advances, skill_total]}
                            tmp = [(name, val) for name, [_, _, val, _] in self.skills_advanced.items() if name.find(name_short) >= 0]
                            tmp.sort()
                            final_name = tmp[-1][0]  # pick skill with the highest advance value
                            [_, _, skill_advances, _] = self.skills_advanced[final_name]
                            out_skills.update({final_name: skill_advances})

                        # skill name is new, even for skill_advanced
                        else:
                            out_skills.update({skill_name: 0})
            # parse
            out_skills = self.parse_skill_words(out_skills)

            # error?
            if len(out_skills) != 8:
                raise Exception(f'advance_stats:advance_skills -> less then 8 skills available, cannot advance.\n'
                                f'career={self.career_current.name}, skill_names={skill_names}, out_skills={out_skills}')

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

                if advance >= adv_sum:
                    cnt += 1

            if cnt == 8:
                return xp_val, True
            else:
                return xp_val, False
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
            """

            if self.age_str != 'Young' and 0 <= self.career_level <= 2 and xp_val >= 100:
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

                return xp_val, True
            else:
                return xp_val, False

        if xp is None:
            xp = self.xp_start

        if 0 <= self.career_level <= 3:
            # ---- Talents
            xp, f_full_advance = advance_talents(xp)
            self.update_all()
            if not f_full_advance:
                self.xp_left = xp
                return
            # --- Stats
            xp, f_full_advance = advance_stats(xp)
            self.update_all()
            if not f_full_advance:
                self.xp_left = xp
                return
            # ---- Skills
            xp, f_full_advance = advance_skills(xp)
            self.update_all()
            if not f_full_advance:
                self.xp_left = xp
                return
            # ---- Advance to next level?
            xp, f_advanced = advance_next_level(xp, self)
            self.update_all()
            if f_advanced:
                self.advance_by_xp(xp)  # continue advancing...
            else:
                self.xp_left = xp
                return

    def advance_continue(self, xp=None):
        """
        Continue advancing, after reaching career lvl 3
        """
        def advance_stats(xp_val):
            """
            ALL stats for current and previous careers -> advance to 'adv_sum' value
            :return: xp: int
            :return: boolean: Was there enough xp to fully advance in this domain?
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
                    return (stat_val - 50) // 5 * 30 + 350  # own formula
            cnt = 0

            # get all stat names
            stat_names = []
            for i in range(0, self.career_level + 1):
                stat_names = stat_names + self.career_main.lvl[i].advances  # e.g. ['T', 'DEX', 'INT']
            # get adv sum
            adv_sum = max([self.attributes[stat_name][1] for stat_name in stat_names]) + 10

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

                if self.attributes[stat_name][1] >= adv_sum:
                    cnt += 1

            if cnt == len(stat_names):
                return xp_val, True
            else:
                return xp_val, False
        def advance_skills(xp_val):
            """
            ALL skills from current and previous careers -> advance to 'adv_sum' value
            :return: xp: int
            :return: boolean: Was there enough xp to fully advance in this domain?
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
                    return (skill_val - 50) // 5 * 30 + 210  # own formula
            cnt = 0

            # get all skill names
            skill_names = []
            for i in range(self.career_level, -1, -1):
                skill_names = skill_names + self.career_main.lvl[i].skills  # e.g. ['Lore (Any)', 'Track']
            # get adv_sum
            adv_sum = max([self.skills_basic[skill_name.split(' (')[0]][2] for skill_name in skill_names if skill_name.split(' (')[0] in self.skills_basic.keys()]) + 10

            # get current advance values of skills
            out_skills = {}  # {skill_name: advance_value}
            for skill_name in skill_names:
                name_short = skill_name.split(' (')[0]

                # in skill_basic?
                if name_short in self.skills_basic.keys():
                    [_, _, skill_advances, _] = self.skills_basic[name_short]  # [stat_str, stat_total, skill_advances, skill_total]
                    out_skills.update({skill_name: skill_advances})

                # in skill_advanced?
                else:
                    # try skill's full name
                    if skill_name in self.skills_advanced.keys():
                        [_, _, skill_advances, _] = self.skills_advanced[skill_name]  # [stat_str, stat_total, skill_advances, skill_total]
                        out_skills.update({skill_name: skill_advances})
                    else:
                        # skill name has '(Any one)' and there is according name in skill_advanced?
                        if skill_name.find('(Any one)') >= 0 and name_short in [name.split(' (')[0] for name in self.skills_advanced.keys()]:
                            # {skill_name: [stat_str, stat_total, skill_advances, skill_total]}
                            tmp = [(name, val) for name, [_, _, val, _] in self.skills_advanced.items() if name.find(name_short) >= 0]
                            tmp.sort()
                            final_name = tmp[-1][0]  # pick skill with the highest advance value
                            [_, _, skill_advances, _] = self.skills_advanced[final_name]
                            out_skills.update({final_name: skill_advances})

                        # skill name is new, even for skill_advanced
                        else:
                            out_skills.update({skill_name: 0})
            # parse
            out_skills = self.parse_skill_words(out_skills)
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

                if advance >= adv_sum:
                    cnt += 1

            if cnt == len(out_skills):
                return xp_val, True
            else:
                return xp_val, False

        if xp is None:
            xp = self.xp_start

        if self.career_level == 3:
            # --- Stats
            xp, f_full_advance = advance_stats(xp)
            self.update_all()
            if not f_full_advance:
                self.xp_left = xp
                return
            # ---- Skills
            xp, f_full_advance = advance_skills(xp)
            self.update_all()
            if not f_full_advance:
                self.xp_left = xp
                return

            # ---- Continue (if not returned at this point)
            self.advance_continue(xp)

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
        from functions import random_pick
        from constants import skills_all
        """
        :param in_skills:     {skill_name: advance_value}
        :return: out_skills:  {skill_name: advance_value}
        """
        # parse (Any one) -> choose one from list
        out_skills = {}
        for skill_name, advance in in_skills.items():
            new_name = ''
            if skill_name.find("(Any one)") >= 0:
                short_name = skill_name[:skill_name.find('(Any one)') - 1]
                _, _, choose_list = skills_all[short_name]
                new_name = short_name + ' (' + random_pick(choose_list) + ')'
            else:
                new_name = skill_name
            out_skills.update({new_name: advance})

        return out_skills
    def add_skills(self, in_skills):
        from constants import skills_all_basic, skills_all_advanced
        """
        :param in_skills:     {skill_name: advance_value}
        """
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
        #if len(found_total) != len(self._SkillNames): print("Not all skills were found", 'FOUND:', found_total, 'ALL:', self._SkillNames)

    @staticmethod
    def parse_talent_words(in_talents):
        from functions import random_pick, roll1d100
        from constants import talents_random, talents_all
        """
        :param in_talents:     {talent_name: advance_value}
        :return: out_talents:  {talent_name: advance_value}
        """
        out_talents = {}
        for talent_name, advance in in_talents.items():
            name = talent_name
            # sth " or " sth
            if name.find(" or ") >= 0:
                two_talents = name.split(" or ")
                name = random_pick(two_talents)  # pick one from two talents

            # Random
            if name == "Random":
                name = talents_random[roll1d100() - 1]

            # (Any one)
            if name.find("(Any one)") >= 0:
                short_name = name[:name.find('(Any one)') - 1]
                [_, _, _, choose_list] = talents_all[short_name]  # ["Bonus I", "Perception", "Perception test...", ["Vision", "Taste"]]
                name = short_name + ' (' + random_pick(choose_list) + ')'

            out_talents.update({name: advance})

        return out_talents
    def add_talents(self, in_talents):
        from constants import talents_all
        """
        :param in_talents:     {talent_name: advance_value}
        """
        for talent_name, advance in in_talents.items():
            short_name = talent_name.split(' (')[0]
            [_, test, description, _] = talents_all[
                short_name]  # ["Bonus I", "Perception", "Perception test...", ["Vision", "Taste"]]
            self.talents.update({talent_name: (test, description)})  # {talent_name: (test, description)}
    def modify_stats_by_talents(self, in_talents):
        """
        :param in_talents: {talent_name: advance_value}
        """
        # add values to base stats, if talent says so
        for talent_name in in_talents.keys():
            #{stat_name: [base, advance, total]}
            if talent_name == "Coolheaded":
                # WP+5
                [base, advance, total] = self.attributes['WP']
                self.attributes.update({'WP': [base+5, advance, total]})
            elif talent_name == "Fleetfooted":
                # MoveSpeed+1
                [base, advance, total] = self.attributes['MoveSpeed']
                self.attributes.update({'MoveSpeed': [base+1, advance, total]})
            elif talent_name == "Hardy":
                # Wounds += Toughness Bonus
                bonusT = self.attributes['WP'][2] // 10  # total value of T
                [base, advance, total] = self.attributes['Wounds']
                self.attributes.update({'Wounds': [base+bonusT, advance, total]})
            elif talent_name == "Lightning Reflexes":
                # AG+5
                [base, advance, total] = self.attributes['AG']
                self.attributes.update({'AG': [base+5, advance, total]})
            elif talent_name == "Luck":
                # max Fate+1
                [base, advance, total] = self.attributes['Fate']
                self.attributes.update({'Fate': [base+1, advance, total]})
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



    # function "present" -> obsolete, not used
    """
    def present(self):
        # update
        self.update_all()
        print(f'Name: {self.name}')
        print(f'{self.sex_str}, {self.species}, Age: {self.age}, Height: {self.height:.2f}m')
        print(f'Class: {ClassAll[self._ClassN]}, Career: {self._CareerName}, Status: {CareerSocialL1[self._CareerN]}')
        print(f'Appearance: ')
        for text in self.desc_appearance: print(f'\t {text}')
        print(f'General: {self.desc_gen_look}')
        print(f'Traits:')
        for text in self.desc_traits[0:3]: print(f'\t {text}')
        print(f'Reactions:')
        for text in self.desc_reactions: print(f'\t {text}')
        print('------------------------------------------------------------------------------')
        # {skill_name: [stat_str, stat_total, skill_advances, skill_total]}
        print(f'Skills Basic:')
        for skill_name, values_list in self.skills_basic.items(): print(f'\t{skill_name}\t{values_list}')
        print(f'Skills Advanced:')
        for skill_name, values_list in self.skills_advanced.items(): print(f'\t{skill_name}\t{values_list}')
        # {talent_name: talent's description]}
        print(f'Talents:')
        for talent_name, talent_description in self.talents.items(): print(f'\t{talent_name}\t->\t{talent_description}')
        print(f'Stats:')
        for stat_name, stat_value in self.attributes.items(): print(f'\t{stat_name}\t{stat_value}')
        print('------------------------------------------------------------------------------')
        if self._Dooming is not None:
            print(f'Dooming: {self._Dooming}')
        print(f'Trapping: {self._Trapping}')
        print(f'Money: {self._Money}')
    """



