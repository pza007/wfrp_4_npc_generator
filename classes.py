import re
import math
from constants import *
from functions import *


class NpcSingleton(object):
    def __new__(cls):
        """ creates a singleton object, if it is not created, or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(NpcSingleton, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.sex = None               # [int] 0 or 1 (Male or Female)
        self.sex_str = None           # [str] 'Male' or 'Female'
        self.species = None           # [str] "Human", "Dwarf", "Halfling", "High Elf", "Wood Elf", "Gnome"
        self.age = None               # [int] in years
        self.height = None            # [float] in meters
        self.name = None              # [str] Name and Surname
        self.desc_gen_look = None     # [str]
        self.desc_traits = None       # [list of str]
        self.desc_reactions = None    # [list of str]
        self.desc_appearance = None   # [list of str]
        self.ch_class = None          # [str]
        self.career = None            # [str]
        self.career_level = None      # [int]
        self.status = None            # [str]
        self.trapping = None          # [str]
        self.money = None             # [str]
        self.dooming = None           # [str]
        self.xp_start = None          # [int]
        self.xp_left = None           # [int]
        self.attributes = {           # {stat_name: [basic, advance, total]}
            "WS": [0, 0, 0], "BS": [0, 0, 0], "S": [0, 0, 0], "T": [0, 0, 0], "AG": [0, 0, 0],
            "I": [0, 0, 0], "DEX": [0, 0, 0], "INT": [0, 0, 0], "WP": [0, 0, 0], "FEL": [0, 0, 0],
            "Wounds": [0, 0, 0], "MoveSpeed": [0, 0, 0], "Fate": [0, 0, 0], "Resilience": [0, 0, 0]}
        self.skills_basic = {}        # {skill_name: [stat_str, stat_total, skill_advances, skill_total]}
        self.skills_advanced = {}     # {skill_name: [stat_str, stat_total, skill_advances, skill_total]}
        self.talents = {}             # {talent_name: (test, description)}

        # INTERNAL variables
        self._SpeciesN = None         # int
        self._NamesSpecies = None     # [list of str]
        self._SurnamesSpecies = None  # [list of str]
        self._SkillNames = None       # [list of str]
        self._SkillValues = None      # [list of int]
        self._TalentNames = None      # [list of str]
        self._TalentValues = None     # [list of int]
        self._CareerSpecies = None    # [list of str]
        self._CareerN = None          # int
        self._CareerName = None       # str
        self._ClassN = None           # int
        # ["WS","BS","S","T","AG","I","DEX","INT","WP","FEL"]
        self._StatsBase =    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # from class
        self._StatsAdvance = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  #
        self._StatsTotal =   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # = _StatsBase + _StatsAdvance
        # ["W", "M", "Fate", "Resilience", "Extra"]
        self._StatsOther =   [0, 0, 0, 0, 0, 0]
        self._Dooming = None          # str
        self._Trapping = None         # [list of str]
        self._Money = None            # str

        self.get_init_values()

    def get_init_values(self):
        with open('config.txt', 'r') as f:
            for line in f.readlines():
                if not line.startswith('#') and len(line) > 2:
                    splits = line.split(' = ')
                    splits = [text.strip() for text in splits]

                    if splits[0] == 'sex':
                        if splits[1] != 'Any':
                            if splits[1] == 'Male':
                                self.sex_str = 'Male'
                                self.sex = 0
                            else:
                                self.sex_str = 'Female'
                                self.sex = 1

                    elif splits[0] == 'species':
                        if splits[1] != 'Any':
                            self._SpeciesN = SpeciesAll.index(splits[1]) + 1
                            self.species = splits[1]

                    elif splits[0] == 'age':
                        if splits[1] != 'Any':
                            # roll species if needed
                            if self.species is None:
                                self.roll_species()
                            # roll age in boundaries
                            age_range = AgeAll[self._SpeciesN - 1]
                            if splits[1] == 'Young':
                                low =  age_range[0]
                                high = age_range[0]+abs(age_range[1]-age_range[0])//4
                                self.age = random.randint(low, high)
                            elif splits[1] == 'Middle':
                                low =  age_range[1]-abs(age_range[2]-age_range[1])//4
                                high = age_range[1]+abs(age_range[2]-age_range[1])//4
                                self.age = random.randint(low, high)
                            elif splits[1] == 'Old':
                                low =  age_range[2]-abs(age_range[2]-age_range[1])//5
                                high = age_range[2]+abs(age_range[2]-age_range[1])//5
                                self.age = random.randint(low, high)

                    elif splits[0] == 'class':
                        if splits[1] != 'Any':
                            self._ClassN = ClassAll.index(splits[1])
                            self.ch_class = ClassAll[self._ClassN]

                    elif splits[0] == 'career':
                        if splits[1] != 'Any':
                            # roll species if needed
                            if self.species is None:
                                self.roll_species()
                            self._CareerSpecies = CareerSpeciesAll[self._SpeciesN - 1]

                            self._CareerN = CareerL2.index(splits[1])
                            # must fit species
                            if self._CareerSpecies[self._CareerN] < 0:
                                raise Exception(f'Career: {splits[1]} not available for species: {self.species}')
                            # must fit class
                            if self._ClassN is not None:
                                if self._CareerN < ClassCareer[self._ClassN][0] or self._CareerN > ClassCareer[self._ClassN][1]:    # [min CareerN, max CareerN]
                                    raise Exception(f'Career: {splits[1]} not available for class: {self.ch_class}')

                            # map career to lvl 1
                            self._CareerName = CareerL1[self._CareerN]
                            self.career = self._CareerName
                            self.career_level = 1
                            self.status = CareerSocialL1[self._CareerN]

                    elif splits[0] == 'xp':
                        if splits[1] != 'Any':
                            self.xp_start = int(splits[1])
                            self.xp_left = self.xp_start

    def roll_npc(self):
        #0  roll description
        if self.sex is None: self.roll_sex()
        if self.species is None: self.roll_species()
        if self.age is None: self.roll_age()
        self.roll_height()
        self.roll_name()
        self.roll_description()
        #1  roll class, career
        if self.ch_class is None: self.roll_class()
        if self.career is None: self.roll_career()  # TODO: for now -> just one career
        #2  roll attributes
        self.roll_attributes()
        #3  advance stats
        self.advance_stats()
        #4  roll skills and talents by species
        self.roll_skills_species()
        self.roll_talents_species()
        #5  set skills and talents by career
        self.set_skills_career()
        self.set_talents_career()
        #6  modify base stats by talents
        self.modify_stats_by_talents()
        #7  roll_other_things
        self.roll_other_things()
        # update
        self.update_all()

    def roll_sex(self):
        self.sex = random.randint(0, 1)
        if self.sex == 0:
            self.sex_str = 'Male'
        else:
            self.sex_str = 'Female'
    def roll_species(self):
        SpeciesRoll = roll1d100()
        if SpeciesRoll <= 89:
            self._SpeciesN = 1
        elif SpeciesRoll <= 90:
            self._SpeciesN = 6
        elif SpeciesRoll <= 95:
            self._SpeciesN = 2
        elif SpeciesRoll <= 98:
            self._SpeciesN = 3
        elif SpeciesRoll <= 99:
            self._SpeciesN = 4
        else:
            self._SpeciesN = 5
        self.species = SpeciesAll[self._SpeciesN - 1]
    def roll_age(self):
        # range e.g.: [6,  70//2,  70 ]
        age_range = AgeAll[self._SpeciesN - 1]
        self.age = random.randint(age_range[0], age_range[2])
    def roll_height(self):
        # consider age
        age_range = AgeAll[self._SpeciesN - 1]
        value_range = [0.6, 1, 0.8]
        factor = 1
        if   self.age == age_range[0]:
            factor = value_range[0]
        elif age_range[0] < self.age <age_range[1]:
            factor = value_range[0] + (abs(self.age-age_range[0])*abs(value_range[1]-value_range[0])) / (age_range[1]-age_range[0])
        elif self.age == age_range[1]:
            factor = value_range[1]
        elif age_range[1] < self.age <age_range[2]:
            factor = value_range[1] - (abs(self.age-age_range[1])*abs(value_range[2]-value_range[1])) / (age_range[2]-age_range[1])
        elif self.age == age_range[2]:
            factor = value_range[2]
        # roll height
        if self.species == "Human":
            self.height = factor*(1.5 + rollXd10(4)/100)
        elif self.species == "Dwarf":
            self.height = factor*(1.3 + rollXd10(2)/100)
        elif self.species == "Halfling":
            self.height = factor*(0.95 + rollXd10(2)/100)
        elif self.species == "High Elf":
            self.height = factor*(1.8 + rollXd10(3)/100)
        elif self.species == "Wood Elf":
            self.height = factor*(1.7 + rollXd10(3)/100)
        elif self.species == "Gnome":
            self.height = factor*(1.0 + rollXd10(3)/100)
    def roll_name(self):
        """
        :return: [str] name and surname (by species and sex)
        """
        self._NamesSpecies = NamesAll[self.sex][self._SpeciesN - 1]
        # Dwarves could get Icelandic style surnames, but from either 66% MAle 33% female
        if self._SpeciesN == 2 and random.random() > .5:
            self._SurnamesSpecies = NamesAll[math.floor(random.random() * 3 / 2)][self._SpeciesN - 1]
            suffix = SurnameSuffixDwarvenAll[self.sex][math.floor(random.random() * len(SurnameSuffixDwarvenAll[self.sex]))]
            for i in range(len(self._SurnamesSpecies)):
                self._SurnamesSpecies[i] = self._SurnamesSpecies[i] + suffix
        else:
            self._SurnamesSpecies = SurnamesAll[self._SpeciesN - 1]

        self.name = self._NamesSpecies[math.floor(random.random() * len(self._NamesSpecies))] + " " + \
                    self._SurnamesSpecies[math.floor(random.random() * len(self._SurnamesSpecies))]
    def roll_description(self):
        (self.desc_gen_look, self.desc_traits, self.desc_reactions), self.desc_appearance = get_traits(self), get_appearance(self)
    def roll_class(self):
        self._ClassN = random.randint(0, len(ClassAll)-1)
        self.ch_class = ClassAll[self._ClassN]
    def roll_career(self):
        # filter by class
        pool1 = list(range(ClassCareer[self._ClassN][0], ClassCareer[self._ClassN][1]))
        # filter by species
        self._CareerSpecies = CareerSpeciesAll[self._SpeciesN - 1]
        pool2 = []
        for idx in pool1:
            if self._CareerSpecies[idx] > 0:
                pool2.append(idx)
        # roll and assign
        self._CareerN = random.choice(pool2)
        self._CareerName = CareerL1[self._CareerN]
        self.career = self._CareerName
        self.career_level = 1
        self.status = CareerSocialL1[self._CareerN]
    def roll_attributes(self):
        #   0     1     2    3    4     5     6      7     8      9
        # ["WS", "BS", "S", "T", "AG", "I", "DEX", "INT", "WP", "FEL"]
        # roll base stats by species e.g. 2d10+20
        for i in range(len(self._StatsBase)):
            self._StatsBase[i] = roll2d10()+StatsAll[self._SpeciesN - 1][i]
        #   0    1     2          3           4
        # ["W", "M", "Fate", "Resilience", "Extra"]
        other_stats = StatsExtraAll[self._SpeciesN - 1]
        #   wounds
        bS = self._StatsBase[2] // 10
        bT = self._StatsBase[3] // 10
        bWP = self._StatsBase[8] // 10
        if self._SpeciesN == 0:  # "Human"
            self._StatsOther[0] = bS + 2 * bT + bWP
        elif self._SpeciesN == 1:  # "Dwarf"
            self._StatsOther[0] = bS + 2 * bT + bWP
        elif self._SpeciesN == 2:  # "Halfling"
            self._StatsOther[0] = 2 * bT + bWP
        elif self._SpeciesN == 3:  # "High Elf"
            self._StatsOther[0] = bS + 2 * bT + bWP
        elif self._SpeciesN == 4:  # "Wood Elf"
            self._StatsOther[0] = bS + 2 * bT + bWP
        elif self._SpeciesN == 5:  # "Gnome"
            self._StatsOther[0] = 2 * bT + bWP
        #   move speed
        self._StatsOther[1] = other_stats[1]
        #   fate, resilience
        roll_val = random.randint(0, other_stats[-1])
        self._StatsOther[2] += roll_val
        self._StatsOther[3] += other_stats[-1] - roll_val
        # update attributes
        self.update_attributes()
    def advance_stats(self):
        # add 5 advances points by career
        choice_list = [[5, 0, 0], [4, 1, 0], [3, 1, 1], [3, 2, 0], [2, 2, 1]]
        roll_list = choice_list[random.randint(0, 4)]
        for i in range(3):
            idx = CareerAdvanceL1[self._CareerN][i]
            self._StatsAdvance[idx] += roll_list[i]
        # update attributes
        self.update_attributes()
    def roll_skills_species(self):
        # roll 6 skills
        skills_by_species = SkillStartAll[self._SpeciesN - 1]
        self._SkillNames = []
        self._SkillValues = []
        indexes = []
        while len(indexes) < 6:
            idx = random.randint(0, len(skills_by_species) - 1)
            if idx not in indexes:
                indexes.append(idx)
        # get skill names, skill values by index
        for i, idx in enumerate(indexes):
            self._SkillNames.append(skills_by_species[idx])
            # advance
            if i < 3:
                self._SkillValues.append(5)     # 3 skills of value: 5
            else:
                self._SkillValues.append(3)     # 3 skills of value: 3
        # parse skill names
        self._SkillNames = self.parse_skill_words(self._SkillNames)
    def roll_talents_species(self):
        # roll 5 talents
        self._TalentNames = TalentStartAll[self._SpeciesN - 1]
        # parse talent names
        self._TalentNames = self.parse_talent_words(self._TalentNames)
        # advance
        self._TalentValues = [1]*len(self._TalentNames)
    def set_skills_career(self):
        # add 8 skills, advance 40 points
        skills_by_career = CareerSkillL1[self._CareerN]
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
        skills_values = example[random.randint(0, len(example)-1)]
        for skill_name, skill_value in zip(skills_by_career, skills_values):
            if skill_name not in self._SkillNames:
                self._SkillNames.append(skill_name)
                self._SkillValues.append(skill_value)
            else:
                idx = self._SkillNames.index(skill_name)
                self._SkillValues[idx] += skill_value
    def set_talents_career(self):
        # add 1 (out of 4) talent, advance
        # get unique names
        talents_by_career = list(set(CareerTalentsL1[self._CareerN]) - set(self._TalentNames))
        # pick one
        roll_val = random.randint(0, len(talents_by_career)-1)
        self._TalentNames.append(talents_by_career[roll_val])
        # parse talent names
        self._TalentNames = self.parse_talent_words(self._TalentNames)
        # advance
        self._TalentValues.append(1)
    def modify_stats_by_talents(self):
        # add values to basic stats, if talent says so
        # ["WS","BS","S","T","AG","I","DEX","INT","WP","FEL"]
        # ["W", "M", "Fate", "Resilience", "Extra"]
        for talent_name in self._TalentNames:
            if talent_name == "Coolheaded":
                self._StatsBase[8] += 5
            elif talent_name == "Fleetfooted":  # MoveSpeed += 1
                self._StatsOther[1] += 1
            elif talent_name == "Hardy":  # Wounds += Toughness Bonus
                bT = self._StatsTotal[3] // 10
                self._StatsOther[0] += bT
            elif talent_name == "Lightning Reflexes":
                self._StatsBase[4] += 5
            elif talent_name == "Marksman":
                self._StatsBase[1] += 5
            elif talent_name == "Nimble Fingered":
                self._StatsBase[6] += 5
            elif talent_name == "Savvy":
                self._StatsBase[7] += 5
            elif talent_name == "Sharp":
                self._StatsBase[5] += 5
            elif talent_name == "Suave":
                self._StatsBase[9] += 5
            elif talent_name == "Very Resilient":
                self._StatsBase[3] += 5
            elif talent_name == "Very Strong":
                self._StatsBase[2] += 5
            elif talent_name == "Warrior Born":
                self._StatsBase[0] += 5
        # update attributes
        self.update_attributes()
    def roll_other_things(self):
        def rollTrappings(TrapString):
            indexes = [i.start() for i in re.finditer("[0-9]d10", TrapString)]
            for index in indexes:
                number = int(TrapString[index:index + 1])  # Xd10
                rolled_val = rollXd10(number)
                TrapString = TrapString.replace(TrapString[index:index + 4], str(rolled_val))
            return TrapString
        def rollMoney(SocialString):
            ParsedSocial = SocialString.split(" ")
            if ParsedSocial[0] == "Gold":
                money = ParsedSocial[1] + " Gold Coins."
            elif ParsedSocial[0] == "Silver":
                money = str(rollXd10(int(ParsedSocial[1]))) + " Silver Coins."
            elif ParsedSocial[0] == "Brass":
                money = str(rollXd10(int(ParsedSocial[1]) * 2)) + " Brass Coins."
            else:
                money = "0 coins."
            return money
        # name - human Noble or Noble Blood?
        if (self._SpeciesN == 1) and ((self._CareerName == "Noble") or ("Noble Blood" in self._TalentNames)):
            name, surname = self.name.split(' ')
            if len([1 for suffix in SurnameSuffixHumanNoble if surname.find(suffix) >= 0]) == 0:
                surname = surname + SurnameSuffixHumanNoble[math.floor(random.random() * len(SurnameSuffixHumanNoble))]
            self.name = name + " von " + surname
        # skill - Dooming?
        if 'Doomed' in self._TalentNames:
            self._Dooming = DoomingsAll[math.floor(random.random() * len(DoomingsAll))]
            self.dooming = self._Dooming
        else:
            self.dooming = '-'
        # trapping and money
        self._Trapping = rollTrappings(TrappingClass[self._ClassN] + ", " + TrappingCareerL1[self._CareerN])
        self.trapping = self._Trapping
        self._Money = rollMoney(CareerSocialL1[self._CareerN])
        self.money = self._Money

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

    def advance_by_xp(self, xp=None):
        def advance_talents(xp_val, npc):
            # advance (to 1) all missing talents from career
            if npc.career_level == 1:
                talents_by_career = list(CareerTalentsL1[npc._CareerN])
            elif npc.career_level == 2:
                talents_by_career = list(CareerTalentsL2[npc._CareerN])
            elif npc.career_level == 3:
                talents_by_career = list(CareerTalentsL3[npc._CareerN])
            elif npc.career_level == 4:
                talents_by_career = list(CareerTalentsL4[npc._CareerN])
            else: return None    # error

            # find out which talent is already advanced and remove it from the list: talents_by_career
            for i in range(len(npc._TalentNames)):
                to_del = [t_name for t_name in talents_by_career if t_name.split('(')[0].find(npc._TalentNames[i].split('(')[0]) >= 0]
                if len(to_del) > 0:
                    for name in to_del:
                        talents_by_career.remove(name)
            # advance
            for talent_name in talents_by_career:
                if xp_val >= 100:
                    npc._TalentNames.append(talent_name)
                    npc._TalentValues.append(1)
                    xp_val -= 100   # advancing talent to 1 is always 100xp
            return xp_val
        def advance_stats(xp_val, npc):
            def get_cost(stat_val):
                if 0 <= stat_val < 5:
                    return 25
                elif 5 <= stat_val < 10:
                    return 30
                elif 10 <= stat_val < 15:
                    return 40
                elif 15 <= stat_val < 20:
                    return 50
                elif 20 <= stat_val <= 25:
                    return 70
                else: return None    # error
            # advance selected career stats to be able to reach next lvl
            if npc.career_level == 1:
                adv_sum = 5
                stats = CareerAdvanceL1[npc._CareerN]
            elif npc.career_level == 2:
                adv_sum = 10
                stats = CareerAdvanceL2[npc._CareerN]
            elif npc.career_level == 3:
                adv_sum = 15
                stats = CareerAdvanceL3[npc._CareerN]
            elif npc.career_level == 4:
                adv_sum = 20
                stats = CareerAdvanceL4[npc._CareerN]
            else: return None    # error

            for i in range(len(stats)):
                idx = stats[i]
                if npc._StatsAdvance[idx] < adv_sum:
                    for j in range(adv_sum - npc._StatsAdvance[idx]):
                        cost = get_cost(npc._StatsAdvance[idx])
                        if xp_val >= cost:
                            npc._StatsAdvance[idx] += 1
                            xp_val -= cost
            return xp_val
        def advance_skills(xp_val, npc):
            def get_cost(skill_val):
                if 0 <= skill_val < 5:
                    return 10
                elif 5 <= skill_val < 10:
                    return 15
                elif 10 <= skill_val < 15:
                    return 20
                elif 15 <= skill_val < 20:
                    return 30
                elif 20 <= skill_val <= 25:
                    return 40
                else: return None    # error
            # advance all career skills to be able to reach next level
            if npc.career_level == 1:
                adv_sum = 5
            elif npc.career_level == 2:
                adv_sum = 10
            elif npc.career_level == 3:
                adv_sum = 15
            elif npc.career_level == 4:
                adv_sum = 20
            else: return None    # error

            for i in range(len(npc._SkillValues)):
                if npc._SkillValues[i] < adv_sum:
                    for j in range(adv_sum - npc._SkillValues[i]):
                        cost = get_cost(npc._SkillValues[i])
                        if xp_val >= cost:
                            npc._SkillValues[i] += 1
                            xp_val -= cost
            return xp_val
        def advance_next_level(xp_val, npc):
            # possible for levels: 1-3
            def rollTrappings(TrapString):
                indexes = [i.start() for i in re.finditer("[0-9]d10", TrapString)]
                for index in indexes:
                    number = int(TrapString[index:index + 1])  # Xd10
                    rolled_val = rollXd10(number)
                    TrapString = TrapString.replace(TrapString[index:index + 4], str(rolled_val))
                return TrapString
            def rollMoney(SocialString, in_npc):
                # old values
                values = [0, 0, 0]  # Gold Coins, Silver Coins, Brass Coins
                splits_gold = in_npc._Money.split(' Gold Coins')
                splits_silver = in_npc._Money.split(' Silver Coins')
                splits_brass = in_npc._Money.split(' Brass Coins')
                if splits_gold[0].isdecimal():
                    values[0] += int(splits_gold[0])
                if splits_silver[0].isdecimal():
                    values[1] += int(splits_silver[0])
                if splits_brass[0].isdecimal():
                    values[2] += int(splits_brass[0])

                # roll
                ParsedSocial = SocialString.split(" ")
                if ParsedSocial[0] == "Gold":
                    money = ParsedSocial[1] + " Gold Coins."
                elif ParsedSocial[0] == "Silver":
                    money = str(rollXd10(int(ParsedSocial[1]))) + " Silver Coins."
                elif ParsedSocial[0] == "Brass":
                    money = str(rollXd10(int(ParsedSocial[1]) * 2)) + " Brass Coins."
                else:
                    money = "0 Brass Coins."

                # new values
                splits_gold = money.split(' Gold Coins')
                splits_silver = money.split(' Silver Coins')
                splits_brass = money.split(' Brass Coins')
                if splits_gold[0].isdecimal():
                    values[0] += int(splits_gold[0])
                if splits_silver[0].isdecimal():
                    values[1] += int(splits_silver[0])
                if splits_brass[0].isdecimal():
                    values[2] += int(splits_brass[0])
                out_str = []
                if values[0] > 0:
                    out_str.append(f'{values[0]} Gold Coins')
                if values[1] > 0:
                    out_str.append(f'{values[1]} Silver Coins')
                if values[2] > 0:
                    out_str.append(f'{values[1]} Brass Coins')

                return ', '.join(out_str)

            is_ready = False
            if npc.career_level == 1:
                stats_adv = [npc._StatsAdvance[idx] for idx in CareerAdvanceL1[npc._CareerN]]
                sum_adv = 5
                new_level = {"name": CareerL2[npc._CareerN], "status": CareerSocialL2[npc._CareerN], "skills": CareerSkillL2[npc._CareerN], "trapping": TrappingCareerL2[npc._CareerN], "money": CareerSocialL2[npc._CareerN]}
            elif npc.career_level == 2:
                stats_adv = [npc._StatsAdvance[idx] for idx in CareerAdvanceL2[npc._CareerN]]
                sum_adv = 10
                new_level = {"name": CareerL3[npc._CareerN], "status": CareerSocialL3[npc._CareerN], "skills": CareerSkillL3[npc._CareerN], "trapping": TrappingCareerL3[npc._CareerN], "money": CareerSocialL3[npc._CareerN]}
            elif npc.career_level == 3:
                stats_adv = [npc._StatsAdvance[idx] for idx in CareerAdvanceL3[npc._CareerN]]
                sum_adv = 15
                new_level = {"name": CareerL4[npc._CareerN], "status": CareerSocialL4[npc._CareerN], "skills": CareerSkillL4[npc._CareerN], "trapping": TrappingCareerL4[npc._CareerN], "money": CareerSocialL4[npc._CareerN]}
            else:
                return xp_val, is_ready
            # stats from career lvl >= sum_adv
            # 8 skills values >= sum_adv
            # 1 talent from career lvl
            # 100 xp
            if False not in \
                    [val >= sum_adv for val in stats_adv] + \
                    [sum([1 for val in npc._SkillValues if val >= sum_adv]) >= 8] + \
                    [sum(1 for val in npc._TalentValues if val >= 1) >= 1] + \
                    [xp_val >= 100]:
                is_ready = True
                # deduct xp
                xp_val -= 100
                # new: career name, social status
                npc._CareerName = new_level["name"]
                npc.career = npc._CareerName
                npc.career_level += 1
                npc.status = new_level["status"]
                # new: skills (value=0)
                skills_by_career = new_level["skills"]
                skills_values = [0]*len(skills_by_career)
                for skill_name, skill_value in zip(skills_by_career, skills_values):
                    npc._SkillNames.append(skill_name)
                    npc._SkillValues.append(skill_value)
                npc._SkillNames = npc.parse_skill_words(npc._SkillNames)
                # don't need to add talents - they will be added during next advances
                # new: trapping (add)
                npc._Trapping = npc._Trapping + ', ' + rollTrappings(new_level["trapping"])
                npc.trapping = npc._Trapping
                # new money (add)
                npc._Money = rollMoney(new_level["money"], npc)
                npc.money = npc._Money

                return xp_val, is_ready
            else:
                return xp_val, is_ready
        if xp is None:
            xp = self.xp_start
        # ------------------------------------------------------
        xp = advance_talents(xp, self)
        self._TalentNames = self.parse_talent_words(self._TalentNames)  # new talents are added
        self.modify_stats_by_talents()
        self.update_all()
        # ------------------------------------------------------
        xp = advance_stats(xp, self)
        self.update_all()
        # ------------------------------------------------------
        xp = advance_skills(xp, self)
        self.update_all()
        # ------------------------------------------------------
        # advance to new level?
        xp, ready = advance_next_level(xp, self)
        self.update_all()
        if ready:
            self.advance_by_xp(xp)
        else:
            self.xp_left = xp


    @staticmethod
    def parse_skill_words(skill_names):
        # (Any one)
        for i in range(len(skill_names)):
            skill_name = skill_names[i]
            if skill_name.find("(Any one)") >= 0:
                for s_list in AnySkills:
                    if skill_name in s_list:
                        skill_names[i] = s_list[random.randint(1, len(s_list) - 1)]
                        break
        return skill_names
    @staticmethod
    def parse_talent_words(talent_names):
        for i in range(len(talent_names)):
            talent_name = talent_names[i]
            # sth " or " sth
            if talent_name.find(" or ") >= 0:
                two_talents = talent_name.split(" or ")
                talent_names[i] = two_talents[random.randint(0, 1)]      # pick one of two talents
            # Random
            if talent_name == "Random":
                roll_val = roll1d100()
                j = 0
                while j < len(TalentRandom):
                    if roll_val <= TalentRandom[j]:
                        break
                    j += 1
                talent_names[i] = TalentRandomName[j]   # pick from random table (TalentRandomName)
            # (Any one)
            if talent_name.find("(Any one)") >= 0:
                for t_list in AnyTalents:
                    if talent_name in t_list:
                        talent_names[i] = t_list[random.randint(1, len(t_list) - 1)]
                        break
        return talent_names
    def update_attributes(self):
        # INTERNAL
        #   * _StatsTotal
        self._StatsTotal = [val1 + val2 for val1, val2 in zip(self._StatsBase, self._StatsAdvance)]
        #   * Wounds (_StatsOther[0])
        bS = self._StatsTotal[2] // 10
        bT = self._StatsTotal[3] // 10
        bWP = self._StatsTotal[8] // 10
        if self._SpeciesN == 0:  # "Human"
            self._StatsOther[0] = bS + 2 * bT + bWP
        elif self._SpeciesN == 1:  # "Dwarf"
            self._StatsOther[0] = bS + 2 * bT + bWP
        elif self._SpeciesN == 2:  # "Halfling"
            self._StatsOther[0] = 2 * bT + bWP
        elif self._SpeciesN == 3:  # "High Elf"
            self._StatsOther[0] = bS + 2 * bT + bWP
        elif self._SpeciesN == 4:  # "Wood Elf"
            self._StatsOther[0] = bS + 2 * bT + bWP
        elif self._SpeciesN == 5:  # "Gnome"
            self._StatsOther[0] = 2 * bT + bWP
        # EXTERNAL
        self.attributes = {"WS": [self._StatsBase[0], self._StatsAdvance[0], self._StatsTotal[0]],
                           "BS": [self._StatsBase[1], self._StatsAdvance[1], self._StatsTotal[1]],
                           "S":  [self._StatsBase[2], self._StatsAdvance[2], self._StatsTotal[2]],
                           "T":  [self._StatsBase[3], self._StatsAdvance[3], self._StatsTotal[3]],
                           "AG": [self._StatsBase[4], self._StatsAdvance[4], self._StatsTotal[4]],
                           "I":  [self._StatsBase[5], self._StatsAdvance[5], self._StatsTotal[5]],
                           "DEX":[self._StatsBase[6], self._StatsAdvance[6], self._StatsTotal[6]],
                           "INT":[self._StatsBase[7], self._StatsAdvance[7], self._StatsTotal[7]],
                           "WP" :[self._StatsBase[8], self._StatsAdvance[8], self._StatsTotal[8]],
                           "FEL":[self._StatsBase[9], self._StatsAdvance[9], self._StatsTotal[9]],
                           "Wounds":    [self._StatsOther[0], self._StatsOther[0], self._StatsOther[0]],
                           "MoveSpeed": [self._StatsOther[1], self._StatsOther[1], self._StatsOther[1]],
                           "Fate":      [self._StatsOther[2], self._StatsOther[2], self._StatsOther[2]],
                           "Resilience":[self._StatsOther[3], self._StatsOther[3], self._StatsOther[3]]}
    def update_skills(self):
        # EXTERNAL
        #   basic
        found_total = []
        out = {}  # {skill_name: [stat_str, stat_total, skill_advances, skill_total]}
        for skill_name in data_SkillsBasic.keys():     # e.g. "Animal Training"
            skill_list = data_SkillsBasic[skill_name]  # e.g: ["INT", "advanced", ["Demigryph", "Dog", "Horse", "Pegasus", "Pigeon"]]
            found = False
            for i in range(len(self._SkillNames)):
                if skill_name.split(' (')[0] == self._SkillNames[i].split(' (')[0]:
                    stat_str = skill_list[0]  # e.g. "INT"
                    stat_total = self._StatsTotal[StatsName.index(stat_str)]  # e.g. =20
                    skill_advances = self._SkillValues[i]  # e.g. "Animal Training"=5
                    skill_total = stat_total + skill_advances  # e.g. =25
                    out.update({self._SkillNames[i]: [stat_str, stat_total, skill_advances, skill_total]})
                    found = True
                    found_total.append(self._SkillNames[i])
            if not found:
                stat_str = skill_list[0]
                stat_total = self._StatsTotal[StatsName.index(stat_str)]
                skill_advances = 0
                skill_total = stat_total + skill_advances
                out.update({skill_name: [stat_str, stat_total, skill_advances, skill_total]})
        #   special for 'Meele' - leave just one, the highest

        self.skills_basic = out

        #   advanced
        out = {}  # {skill_name: [stat_str, stat_total, skill_advances, skill_total]}
        for skill_name in data_SkillsAdvanced.keys():     # e.g. "Animal Training"
            skill_list = data_SkillsAdvanced[skill_name]  # e.g: ["INT", "advanced", ["Demigryph", "Dog", "Horse", "Pegasus", "Pigeon"]]
            found = False
            for i in range(len(self._SkillNames)):
                if skill_name.split(' (')[0] == self._SkillNames[i].split(' (')[0]:
                    stat_str = skill_list[0]                                    # e.g. "INT"
                    stat_total = self._StatsTotal[StatsName.index(stat_str)]    # e.g. =20
                    skill_advances = self._SkillValues[i]                       # e.g. "Animal Training"=5
                    skill_total = stat_total + skill_advances                   # e.g. =25
                    out.update({self._SkillNames[i]: [stat_str, stat_total, skill_advances, skill_total]})
                    found = True
                    found_total.append(self._SkillNames[i])
            if not found:
                stat_str = skill_list[0]
                stat_total = self._StatsTotal[StatsName.index(stat_str)]
                skill_advances = 0
                skill_total = stat_total + skill_advances
                out.update({skill_name: [stat_str, stat_total, skill_advances, skill_total]})

        # filter only skills with at least 1 advance
        out2 = {}
        for skill_name, values_list in out.items():
            if values_list[2] > 0:
                out2.update({skill_name: values_list})
        self.skills_advanced = out2
        if len(found_total) != len(self._SkillNames): print("Not all skills were found", 'FOUND:', found_total, 'ALL:', self._SkillNames)

    def update_talents(self):
        # EXTERNAL
        out = {}
        for _talent_name in self._TalentNames:  # e.g.  "Accurate Shot": ["Bonus BS", "BS", "+[lvl]dmg on all ranged weapons."],
            idx, test, desc = None, None, None
            for i, val_str in enumerate(data_Talents.keys()):
                if _talent_name.split(' (')[0] == val_str.split(' (')[0]:
                    idx, test, desc = i, data_Talents[val_str][1], data_Talents[val_str][2]

            if None not in [idx, test, desc]:
                out.update({_talent_name: (test, desc)})  # {talent_name: (test, description)}
            else:
                print("!!Talent not found\t" + _talent_name)

        self.talents = out
    def update_all(self):
        self.update_attributes()
        self.update_skills()
        self.update_talents()

