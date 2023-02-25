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
        self.arcane = None            # [str] e.g. "Beasts"
        self.spells = {}              # {'Petty': {spell_name: SpellClass, ...},
                                      #  'Arcane': {spell_name: SpellClass, ...},
                                      #  'Beasts': {spell_name: SpellClass, ...} }  <- should match self.arcane
        self.god = None
        self.blessings = {}           # {name: PrayerClass}
        self.miracles = {}            # {name: PrayerClass}

    def get_init_values(self, **kwargs):
        from constants import age_by_species, careers_all, skills_all_basic, skills_all, talents_all, talents_random
        from functions import random_pick
        """
        set: sex, species, age, class, main career, current carrer, status, xp, basic skills
        """
        def parse_skill_names():
            pre_desc = f'NpcSingleton.get_init_values.parse_skill_names: '
            for i in range(4):
                career_obj = self.career_main.lvl[i]    # CareerClass
                out_names = []
                for skill_name in career_obj.skills:
                    if skill_name.find("(Any one)") < 0:
                        out_names.append(skill_name)
                    else:
                        # (Any one) -> choose one from list
                        short_name = skill_name[:skill_name.find('(Any one)') - 1]
                        _, _, list_of_choices = skills_all[short_name]
                        # choose one from unique list
                        names_for_skill = set([short_name + ' (' + choice_name + ')' for choice_name in list_of_choices])
                        names_previous_careers = []
                        for j in range(i):
                            names_previous_careers += self.career_main.lvl[j].skills
                        names_previous_careers = set(names_previous_careers)
                        names_current_career = set(career_obj.skills)
                        names_current = set(out_names)
                        choose_list = list(names_for_skill - names_previous_careers - names_current_career - names_current)
                        if len(choose_list) == 0:
                            error = f'{pre_desc}choose_list for skill: {skill_name} is empty!'
                            logger.error(error)
                            raise Exception(error)
                        new_name = random_pick(choose_list)
                        out_names.append(new_name)

                # check length
                if len(career_obj.skills) != len(out_names):
                    error = f'{pre_desc}Length of input ({len(career_obj.skills)}) != length of output ({len(out_names)})'
                    logger.error(error)
                    raise Exception(error)
                # check unique
                if len(set(out_names)) != len(out_names):
                    error = f'{pre_desc}Output values are not unique: {out_names}'
                    logger.error(error)
                    raise Exception(error)

                # modify values
                self.career_main.lvl[i].skills = out_names
        def parse_talent_names():
            def get_choose_list(in_lvl, in_names_for_talent):
                # choose one from unique list
                names_previous_careers = []
                for j in range(in_lvl):
                    names_previous_careers += self.career_main.lvl[j].talents
                names_previous_careers = set(names_previous_careers)
                names_current_career = set(career_obj.talents)
                names_current = set(out_names)
                choose_list = list(in_names_for_talent - names_previous_careers - names_current_career - names_current)
                if len(choose_list) == 0:
                    error = f'{pre_desc}choose_list for talent: {talent_name} is empty!'
                    logger.error(error)
                    raise Exception(error)
                return choose_list
            pre_desc = f'NpcSingleton.get_init_values.parse_talent_names: '

            for i in range(4):
                career_obj = self.career_main.lvl[i]    # CareerClass
                out_names = []
                for talent_name in career_obj.talents:
                    if talent_name.find("(Any one)") < 0 and talent_name.find(" or ") < 0 and talent_name != "Random":
                        out_names.append(talent_name)

                    elif talent_name.find("(Any one)") >= 0:
                        # (Any one) -> choose one from list
                        short_name = talent_name[:talent_name.find('(Any one)') - 1]
                        _, _, _, list_of_choices = talents_all[short_name]  # ["Bonus I", "Perception", "Perception test...", ["Vision", "Taste"]]
                        names_for_talent = set([short_name + ' (' + choice_name + ')' for choice_name in list_of_choices])
                        new_name = random_pick(get_choose_list(i, names_for_talent))    # choose one from unique list
                        out_names.append(new_name)

                    elif talent_name.find(" or ") >= 0:
                        # sth " or " sth -> pick one from two talents
                        two_talents = talent_name.split(" or ")
                        names_for_talent = set(two_talents)
                        new_name = random_pick(get_choose_list(i, names_for_talent))    # choose one from unique list
                        out_names.append(new_name)

                    else:   # talent_name == "Random"
                        names_for_talent = set(talents_random)
                        new_name = random_pick(get_choose_list(i, names_for_talent))    # choose one from unique list
                        out_names.append(new_name)

                # check length
                if len(career_obj.talents) != len(out_names):
                    error = f'{pre_desc}Length of input ({len(career_obj.talents)}) != length of output ({len(out_names)})'
                    logger.error(error)
                    raise Exception(error)
                # check unique
                if len(set(out_names)) != len(out_names):
                    error = f'{pre_desc}Output values are not unique: {out_names}'
                    logger.error(error)
                    raise Exception(error)

                # modify values
                self.career_main.lvl[i].talents = out_names
        def parse_trappings():
            from functions import rollXd10
            pre_desc = f'NpcSingleton.get_init_values.parse_trappings: '

            for i in range(4):
                career_obj = self.career_main.lvl[i]  # CareerClass
                out_text = career_obj.trappings
                indexes = [i.start() for i in re.finditer("[0-9]d10", out_text)]
                for index in indexes:
                    number = int(out_text[index:index + 1])  # Xd10
                    rolled_val = rollXd10(number)
                    out_text = out_text.replace(out_text[index:index + 4], str(rolled_val))
                # modify value
                self.career_main.lvl[i].trappings = out_text

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
        # parse words in career (skill names, talents, trappings)
        parse_skill_names()
        parse_talent_names()
        parse_trappings()
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
        #5  roll_spells (if magical)
        self.roll_spells()
        #6  roll_other_things
        self.roll_other_things()
        # update
        self.update_all()
    def roll_height(self):
        from functions import random_pick, rollXd10
        from constants import age_by_species, height_by_species
        pre_desc = f'NpcSingleton.roll_height: '

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
        else:
            error = f'{pre_desc}Unknows species: {self.species}'
            logger.error(error)
            raise Exception(error)
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

        # Noble - handle in roll_other_things()

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
        Roll 6 skills, can be the same as in career
        :return: out_skills: {skill_name: advance}
        """
        from constants import skills_by_species, skills_all
        from functions import random_pick
        def parse_skill_names(in_skill_names):
            pre_desc = f'NpcSingleton.roll_skills_species.parse_skill_names: '

            out_names = []
            for skill_name in in_skill_names:
                if skill_name.find("(Any one)") < 0:
                    out_names.append(skill_name)
                else:
                    # (Any one) -> choose one from list
                    short_name = skill_name[:skill_name.find('(Any one)') - 1]
                    _, _, list_of_choices = skills_all[short_name]
                    # choose one, different from current
                    names_for_skill = set([short_name + ' (' + choice_name + ')' for choice_name in list_of_choices])
                    names_current = set(out_names)
                    choose_list = list(names_for_skill - names_current)
                    if len(choose_list) == 0:
                        error = f'{pre_desc}choose_list for skill: {skill_name} is empty!'
                        logger.error(error)
                        raise Exception(error)
                    new_name = random_pick(choose_list)
                    out_names.append(new_name)

            # check length
            if len(in_skill_names) != len(out_names):
                error = f'{pre_desc}Length of input ({len(in_skill_names)}) != length of output ({len(out_names)})'
                logger.error(error)
                raise Exception(error)
            # check unique
            if len(set(out_names)) != len(out_names):
                error = f'{pre_desc}Output values are not unique: {out_names}'
                logger.error(error)
                raise Exception(error)

            return out_names

        # roll 6 skill names
        skill_names = [name for name in random.sample(skills_by_species[self.species], 6)]
        # parse
        skill_names = parse_skill_names(skill_names)
        # advance skills values
        skills = {}     # {skill_name: advance}
        for i, skill_name in enumerate(skill_names):
            if i < 3:
                skills.update({skill_name: 5})  # advance 3 skills by value: 5
            else:
                skills.update({skill_name: 3})  # advance 3 skills by value: 3
        # add
        self.add_skills(skills)
        # update
        self.update_skills()
    def roll_talents_species(self):
        """
        Roll 5 (or 6) talents, can be the same as in career
        :return: out_skills: {skill_name: advance}
        """
        from constants import talents_by_species, talents_all, talents_random
        from functions import random_pick
        def parse_talent_names(in_talent_names):
            pre_desc = f'NpcSingleton.roll_talents_species.parse_talent_names: '

            out_names = []
            for talent_name in in_talent_names:
                if talent_name.find("(Any one)") < 0 and talent_name.find(" or ") < 0 and talent_name != "Random":
                    out_names.append(talent_name)

                elif talent_name.find("(Any one)") >= 0:
                    # (Any one) -> choose one from list
                    short_name = talent_name[:talent_name.find('(Any one)') - 1]
                    _, _, _, list_of_choices = talents_all[short_name]  # ["Bonus I", "Perception", "Perception test...", ["Vision", "Taste"]]
                    # choose one, different from current
                    names_for_talent = set([short_name + ' (' + choice_name + ')' for choice_name in list_of_choices])
                    names_current = set(out_names)
                    choose_list = list(names_for_talent - names_current)
                    if len(choose_list) == 0:
                        error = f'{pre_desc}choose_list for talent: {talent_name} is empty!'
                        logger.error(error)
                        raise Exception(error)
                    new_name = random_pick(choose_list)
                    out_names.append(new_name)

                elif talent_name.find(" or ") >= 0:
                    # sth " or " sth -> pick one from two talents
                    two_talents = talent_name.split(" or ")
                    # choose one, different from current
                    names_for_talent = set(two_talents)
                    names_current = set(out_names)
                    choose_list = list(names_for_talent - names_current)
                    if len(choose_list) == 0:
                        error = f'{pre_desc}choose_list for talent: {talent_name} is empty!'
                        logger.error(error)
                        raise Exception(error)
                    new_name = random_pick(choose_list)
                    out_names.append(new_name)

                else:   # talent_name == "Random"
                    # choose one, different from current
                    names_for_talent = set(talents_random)
                    names_current = set(out_names)
                    choose_list = list(names_for_talent - names_current)
                    if len(choose_list) == 0:
                        error = f'{pre_desc}choose_list for talent: {talent_name} is empty!'
                        logger.error(error)
                        raise Exception(error)
                    new_name = random_pick(choose_list)
                    out_names.append(new_name)

            # check length
            if len(in_talent_names) != len(out_names):
                error = f'{pre_desc}Length of input ({len(in_talent_names)}) != length of output ({len(out_names)})'
                logger.error(error)
                raise Exception(error)
            # check unique
            if len(set(out_names)) != len(out_names):
                error = f'{pre_desc}Output values are not unique: {out_names}'
                logger.error(error)
                raise Exception(error)

            return out_names

        # roll talent names
        talent_names = talents_by_species[self.species]
        # parse
        talent_names = parse_talent_names(talent_names)
        # advance talents values
        talents = {name: 1 for name in talent_names}
        ok, reason = self.can_add_talents(talents)
        if ok:
            # modify stats
            self.modify_stats_for_new_talents(talents)  # all talents are new and have advance == 1
            # add
            self.add_talents(talents)
        else:
            logger.error(reason)
            raise Exception(reason)
    def set_skills_career(self):
        """
        Add and advance 8 skills from career
        Note: names are already parsed in get_init_values()
        """
        from functions import random_pick
        # add 8 skills from career
        skill_names = self.career_current.skills
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
        skills = {}
        for i, skill_name in enumerate(skill_names):
            skills.update({skill_name: out_values[i]})
        # add
        self.add_skills(skills)
        # update
        self.update_skills()
    def set_talents_career(self):
        """
        Add all talents from career
        Advance (by 1) only one, randomly picked talent, the rest of talents will have 0 advances
        Note: names are already parsed in get_init_values()
        """
        # get all talents from career
        talents = {name: 0 for name in self.career_current.talents}  # {talent_name: advance_value}
        # advance (by 1) only one talent
        for talent_name in talents.keys():
            ok, reason = self.can_add_talents({talent_name: 1})
            if ok:
                talents[talent_name] = 1
                # modify stats?
                if talent_name not in self.talents.keys():
                    self.modify_stats_for_new_talents({talent_name: 1})  # talent is new and has advance == 1
                break
        # the rest of talents will have 0 advances
        self.add_talents(talents)
    def roll_spells(self):
        from spells import spells_petty
        # check if 'Petty Magic' is available
        if 'Petty Magic' in self.talents.keys():
            # add a number of spells equal to npc's Willpower Bonus
            bWP = self.attributes['WP'][2] // 10
            out_dict = {}
            for spell_name in random.sample(spells_petty.keys(), bWP):
                out_dict.update({spell_name: spells_petty[spell_name]})
            self.spells.update({'Petty': out_dict})

            # check if 'Arcane Magic' is available
            for talent_name in self.talents.keys():
                if talent_name.find('Arcane Magic') >= 0:
                    # set values
                    idx_start = talent_name.find('(')
                    idx_end = talent_name[idx_start+1:].find(')')
                    arcane_str = talent_name[idx_start+1: idx_end]
                    self.arcane = arcane_str
                    self.spells.update({'Arcane': {}})
                    self.spells.update({self.arcane: {}})
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
        # trappings (for career - already parsed)
        self.trapping = self.parse_trappings(trappings_by_class[self.ch_class]) + ", " + self.career_current.trappings

        # money
        self.money = self.roll_money(self.career_current.status)
    @staticmethod
    def parse_trappings(in_string):
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
        #   sum of career attributes == 5 (self.advance_stats)
        if sum([self.attributes[stat_name][1] for stat_name in self.career_current.advances]) != 5:
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
        #   for Halfling, Gnome: exactly 7 talents with advance points == 1 (self.roll_talents_species=6, set_talents_career=1)
        if self.species in ["Halfling", "Gnome"]:
            if sum_advances != 7:
                error = f'{pre_desc}Talents - number of advanced talents !=7'
                logger.error(error)
                raise Exception(error)
        #   for rest species: exactly 6 talents with advance points == 1 (self.roll_talents_species=5, set_talents_career=1)
        else:
            if sum_advances != 6:
                error = f'{pre_desc}Talents - number of advanced talents !=6'
                logger.error(error)
                raise Exception(error)

        # SPELLS
        if 'Petty Magic' in self.talents.keys():
            if 'Petty' not in self.spells.keys():
                error = f'{pre_desc}Spells - petty spells not set.'
                logger.error(error)
                raise Exception(error)
            elif len(self.spells['Petty']) == 0:
                error = f'{pre_desc}Spells - petty spells not set.'
                logger.error(error)
                raise Exception(error)
            # Arcane Magic
            for talent_name in self.talents.keys():
                if talent_name.find('Arcane Magic') >= 0:
                    if self.arcane is None:
                        error = f'{pre_desc}Spells - arcane not set.'
                        logger.error(error)
                        raise Exception(error)

    def advance_by_xp(self, xp_0=None):
        """
        Advance from career lvl 0 to lvl 3
        :return: reason:    <str>
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
            talents = {}    # {talent_name: advance}
            for talent_name in self.career_current.talents:
                talents.update({talent_name: self.talents[talent_name][1]})  # {talent_name: (talent_test, talent_advance, talent_description)}

            # try to advance each talent to maximal value (defined in constants.all_talents)
            for talent_name, talent_advance in talents.items():
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
                        # modify stats?
                        if val == 1:
                            if talent_name in self.talents.keys():
                                if self.talents[talent_name][1] == 0:
                                    # talent was added with advance == 0, but now it has advance == 1
                                    self.modify_stats_for_new_talents({talent_name: val})
                            else:
                                # talent in new and has advance == 1
                                self.modify_stats_for_new_talents({talent_name: val})
                        # add to previous value!
                        self.add_talents({talent_name: 1})
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

            # return advance not completed
            if len(reason) > 0:
                return xp_val, False, reason
            if cnt != len(talents):
                reason = f'Number of fully advanced talents: {cnt} != {len(talents)}'
                return xp_val, False, reason
            # return advance fully completed
            return xp_val, True, reason
        def advance_spells(xp_val):
            """
            Advance spells for current career
            :return: xp: int
            :return: boolean: Was there enough xp to fully advance in this domain?
            :return: reason
            """
            pre_desc = f'NpcSingleton.advance_by_xp.advance_spells: '
            reason = ''
            from spells import spells_petty, spells_arcane, spells_lore_all
            def get_advance_plan():
                # calculate how many advances in each group to make
                num_petty_spells = len(self.spells['Petty'])       # shall be set at: roll_spells()
                try:
                    num_arcane_spells = len(self.spells['Arcane'])
                except KeyError:
                    num_arcane_spells = 0
                try:
                    num_lore_spells = len(self.spells[self.arcane])
                except KeyError:
                    num_lore_spells = 0

                if self.career_level == 0:
                    # 'Petty': 3
                    val_p = 3-num_petty_spells if num_petty_spells <= 3 else 0
                    val_a = 0
                    val_l = 0
                elif self.career_level == 1:
                    # 'Petty': 4, 'Arcane': 2, 'Lore': 1
                    val_p = 4-num_petty_spells   if num_petty_spells <= 4 else 0
                    val_a = 2-num_arcane_spells if num_arcane_spells <= 2 else 0
                    val_l = 1-num_lore_spells     if num_lore_spells <= 1 else 0
                elif self.career_level == 2:
                    # 'Petty': 5, 'Arcane': 3, 'Lore': 3
                    val_p = 5-num_petty_spells   if num_petty_spells <= 5 else 0
                    val_a = 3-num_arcane_spells if num_arcane_spells <= 3 else 0
                    val_l = 3-num_lore_spells     if num_lore_spells <= 3 else 0
                else:   # lvl3
                    # 'Petty': 5, 'Arcane': 4, 'Lore': 6
                    val_p = 5-num_petty_spells   if num_petty_spells <= 5 else 0
                    val_a = 4-num_arcane_spells if num_arcane_spells <= 4 else 0
                    val_l = 6-num_lore_spells     if num_lore_spells <= 6 else 0
                return {'Petty': val_p, 'Arcane': val_a, 'Lore': val_l}
            def get_cost(spell_group):
                bWP = self.attributes['WP'][2]//10  # Willpower Bonus
                if spell_group == 'Petty':
                    num_known_spells = len(self.spells['Petty'])
                    if num_known_spells <= bWP: return 50
                    elif bWP < num_known_spells <= bWP*2: return 100
                    elif bWP*2 < num_known_spells <= bWP*3: return 150
                    elif bWP*3 < num_known_spells <= bWP*4: return 200
                else:   # 'Arcane' or Lore magic
                    num_known_spells = len(self.spells['Arcane']) + len(self.spells[self.arcane])
                    if num_known_spells <= bWP: return 100
                    elif bWP < num_known_spells <= bWP*2: return 200
                    elif bWP*2 < num_known_spells <= bWP*3: return 300
                    elif bWP*3 < num_known_spells <= bWP*4: return 400
                    elif bWP*4 < num_known_spells <= bWP*5: return 500
                    elif bWP*5 < num_known_spells <= bWP*6: return 600
                    elif bWP*6 < num_known_spells <= bWP*7: return 700

            # special workaround to get Arcane and Lore spells earlier
            # if available, advance talent 'Arcane Magic' from 0 to 1 and have access to spells
            if self.arcane is None:
                for talent_name in self.talents.keys():
                    if talent_name.find('Arcane Magic') >= 0:
                        if self.talents[talent_name][1] == 0:  # {talent_name: (talent_test, talent_advance, talent_description)}
                            if xp_val >= 100:
                                xp_val -= 100
                                # modify stats
                                self.modify_stats_for_new_talents({talent_name: 1})
                                # add to previous value!
                                self.add_talents({talent_name: 1})
                                break
                            else:
                                reason = f'To upgrade talent:{talent_name} to lvl: {1}/{1} cost>xp: {100}>{xp_val}'
                                break


            # check if 'Petty Magic' is available
            if 'Petty' in self.spells.keys():
                advance_plan = get_advance_plan()
                spell_names = set(spells_petty.keys())-set(self.spells['Petty'].keys())     # get unique spell names
                for spell_name in random.sample(spell_names, advance_plan['Petty']):
                    cost = get_cost('Petty')
                    if xp_val >= cost:
                        xp_val -= cost
                        self.spells['Petty'].update({spell_name: spells_petty[spell_name]})
                    else:
                        reason = f'To advance spell:{spell_name} cost>xp: {cost}>{xp_val}'
                        break
            if len(reason) > 0:
                return xp_val, False, reason

            # check if arcane is available
            if self.arcane is not None:
                advance_plan = get_advance_plan()
                # ARCANE
                spell_names = set(spells_arcane.keys()) - set(self.spells['Arcane'].keys())
                for spell_name in random.sample(spell_names, advance_plan['Arcane']):
                    cost = get_cost('Arcane')
                    if xp_val >= cost:
                        xp_val -= cost
                        self.spells['Arcane'].update({spell_name: spells_arcane[spell_name]})
                    else:
                        reason = f'To advance spell:{spell_name} cost>xp: {cost}>{xp_val}'
                        break
                # LORE
                spells_lore = spells_lore_all[self.arcane]
                spell_names = set(spells_lore.keys()) - set(self.spells[self.arcane].keys())
                for spell_name in random.sample(spell_names, advance_plan['Lore']):
                    cost = get_cost('Lore')
                    if xp_val >= cost:
                        xp_val -= cost
                        self.spells[self.arcane].update({spell_name: spells_lore[spell_name]})
                    else:
                        reason = f'To advance spell:{spell_name} cost>xp: {cost}>{xp_val}'
                        break
            if len(reason) > 0:
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
            8 skills from current and previous levels of career -> advance to 'adv_sum' value
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

            # get skill names from current and previous levels of career
            all_skill_names = []
            for i in range(self.career_level+1):
                all_skill_names = all_skill_names + self.career_main.lvl[i].skills
            # pick 8 randomly, without repetitions
            skill_names = random.sample(all_skill_names, 8)
            # get current advance values of skills
            skills = {}   # {skill_name: advance_value}
            for skill_name in skill_names:
                name_short = skill_name.split(' (')[0]
                # in skill_basic?
                if name_short in self.skills_basic.keys():
                    [_, _, skill_advances, _] = self.skills_basic[name_short]  # [stat_str, stat_total, skill_advances, skill_total]
                    skills.update({skill_name: skill_advances})
                # in skill_advanced
                else:
                    [_, _, skill_advances, _] = self.skills_advanced[skill_name]  # [stat_str, stat_total, skill_advances, skill_total]
                    skills.update({skill_name: skill_advances})

            # advance
            adv_sum = (self.career_level + 1) * 5
            for skill_name in skills.keys():
                advance = skills[skill_name]
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
        def advance_next_level(xp_val):
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
            # new career lvl
            self.career_level += 1
            self.career_current = self.career_main.lvl[self.career_level]
            # new status
            self.status = self.career_current.status
            # new skills
            skills = {name: 0 for name in self.career_current.skills}
            self.add_skills(skills)
            self.update_skills()
            # new talents
            talents = {name: 0 for name in self.career_current.talents}
            self.add_talents(talents)
            # new trappings
            self.trapping = self.trapping + ", " + self.career_current.trappings   # already parsed
            # new money
            self.money = self.money + ', ' + self.roll_money(self.career_current.status)

            return xp_val, True, f''

        if xp_0 is None:
            xp_0 = self.xp_start

        reason = ''
        if 0 <= self.career_level <= 3:
            logger.debug(f'\t- Career lvl {self.career_level+1}')
            # ---- Spells
            xp_1, f_1, reason_1 = advance_spells(xp_0)
            self.update_all()
            logger.debug(f'\t\tspells, xp_spent={xp_0 - xp_1}')
            if not f_1:
                self.xp_left = xp_1
                logger.debug(f'\t\t\tstopped! reason={reason_1}, xp_left={self.xp_left}')
                return reason_1
            # ---- Talents
            xp_2, f_2, reason_2 = advance_talents(xp_1)
            self.update_all()
            logger.debug(f'\t\ttalents, xp_spent={xp_1-xp_2}')
            if not f_2:
                self.xp_left = xp_2
                logger.debug(f'\t\t\tstopped! reason={reason_2}, xp_left={self.xp_left}')
                return reason_2
            # --- Stats
            xp_3, f_3, reason_3 = advance_stats(xp_2)
            self.update_all()
            logger.debug(f'\t\tstats, xp_spent={xp_2-xp_3}')
            if not f_3:
                self.xp_left = xp_3
                logger.debug(f'\t\t\tstopped! reason={reason_3}, xp_left={self.xp_left}')
                return reason_3
            # ---- Skills
            xp_4, f_4, reason_4 = advance_skills(xp_3)
            self.update_all()
            logger.debug(f'\t\tskills, xp_spent={xp_3-xp_4}')
            if not f_4:
                self.xp_left = xp_4
                logger.debug(f'\t\t\tstopped! reason={reason_4}, xp_left={self.xp_left}')
                return reason_4
            # ---- Advance to next level?
            xp_5, f_5, reason_5 = advance_next_level(xp_4)
            self.update_all()
            if f_5:
                logger.debug(f'\t\tadvance to next level, xp_spent={xp_0-xp_5}, xp_left={xp_5}')
                reason = self.advance_by_xp(xp_5)  # repeat the function
            else:
                self.xp_left = xp_5
                logger.debug(f'\t\t\tstopped! reason={reason_5}, xp_left={self.xp_left}')
                return reason_5

        return reason
    def advance_continue(self, xp_0):
        """
        Continue advancing, after reaching career lvl 3
        :return: reason:    <str>
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

            # SKILLS - for all that are >=0: max_value + 10
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
        reason = ''

        if len(plan['talents']) > 0:
            # ---- Talents
            xp_1, f_1, reason_1 = advance_talents(xp_0)
            self.update_all()
            logger.debug(f'\t\ttalents, xp_spent={xp_0-xp_1}')
            if not f_1:
                self.xp_left = xp_1
                logger.debug(f'\t\t\tstopped! reason={reason_1}, xp_left={self.xp_left}')
                return reason_1
        else:
            xp_1 = xp_0

        # --- Stats
        xp_2, f_2, reason_2 = advance_stats(xp_1)
        self.update_all()
        logger.debug(f'\t\tstats, xp_spent={xp_1-xp_2}')
        if not f_2:
            self.xp_left = xp_2
            logger.debug(f'\t\t\tstopped! reason={reason_2}, xp_left={self.xp_left}')
            return reason_2

        # ---- Skills
        xp_3, f_3, reason_3 = advance_skills(xp_2)
        self.update_all()
        logger.debug(f'\t\tskills, xp_spent={xp_2-xp_3}')
        if not f_3:
            self.xp_left = xp_3
            logger.debug(f'\t\t\tstopped! reason={reason_3}, xp_left={self.xp_left}')
            return reason_3

        # ---- Continue (if not returned at this point)
        self.advance_continue(xp_3)

        return reason

    def update_attributes(self):
        # stats - calculate all total values
        for stat_name in self.attributes.keys():
            [base, advance, total] = self.attributes[stat_name]   # {stat_name: [base, advance, total]}
            total = base + advance
            self.attributes.update({stat_name: [base, advance, total]})
        #   - special for "Fate", "Fortune", "Resilience", "Resolve"
        if self.attributes["Fate"][2] > self.attributes["Fortune"][2]:
            self.attributes["Fortune"] = self.attributes["Fate"]
        if self.attributes["Resilience"][2] > self.attributes["Resolve"][2]:
            self.attributes["Resolve"] = self.attributes["Resilience"]

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
    def can_add_talents(self, in_talents):
        """
        :param in_talents:              {talent_name: advance}
        :return f_success, reason       boolean, str
        """
        from constants import talents_all
        pre_desc = f'NpcSingleton.can_add_talents: '
        f_success = True
        reason = ''

        # check if input is unique
        if len(set(in_talents.keys())) != len(in_talents.keys()):
            f_success = False
            reason = f'{pre_desc}Input names are not unique: {in_talents.keys()})'
            return f_success, reason

        for talent_name, advance in in_talents.items():
            # talent already exists
            if talent_name in self.talents.keys():
                test, current_advance, description = self.talents[talent_name]
                limit, test, description, _ = talents_all[talent_name] # ["Bonus I", "Perception", "Perception test...", ["Vision", "Taste"]]
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

                # reached max value?
                if current_advance + advance > max_advance:
                    f_success = False
                    reason = f'{pre_desc}Maximal advance already reached: {current_advance}/{max_advance})'
                    return f_success, reason

        # no problems
        return f_success, reason
    def add_talents(self, in_talents):
        """
        :param in_talents:     {talent_name: advance}
        Note: only unique names allowed!
        Note: if talent name already exists -> increase advance value
        """
        from constants import talents_all
        pre_desc = f'NpcSingleton.add_talents: '

        # check if input unique
        if len(set(in_talents.keys())) != len(in_talents.keys()):
            error = f'{pre_desc}Input names are not unique: {in_talents.keys()})'
            logger.error(error)
            raise Exception(error)

        for talent_name, advance in in_talents.items():
            # talent already exists? -> increase advance value
            if talent_name in self.talents.keys():
                test, current_advance, description = self.talents[talent_name]
                current_advance += advance
                self.talents.update({talent_name: (test, current_advance, description)})
            # create new entry
            else:
                short_name = talent_name.split(' (')[0]
                [_, test, description, _] = talents_all[short_name]  # ["Bonus I", "Perception", "Perception test...", ["Vision", "Taste"]]
                self.talents.update({talent_name: (test, advance, description)})
    def modify_stats_for_new_talents(self, in_talents):
        """
        :param in_talents: {talent_name: advance_value}
        Note: stats will be updated every time! No restrictions!
        """
        for talent_name, talent_advance in in_talents.items():
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
                self.attributes.update({'WS': [base+5, advance, total]})
            elif talent_name.find('Arcane Magic') >= 0:
                # fill self.arcane and self.spells
                arcane_str = talent_name[talent_name.find('(') + 1: talent_name.find(')')]
                self.arcane = arcane_str
                self.spells.update({'Arcane': {}})
                self.spells.update({self.arcane: {}})

        # update attributes
        self.update_attributes()
    def parse_spells(self, in_spells):
        """
        :param in_spells:     {spell_name: SpellClass, ...}
        :return: out_spells:  {spell_name: SpellClass, ...}
        """
        from spells import SpellClass
        pre_desc = f'NpcSingleton.parse_spells: '

        # {stat_name: [base, advance, total]}
        stat_values = {
            "WS": self.attributes['WS'][2],
            "BS": self.attributes['BS'][2],
            "S": self.attributes['S'][2],
            "T": self.attributes['T'][2],
            "AG": self.attributes['AG'][2],
            "I": self.attributes['I'][2],
            "DEX": self.attributes['DEX'][2],
            "INT": self.attributes['INT'][2],
            "WP": self.attributes['WP'][2],
            "FEL": self.attributes['FEL'][2],

            "bWS":  self.attributes['WS'][2]//10,
            "bBS":  self.attributes['BS'][2]//10,
            "bS":   self.attributes['S'][2]//10,
            "bT":   self.attributes['T'][2]//10,
            "bAG":  self.attributes['AG'][2]//10,
            "bI":   self.attributes['I'][2]//10,
            "bDEX": self.attributes['DEX'][2]//10,
            "bINT": self.attributes['INT'][2]//10,
            "bWP":  self.attributes['WP'][2]//10,
            "bFEL": self.attributes['FEL'][2]//10
        }

        out_spells = {}     # {spell_name: SpellClass, ...}
        for spell_name, spell_obj in in_spells.items():
            out_values = []     # [cn, _range, target, duration, description]
            for val_str in [spell_obj.cn, spell_obj._range, spell_obj.target, spell_obj.duration, spell_obj.description]:
                # separate to words
                splits = val_str.split(' ')
                out_splits = []
                for split in splits:
                    idx_start = split.find('[')
                    idx_end = split.find(']')
                    # extract wanted string from word
                    if idx_start >= 0 and idx_end >=0 and idx_start < idx_end:
                        inner_str = split[idx_start+1: idx_end]
                        attribute_or_bonus_str = [val for val in re.findall('[a-z,A-Z]*', inner_str) if len(val) > 0][0]
                        # e.g. [WP], [bWP]
                        try:
                            dec_value = stat_values[attribute_or_bonus_str]
                        except KeyError:
                            error = f'{pre_desc}Found string:"{attribute_or_bonus_str}" does not include information about npc attibute or it\'s bonus.'
                            logger.error(error)
                            raise Exception(error)
                        # e.g. [bWP+2]
                        if len(re.findall('\+[0-9]',inner_str)) > 0:
                            dec_value += int(re.findall('[0-9]', inner_str)[0])
                        # parse
                        out_splits.append(split[:idx_start] + str(dec_value) + split[idx_end+1:])
                    else:
                        out_splits.append(split)
                out_values.append(' '.join(out_splits))
            # add
            out_spells.update({spell_name: SpellClass(out_values[0], out_values[1], out_values[2], out_values[3], out_values[4])})

        return out_spells
    def parse_prayers(self, in_prayers):
        """
        :param   in_prayers:     {spell_name: PrayerClass, ...}
        :return: out_prayers:    {spell_name: PrayerClass, ...}
        """
        from prayers import PrayerClass
        pre_desc = f'NpcSingleton.parse_prayers: '

        # {stat_name: [base, advance, total]}
        stat_values = {
            "WS": self.attributes['WS'][2],
            "BS": self.attributes['BS'][2],
            "S": self.attributes['S'][2],
            "T": self.attributes['T'][2],
            "AG": self.attributes['AG'][2],
            "I": self.attributes['I'][2],
            "DEX": self.attributes['DEX'][2],
            "INT": self.attributes['INT'][2],
            "WP": self.attributes['WP'][2],
            "FEL": self.attributes['FEL'][2],

            "bWS":  self.attributes['WS'][2]//10,
            "bBS":  self.attributes['BS'][2]//10,
            "bS":   self.attributes['S'][2]//10,
            "bT":   self.attributes['T'][2]//10,
            "bAG":  self.attributes['AG'][2]//10,
            "bI":   self.attributes['I'][2]//10,
            "bDEX": self.attributes['DEX'][2]//10,
            "bINT": self.attributes['INT'][2]//10,
            "bWP":  self.attributes['WP'][2]//10,
            "bFEL": self.attributes['FEL'][2]//10
        }

        out_prayers = {}     # {name: PrayerClass, ...}
        for prayer_name, prayer_obj in in_prayers.items():
            out_values = []     # [_range, target, duration, description]
            for val_str in [prayer_obj._range, prayer_obj.target, prayer_obj.duration, prayer_obj.description]:
                # separate to words
                splits = val_str.split(' ')
                out_splits = []
                for split in splits:
                    idx_start = split.find('[')
                    idx_end = split.find(']')
                    # extract wanted string from word
                    if idx_start >= 0 and idx_end >=0 and idx_start < idx_end:
                        inner_str = split[idx_start+1: idx_end]
                        attribute_or_bonus_str = [val for val in re.findall('[a-z,A-Z]*', inner_str) if len(val) > 0][0]
                        # e.g. [WP], [bWP]
                        try:
                            dec_value = stat_values[attribute_or_bonus_str]
                        except KeyError:
                            error = f'{pre_desc}Found string:"{attribute_or_bonus_str}" does not include information about npc attibute or it\'s bonus.'
                            logger.error(error)
                            raise Exception(error)
                        # e.g. [bWP+2]
                        if len(re.findall('\+[0-9]',inner_str)) > 0:
                            dec_value += int(re.findall('[0-9]', inner_str)[0])
                        # parse
                        out_splits.append(split[:idx_start] + str(dec_value) + split[idx_end+1:])
                    else:
                        out_splits.append(split)
                out_values.append(' '.join(out_splits))
            # add
            out_prayers.update({prayer_name: PrayerClass(out_values[0], out_values[1], out_values[2], out_values[3])})

        return out_prayers

    def final_modifications(self):
        from constants import skills_all
        from functions import random_pick
        from prayers import blessings_by_god, miracles_by_god
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
                self.add_skills({"Trade (Artist)": 1})

            # Craftsman: Add Trade (Any one) to any career
            elif talent_name == "Craftsman":
                # parse
                skill_name = "Trade (Any one)"
                short_name = skill_name[:skill_name.find('(Any one)') - 1]
                # choose one
                _, _, list_of_choices = skills_all[short_name]
                new_name = random_pick(list(set([short_name + ' (' + choice_name + ')' for choice_name in list_of_choices])))
                self.add_skills({new_name: 1})

            # Perfect Pitch: Add Performer (Sing) to any career
            elif talent_name == "Perfect Pitch":
                self.add_skills({"Entertain (Sing)": 1})

            # Seasoned Traveller: Add Lore (Local) to any career
            elif talent_name == "Seasoned Traveller":
                self.add_skills({"Lore (Local)": 1})

            # Witch!:   Add Language (Magick) to any career
            elif talent_name == "Witch!":
                self.add_skills({"Language (Magick)": 1})

            # Bless:   Add god, blessings
            elif talent_name.find("Bless") >= 0:
                self.god = talent_name[talent_name.index('(')+1: talent_name.index(')')]
                self.blessings = blessings_by_god[self.god]

            # Invoke:   Add god, miracles
            elif talent_name.find("Invoke") >= 0:
                if self.god is None:
                    self.god = talent_name[talent_name.index('(')+1: talent_name.index(')')]
                self.miracles = miracles_by_god[self.god]

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
                    error = f'{pre_desc}Talent description includes not handled "[lvl]" string -> {talent_description}'
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

        # Parse spells to include attributes values
        if 'Petty' in self.spells.keys():
            self.spells['Petty'] = self.parse_spells(self.spells['Petty'])
        if 'Arcane' in self.spells.keys():
            self.spells['Arcane'] = self.parse_spells(self.spells['Arcane'])
        if self.arcane is not None:
            self.spells[self.arcane] = self.parse_spells(self.spells[self.arcane])

        # Parse prayers to include attributes values
        if self.blessings is not None:
            self.blessings = self.parse_prayers(self.blessings)
        if self.miracles is not None:
            self.miracles = self.parse_prayers(self.miracles)

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



