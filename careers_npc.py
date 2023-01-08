class CareerClass:
    def __init__(self, name, status, advances, skills, talents, trappings):
        self.name = name    # str
        self.status = status    # str
        self.advances = advances  # list of str
        self.skills = skills  # list of str
        self.talents = talents  # list of str
        self.trappings = trappings  # str


class CareerApothecary:
    def __init__(self):
        self.lvl = [
            CareerClass("Apothecary’s Apprentice",
                        "Brass 3",
                        ['T', 'DEX', 'INT'],
                        ['Consume Alcohol', 'Heal', 'Language (Classical)', 'Lore (Chemistry)', 'Lore (Medicine)', 'Lore (Plants)', 'Trade (Apothecary)', 'Trade (Poisoner)'],
                        ['Concoct', 'Craftsman (Apothecary)', 'Etiquette (Scholar)', 'Read/Write'],
                        "Book (Blank), Healing Draft, Leather Jerkin, Pestle and Mortar"),
            CareerClass("Apothecary",
                        "Silver 1",
                        ['FEL'],
                        ['Charm', 'Haggle', 'Lore (Science)', 'Gossip', 'Language (Guilder)', 'Perception'],
                        ['Criminal', 'Dealmaker', 'Etiquette (Guilder)', 'Pharmacist'],
                        "Guild Licence, Trade Tools"),
            CareerClass("Master Apothecary",
                        "Silver 3",
                        ['I'],
                        ['Intuition', 'Leadership', 'Research', 'Secret Signs (Guilder)'],
                        ['Bookish', 'Master Tradesman (Apothecary),Resistance (Poison)', 'Savvy'],
                        "Book (Apothecary), Apprentice, Workshop"),
            CareerClass("Apothecary-General",
                        "Gold 1",
                        ['WP'],
                        ['Intimidate', 'Ride (Horse)'],
                        ['Acute Sense (Taste)', 'Coolheaded', 'Master Tradesman (Poisoner)', 'Savant (Apothecary)'],
                        "Commission Papers, Large Workshop")
        ]


class CareerEngineer:
    def __init__(self):
        self.lvl = [
            CareerClass("Student Engineer",
                        "Brass 4",
                        ['BS', 'DEX', 'INT'],
                        ['Consume Alcohol', 'Cool', 'Endurance', 'Language (Classical)', 'Lore (Science)', 'Perception', 'Ranged (Blackpowder)', 'Trade (Engineer)'],
                        ['Artistic', 'Gunner', 'Read/Write', 'Tinker'],
                        "Book (Engineer), Hammer and Spikes"),
            CareerClass("Engineer",
                        "Silver 2",
                        ['I'],
                        ['Drive', 'Dodge', 'Navigation', 'Ranged (Engineering)', 'Research', 'Language (Guilder)'],
                        ['Craftsman (Engineer)', 'Etiquette (Guilder)', 'Marksman', 'Orientation'],
                        "Guild Licence, Trade Tools"),
            CareerClass("Master Engineer",
                        "Silver 4",
                        ['T'],
                        ['Language (Khazalid)', 'Leadership', 'Ride (Horse)', 'Secret Signs (Guilder)'],
                        ['Etiquette (Scholar)', 'Master Tradesman (Engineering)', 'Sniper', 'Super Numerate'],
                        "Workshop"),
            CareerClass("Chartered Engineer",
                        "Gold 2",
                        ['WP'],
                        ['Language (Any one)', 'Lore (Any one)'],
                        ['Magnum Opus', 'Rapid Reload', 'Savant (Engineering)', 'Unshakeable'],
                        "Guild License, Library (Engineer), Quality Trade Tools (Engineer), Large Workshop (Engineer)")
        ]


class CareerLawyer:
    def __init__(self):
        self.lvl = [
            CareerClass("Student Lawyer",
                        "Brass 4",
                        ['I', 'DEX', 'INT'],
                        ['Consume Alcohol', 'Endurance', 'Haggle', 'Language (Classical)', 'Lore (Law)', 'Lore (Theology)', 'Perception', 'Research'],
                        ['Blather', 'Etiquette (Scholar)', 'Read/Write', 'Speedreader'],
                        "Book (Law), Magnifying Glass"),
            CareerClass("Lawyer",
                        "Silver 3",
                        ['FEL'],
                        ['Bribery', 'Charm', 'Gossip', 'Intuition', 'Language (Guilder)', 'Secret Signs (Guilder)'],
                        ['Argumentative', 'Criminal', 'Etiquette (Guilder)', 'Suave'],
                        "Court Robes, Guild Licence, Writing Kit"),
            CareerClass("Barrister",
                        "Gold 1",
                        ['WP'],
                        ['Art (Writing)', 'Entertain (Speeches)', 'Intimidate', 'Lore (Any one)'],
                        ['Bookish', 'Cat-tongued', 'Impassioned Zeal', 'Savvy'],
                        "Office, Assistant (Student or Servant)"),
            CareerClass("Judge",
                        "Gold 2",
                        ['T'],
                        ['Cool', 'Lore (Any one)'],
                        ['Commanding Presence', 'Kingpin', 'Savant (Law)', 'Wealthy'],
                        "Gavel, Ostentatious Wig")
        ]


class CareerNun:
    def __init__(self):
        self.lvl = [
            CareerClass("Novitiate Nun",
                        "Brass 1",
                        ['DEX', 'INT', 'FEL'],
                        ['Art (Calligraphy)', 'Cool', 'Endurance', 'Entertain (Storyteller)', 'Gossip', 'Heal', 'Lore (Theology)', 'Pray'],
                        ['Bless (Any one)', 'Stone Soup', 'Panhandle', 'Read/Write'],
                        "Religious Symbol, Robes"),
            CareerClass("Nun",
                        "Brass 4",
                        ['WP'],
                        ['Charm', 'Melee (Any one)', 'Research', 'Trade (Brewer)', 'Trade (Herbalist)', 'Trade (Vintner)'],
                        ['Etiquette (Cultists)', 'Field Dressing', 'Holy Visions', 'Invoke (Any one)'],
                        "Book (Religion), Religious Relic, Trade Tools (Any one)"),
            CareerClass("Abbess",
                        "Silver 2",
                        ['I'],
                        ['Leadership', 'Lore (Local)', 'Lore (Politics)', 'Perception'],
                        ['Resistance (Any one)', 'Robust', 'Savant (Theology)', 'Stout-hearted'],
                        "Abbey, Library (Theology)"),
            CareerClass("Prioress General",
                        "Silver 5",
                        ['T'],
                        ['Language (Any one)', 'Lore (Any one)'],
                        ['Commanding Presence', 'Iron Will', 'Pure Soul', 'Strong-minded'],
                        "Religious Order")
        ]


class CareerPhysician:
    def __init__(self):
        self.lvl = [
            CareerClass("Physician’s Apprentice",
                        "Brass 4",
                        ['DEX', 'INT', 'WP'],
                        ['Bribery', 'Cool', 'Drive', 'Endurance', 'Gossip', 'Heal', 'Perception', 'Sleight of Hand'],
                        ['Bookish', 'Field Dressing', 'Read/Write', 'Strike to Stun'],
                        "Bandages, Healing Draught"),
            CareerClass("Physician",
                        "Silver 3",
                        ['FEL'],
                        ['Charm', 'Haggle', 'Language (Guilder)', 'Lore (Anatomy)', 'Lore (Medicine)', 'Trade (Barber)'],
                        ['Coolheaded', 'Criminal', 'Etiquette (Guilder)', 'Surgery'],
                        "Book (Medicine), Guild Licence, Trade Tools (Medicine)"),
            CareerClass("Doktor",
                        "Silver 5",
                        ['I'],
                        ['Consume Alcohol', 'Intimidate', 'Leadership', 'Research'],
                        ['Etiquette (Scholars)', 'Resistance (Disease)', 'Savvy', 'Strike to Injure'],
                        "Apprentice, Workshop (Medicine)"),
            CareerClass("Court Physician",
                        "Gold 1",
                        ['AG'],
                        ['Lore (Noble)', 'Perform (Dancing)'],
                        ['Etiquette (Nobles)', 'Nimble Fingered', 'Savant (Medicine)', 'Strong-minded'],
                        "Courtly Attire, Letter of Appointment")
        ]


class CareerPriest:
    def __init__(self):
        self.lvl = [
            CareerClass("Initiate Priest",
                        "Brass 2",
                        ['T', 'AG', 'WP'],
                        ['Athletics', 'Cool', 'Endurance', 'Intuition', 'Lore (Theology)', 'Perception', 'Pray', 'Research'],
                        ['Bless (Any one)', 'Holy Visions', 'Read/Write', 'Suave'],
                        "Religious Symbol, Robes"),
            CareerClass("Priest",
                        "Silver 1",
                        ['FEL'],
                        ['Charm', 'Entertain (Storytelling)', 'Gossip', 'Heal', 'Intimidate', 'Melee (Basic)'],
                        ['Blather', 'Bookish', 'Etiquette (Cultists)', 'Invoke (Any one)'],
                        "Book (Religion), Ceremonial Robes"),
            CareerClass("High Priest",
                        "Gold 1",
                        ['INT'],
                        ['Art (Writing)', 'Entertain (Speeches)', 'Leadership', 'Lore (Heraldry)'],
                        ['Acute Sense (Any one)', 'Hatred (Any one)', 'Impassioned Zeal', 'Strong-minded'],
                        "Quality Robes, Religious Relic, Subordinate Priests, Temple"),
            CareerClass("Lector",
                        "Gold 2",
                        ['I'],
                        ['Language (Any one)', 'Lore (Politics)'],
                        ['Master Orator', 'Pure Soul', 'Resistance (Any one)', 'Savant (Theology)'],
                        "Library (Theology), Subordinate High Priests")
        ]


class CareerScholar:
    def __init__(self):
        self.lvl = [
            CareerClass("Student Scholar",
                        "Brass 3",
                        ['T', 'INT', 'WP'],
                        ['Consume Alcohol', 'Entertain (Storytelling)', 'Gamble', 'Gossip', 'Haggle', 'Language (Classical)', 'Lore (Any one)', 'Research'],
                        ['Carouser', 'Read/Write', 'Savvy', 'Super Numerate'],
                        "Alcohol, Book, Opinions, Writing Kit"),
            CareerClass("Scholar",
                        "Silver 2",
                        ['I'],
                        ['Art (Writing)', 'Intuition', 'Language (Any one)', 'Lore (Any one)', 'Perception', 'Trade (Any one)'],
                        ['Bookish', 'Etiquette (Scholars)', 'Speedreader', 'Suave'],
                        "Access to a Library, Degree"),
            CareerClass("Fellow",
                        "Silver 5",
                        ['FEL'],
                        ['Entertain (Lecture)', 'Intimidate', 'Language (Any one)', 'Lore (Any one)'],
                        ['Linguistics', 'Public Speaker', 'Savant (Any one)', 'Tower of Memories'],
                        "Mortarboard, Robes"),
            CareerClass("Professor",
                        "Gold 1",
                        ['DEX'],
                        ['Entertain (Rhetoric)', 'Lore (Any one)'],
                        ['Magnum Opus', 'Master Orator', 'Savant (Any one)', 'Sharp'],
                        "Study")
        ]


class CareerWizard:
    def __init__(self):
        self.lvl = [
            CareerClass("Wizard’s Apprentice",
                        "Brass 3",
                        ['WS', 'INT', 'WP'],
                        ['Channelling', 'Dodge', 'Intuition', 'Language (Magick)', 'Lore (Magic)', 'Melee (Basic)', 'Melee (Polearm)', 'Perception'],
                        ['Aethyric Attunement', 'Petty Magic', 'Read/Write', 'Second Sight'],
                        "Grimoire, Quarterstaff"),
            CareerClass("Wizard",
                        "Silver 3",
                        ['AG'],
                        ['Charm', 'Cool', 'Gossip', 'Intimidate', 'Language (Battle)', 'Language (Any one)'],
                        ['Arcane Magic (Any Arcane Lore)', 'Detect Artefact', 'Fast Hands', 'Sixth Sense'],
                        "Magical License"),
            CareerClass("Master Wizard",
                        "Gold 1",
                        ['I'],
                        ['Animal Care', 'Evaluate', 'Lore (Warfare)', 'Ride (Horse)'],
                        ['Dual Wielder', 'Instinctive Diction', 'Magical Sense', 'Menacing'],
                        "Apprentice, Light Warhorse, Magical Item"),
            CareerClass("Wizard Lord",
                        "Gold 2",
                        ['FEL'],
                        ['Language (Any one)', 'Lore (Any one)'],
                        ['Combat Aware', 'Frightening', 'Iron Will', 'War Wizard'],
                        "Apprentice, Library (Magic), Workshop (Magic)")
        ]


class CareerAgitator:
    def __init__(self):
        self.lvl = [
            CareerClass("Pamphleteer",
                        "Brass 1",
                        ['BS', 'INT', 'FEL'],
                        ['Art (Writing)', 'Bribery', 'Charm', 'Consume Alcohol', 'Gossip', 'Haggle', 'Lore (Politics)', 'Trade (Printing)'],
                        ['Blather', 'Gregarious', 'Panhandle', 'Read/Write'],
                        "Writing Kit, Hammer and Nails, Pile of Leaflets"),
            CareerClass("Agitator",
                        "Brass 2",
                        ['AG'],
                        ['Cool', 'Dodge', 'Entertain (Storytelling)', 'Gamble', 'Intuition', 'Leadership'],
                        ['Alley Cat', 'Argumentative', 'Impassioned Zeal', 'Public Speaker'],
                        "Leather Jack"),
            CareerClass("Rabble Rouser",
                        "Brass 3",
                        ['WS'],
                        ['Athletics', 'Intimidate', 'Melee (Fist)', 'Perception'],
                        ['Cat-tongued', 'Dirty Fighting', 'Flee', 'Step Aside'],
                        "Hand Weapon, Pamphleteer"),
            CareerClass("Demagogue",
                        "Brass 5",
                        ['I'],
                        ['Lore (Heraldry)', 'Ride (Horse)'],
                        ['Etiquette (Any one)', 'Master Orator', 'Schemer', 'Suave'],
                        "3 Pamphleteers, Patron, Printing Press, Impressive Hat")
        ]


class CareerArtisan:
    def __init__(self):
        self.lvl = [
            CareerClass("Apprentice Artisan",
                        "Brass 2",
                        ['S', 'T', 'DEX'],
                        ['Athletics', 'Cool', 'Consume Alcohol', 'Dodge', 'Endurance', 'Evaluate', 'Stealth (Urban)', 'Trade (Any one)'],
                        ['Artistic', 'Craftsman (Any one)', 'Strong Back', 'Very Strong'],
                        "Chalk, Leather Jerkin, 1d10 rags"),
            CareerClass("Artisan",
                        "Silver 1",
                        ['FEL'],
                        ['Charm', 'Haggle', 'Lore (Local)', 'Gossip', 'Language (Guilder)', 'Perception'],
                        ['Dealmaker', 'Etiquette (Guilder)', 'Nimble Fingered', 'Sturdy'],
                        "Guild Licence, Trade Tools"),
            CareerClass("Master Artisan",
                        "Silver 3",
                        ['WP'],
                        ['Intuition', 'Leadership', 'Research', 'Secret Signs (Guilder)'],
                        ['Acute Sense (Taste or Touch)', 'Master Tradesman (Any one)', 'Read/Write', 'Tinker'],
                        "Apprentice, Workshop"),
            CareerClass("Guildmaster",
                        "Gold 1",
                        ['INT'],
                        ['Bribery', 'Intimidate'],
                        ['Briber', 'Magnum Opus', 'Public Speaker', 'Schemer'],
                        "Guild, Quality Clothing")
        ]


class CareerBeggar:
    def __init__(self):
        self.lvl = [
            CareerClass("Pauper",
                        "Brass 0",
                        ['T', 'AG', 'FEL'],
                        ['Athletics', 'Charm', 'Consume Alcohol', 'Cool', 'Dodge', 'Endurance', 'Intuition', 'Stealth (Urban)'],
                        ['Panhandle', 'Resistance (Disease)', 'Stone Soup', 'Very Resilient'],
                        "Poor Quality Blanket, Cup"),
            CareerClass("Beggar",
                        "Brass 2",
                        ['WP'],
                        ['Entertain (Acting)', 'Entertain (Any one)', 'Gossip', 'Haggle', 'Perception', 'Sleight of Hand'],
                        ['Alley Cat', 'Beneath Notice', 'Criminal', 'Etiquette (Criminals)'],
                        "Crutch, Bowl"),
            CareerClass("Master Beggar",
                        "Brass 4",
                        ['WS'],
                        ['Charm Animal', 'Leadership', 'Lore (Local)', 'Secret Signs (Vagabond)'],
                        ['Blather', 'Dirty Fighting', 'Hardy', 'Step Aside'],
                        "Disguise Kit, Hiding Place, Pauper Follower"),
            CareerClass("Beggar King",
                        "Silver 2",
                        ['I'],
                        ['Bribery', 'Intimidate'],
                        ['Cat-tongued', 'Fearless (Watchmen)', 'Kingpin', 'Suave'],
                        "Lair, Large Group of Beggar Followers")
        ]


class CareerInvestigator:
    def __init__(self):
        self.lvl = [
            CareerClass("Sleuth",
                        "Silver 1",
                        ['I', 'AG', 'INT'],
                        ['Charm', 'Climb', 'Cool', 'Gossip', 'Intuition', 'Perception', 'Stealth (Urban)', 'Track'],
                        ['Alley Cat', 'Beneath Notice', 'Read/Write', 'Sharp'],
                        "Lantern, Lamp Oil, Journal, Quill and Ink"),
            CareerClass("Investigator",
                        "Silver 2",
                        ['FEL'],
                        ['Consume Alcohol', 'Dodge', 'Lore (Law)', 'Melee (Brawling)', 'Pick Lock', 'Sleight of Hand'],
                        ['Etiquette (Any one)', 'Savvy', 'Shadow', 'Tenacious'],
                        "Leather Jack, Hand Weapon, Magnifying Glass, Lockpick"),
            CareerClass("Master Investigator",
                        "Silver 3",
                        ['DEX'],
                        ['Bribery', 'Evaluate', 'Leadership', 'Lore (Any one)'],
                        ['Bookish', 'Break and Enter', 'Sixth Sense', 'Suave'],
                        "Assistant, Office"),
            CareerClass("Detective",
                        "Silver 5",
                        ['WP'],
                        ['Intimidate', 'Lore (Any one)'],
                        ['Acute Sense (Any one)', 'Savant (Any one)', 'Speedreader', 'Tower of Memories'],
                        "Network of Informants, Spyglass")
        ]


class CareerMerchant:
    def __init__(self):
        self.lvl = [
            CareerClass("Trader",
                        "Silver 2",
                        ['WS', 'AG', 'FEL'],
                        ['Animal Care', 'Bribery', 'Charm', 'Consume Alcohol', 'Drive', 'Gamble', 'Gossip', 'Haggle'],
                        ['Blather', 'Dealmaker', 'Read/Write', 'Suave'],
                        "Abacus, Mule and Cart, Canvas Tarpaulin, 3d10 Silver Coins"),
            CareerClass("Merchant",
                        "Silver 5",
                        ['INT'],
                        ['Evaluate', 'Intuition', 'Language (Any one)', 'Language (Guilder)', 'Lore (Local)', 'Perception'],
                        ['Briber', 'Embezzle', 'Etiquette (Guilder)', 'Savvy'],
                        "Riverboat or 2 Wagons, Guild License, 20 Gold Coins"),
            CareerClass("Master Merchant",
                        "Gold 1",
                        ['I'],
                        ['Cool', 'Language (Classical)', 'Navigation', 'Secret Signs (Guilder)'],
                        ['Cat-tongued', 'Etiquette (Any one)', 'Numismatics', 'Sharp'],
                        "Town House with Servants, Warehouse, 100 Gold Coins"),
            CareerClass("Merchant Prince",
                        "Gold 3",
                        ['WP'],
                        ['Lore (Any one)', 'Intimidate'],
                        ['Iron Will', 'Luck', 'Schemer', 'Wealthy'],
                        "2 Riverboats or 4 Wagons, Large Town Estate, 2 Warehouses, 1000 Gold Coins, Quality Clothing")
        ]


class CareerRatCatcher:
    def __init__(self):
        self.lvl = [
            CareerClass("Rat Hunter",
                        "Brass 2",
                        ['WS', 'BS', 'WP'],
                        ['Athletics', 'Animal Training (Dog)', 'Charm Animal', 'Consume Alcohol', 'Endurance', 'Melee (Basic)', 'Ranged (Sling)', 'Stealth (Underground or Urban)'],
                        ['Night Vision', 'Resistance (Disease)', 'Strike Mighty Blow', 'Strike to Stun'],
                        "Sling with Ammunition, Sack, Small but Vicious Dog"),
            CareerClass("Rat Catcher",
                        "Silver 1",
                        ['T'],
                        ['Animal Care', 'Gossip', 'Haggle', 'Lore (Poison)', 'Perception', 'Set Trap'],
                        ['Enclosed Fighter', 'Etiquette (Guilder)', 'Fearless (Rats)', 'Very Resilient'],
                        "Animal Traps, Pole for Dead Rats"),
            CareerClass("Sewer Jack",
                        "Silver 2",
                        ['I'],
                        ['Climb', 'Cool', 'Dodge', 'Ranged (Crossbow Pistol)'],
                        ['Hardy', 'Stout-hearted', 'Strong Legs', 'Tunnel Rat'],
                        "Davrich Lantern, Hand Weapon, Leather Jack"),
            CareerClass("Exterminator",
                        "Silver 3",
                        ['S'],
                        ['Leadership', 'Track'],
                        ['Fearless (Skaven)', 'Menacing', 'Robust', 'Strong-minded'],
                        "Assistant, Large and Vicious Dog, Sack of Poisoned Bait (10 doses of Heartkill)")
        ]


class CareerTownsman:
    def __init__(self):
        self.lvl = [
            CareerClass("Clerk",
                        "Silver 1",
                        ['AG', 'INT', 'FEL'],
                        ['Charm', 'Climb', 'Consume Alcohol', 'Drive', 'Dodge', 'Gamble', 'Gossip', 'Haggle'],
                        ['Alley Cat', 'Beneath Notice', 'Etiquette (Servants)', 'Sturdy'],
                        "Lodgings, Sturdy Boots"),
            CareerClass("Townsman",
                        "Silver 2",
                        ['I'],
                        ['Bribery', 'Evaluate', 'Intuition', 'Lore (Local)', 'Melee (Brawling)', 'Play (Any one)'],
                        ['Dealmaker', 'Embezzle', 'Etiquette (Any one)', 'Gregarious'],
                        "Modest Townhouse, Servant, Quill and Ink"),
            CareerClass("Town Councillor",
                        "Silver 5",
                        ['DEX'],
                        ['Cool', 'Lore (Law)', 'Perception', 'Research'],
                        ['Briber', 'Public Speaker', 'Read/Write', 'Supportive'],
                        "Coach and Driver, Townhouse"),
            CareerClass("Burgomeister",
                        "Gold 1",
                        ['WP'],
                        ['Lore (Politics)', 'Intimidate'],
                        ['Commanding Presence', 'Master Orator', 'Schemer', 'Suave'],
                        "Chains of Office, Coach and Footman, Quality Clothing, Large Townhouse with Gardens and Servants")
        ]


class CareerWatchman:
    def __init__(self):
        self.lvl = [
            CareerClass("Watch Recruit",
                        "Brass 3",
                        ['WS', 'S', 'FEL'],
                        ['Athletics', 'Climb', 'Consume Alcohol', 'Dodge', 'Endurance', 'Gamble', 'Melee (Basic)', 'Perception'],
                        ['Drilled', 'Hardy', 'Strike to Stun', 'Tenacious'],
                        "Hand Weapon, Leather Jack, Uniform"),
            CareerClass("Watchman",
                        "Silver 1",
                        ['WP'],
                        ['Charm', 'Cool', 'Gossip', 'Intimidate', 'Intuition', 'Lore (Local)'],
                        ['Break and Enter', 'Criminal', 'Night Vision', 'Sprinter'],
                        "Lantern and Pole, Lamp Oil, Copper Badge"),
            CareerClass("Watch Sergeant",
                        "Silver 3",
                        ['I'],
                        ['Entertain (Storytelling)', 'Haggle', 'Leadership', 'Lore (Law)'],
                        ['Disarm', 'Etiquette (Soldiers)', 'Fearless (Criminals)', 'Nose for Trouble'],
                        "Breastplate, Helm, Symbol of Rank"),
            CareerClass("Watch Captain",
                        "Gold 1",
                        ['INT'],
                        ['Lore (Politics)', 'Ride (Horse)'],
                        ['Public Speaker', 'Robust', 'Kingpin', 'Schemer'],
                        "Riding Horse with Saddle and Tack, Quality Hat, Quality Hand weapon, Quality Symbol of Rank")
        ]


class CareerAdvisor:
    def __init__(self):
        self.lvl = [
            CareerClass("Aide",
                        "Silver 2",
                        ['T', 'I', 'AG'],
                        ['Bribery', 'Consume Alcohol', 'Endurance', 'Gossip', 'Haggle', 'Language (Classical)', 'Lore (Politics)', 'Perception'],
                        ['Beneath Notice', 'Etiquette (Any one)', 'Gregarious', 'Read/Write'],
                        "Writing Kit"),
            CareerClass("Advisor",
                        "Silver 4",
                        ['FEL'],
                        ['Charm', 'Cool', 'Evaluate', 'Gamble', 'Intuition', 'Lore (Local)'],
                        ['Carouser', 'Criminal', 'Gregarious', 'Nimble Fingered'],
                        "Livery"),
            CareerClass("Counsellor",
                        "Gold 1",
                        ['INT'],
                        ['Entertain (Storytelling)', 'Leadership', 'Language (Any one)', 'Lore (Any one)'],
                        ['Argumentative', 'Briber', 'Carouser', 'Cat-tongued'],
                        "Quality Clothing, Aide"),
            CareerClass("Chancellor",
                        "Gold 3",
                        ['WP'],
                        ['Lore (Heraldry)', 'Ride (Horse)'],
                        ['Commanding Presence', 'Embezzle', 'Kingpin', 'Suave'],
                        "Riding Horse with Saddle and Harness, Quality Courtly Garb, Staff of Advisors and Aides")
        ]


class CareerArtist:
    def __init__(self):
        self.lvl = [
            CareerClass("Apprentice Artist",
                        "Silver 1",
                        ['S', 'I', 'DEX'],
                        ['Art (Any one)', 'Cool', 'Consume Alcohol', 'Evaluate', 'Endurance', 'Gossip', 'Perception', 'Stealth (Urban)'],
                        ['Artistic', 'Sharp', 'Strong Back', 'Tenacious'],
                        "Brush or Chisel or Quill Pen"),
            CareerClass("Artist",
                        "Silver 3",
                        ['FEL'],
                        ['Climb', 'Gamble', 'Haggle', 'Intuition', 'Language (Classical)', 'Sleight of Hand', 'Trade (Art Supplies)'],
                        ['Blather', 'Criminal', 'Schemer', 'Supportive'],
                        "Sling Bag containing Trade Tools (Artist)"),
            CareerClass("Master Artist",
                        "Silver 5",
                        ['WP'],
                        ['Charm', 'Leadership', 'Lore (Art)', 'Lore (Heraldry)'],
                        ['Acute Sense (Any one)', 'Dealmaker', 'Etiquette (Any one)', 'Nose for Trouble'],
                        "Apprentice, Patron, Workshop (Artist)"),
            CareerClass("Maestro",
                        "Gold 2",
                        ['INT'],
                        ['Research', 'Ride (Horse)'],
                        ['Ambidextrous', 'Kingpin', 'Magnum Opus', 'Read/Write'],
                        "Large Workshop (Artist), Library (Art), 3 Apprentices")
        ]


class CareerDuellist:
    def __init__(self):
        self.lvl = [
            CareerClass("Fencer",
                        "Silver 3",
                        ['WS', 'I', 'AG'],
                        ['Athletics', 'Dodge', 'Endurance', 'Heal', 'Intuition', 'Language (Classical)', 'Melee (Any one)', 'Perception'],
                        ['Beat Blade', 'Distract', 'Feint', 'Step Aside'],
                        "Basic Weapon or Rapier, Sling Bag containing Clothing and 1d10 Bandages"),
            CareerClass("Duellist",
                        "Silver 5",
                        ['BS'],
                        ['Charm', 'Cool', 'Gamble', 'Melee (Parry)', 'Ranged (Blackpowder)', 'Trade (Gunsmith)'],
                        ['Combat Reflexes', 'Etiquette (Any one)', 'Fast Shot', 'Reversal'],
                        "Main Gauche or Sword-breaker, Pistol with Gunpowder and Ammunition"),
            CareerClass("Duelmaster",
                        "Gold 1",
                        ['S'],
                        ['Intimidate', 'Leadership', 'Melee (Basic)', 'Perform (Acrobatics)'],
                        ['Ambidextrous', 'Disarm', 'Dual Wielder', 'Riposte'],
                        "Quality Rapier, Hand Weapon, Trusty Second, 2 Wooden Training Swords"),
            CareerClass("Judicial Champion",
                        "Gold 3",
                        ['WP'],
                        ['Lore (Law)', 'Melee (Any one)'],
                        ['Combat Master', 'Menacing', 'Reaction Strike', 'Strike to Injure'],
                        "2 Quality Weapons")
        ]


class CareerEnvoy:
    def __init__(self):
        self.lvl = [
            CareerClass("Herald",
                        "Silver 2",
                        ['T', 'AG', 'FEL'],
                        ['Athletics', 'Charm', 'Drive', 'Dodge', 'Endurance', 'Intuition', 'Ride (Horse)', 'Row'],
                        ['Blather', 'Etiquette (Nobles)', 'Read/Write', 'Suave'],
                        "Leather Jack, Livery, Scroll Case"),
            CareerClass("Envoy",
                        "Silver 4",
                        ['INT'],
                        ['Art (Writing)', 'Bribery', 'Cool', 'Gossip', 'Haggle', 'Lore (Politics)'],
                        ['Attractive', 'Cat-tongued', 'Etiquette (Any one)', 'Seasoned Traveller'],
                        "Quill and Ink, 10 sheets of parchment"),
            CareerClass("Diplomat",
                        "Gold 2",
                        ['I'],
                        ['Intimidate', 'Language (Any one)', 'Leadership', 'Navigation'],
                        ['Carouser', 'Dealmaker', 'Gregarious', 'Schemer'],
                        "Aide, Quality Clothes, Map"),
            CareerClass("Ambassador",
                        "Gold 5",
                        ['WP'],
                        ['Language (Any one)', 'Lore (Any one)'],
                        ['Briber', 'Commanding Presence', 'Noble Blood', 'Savvy'],
                        "Aide, Best Quality Courtly Clothes, Staff of Diplomats, Herald")
        ]


class CareerNoble:
    def __init__(self):
        self.lvl = [
            CareerClass("Scion",
                        "Gold 1",
                        ['WS', 'I', 'DEX'],
                        ['Bribery', 'Consume Alcohol', 'Gamble', 'Intimidate', 'Leadership', 'Lore (Heraldry)', 'Melee (Fencing)', 'Play (Any one)'],
                        ['Etiquette (Nobles)', 'Luck', 'Noble Blood', 'Read/Write'],
                        "Courtly Garb, Foil or Hand Mirror, Jewellery worth 3d10 Gold Coins, Personal Servant"),
            CareerClass("Noble",
                        "Gold 3",
                        ['FEL'],
                        ['Charm', 'Gossip', 'Language (Classical)', 'Lore (Local)', 'Ride (Horse)', 'Melee (Parry)'],
                        ['Attractive', 'Briber', 'Carouser', 'Suave'],
                        "4 Household Servants, Quality Courtly Garb, Courtly Garb, Riding Horse with Saddle and Harness or Coach, Main Gauche or Quality Cloak, Jewellery worth 50 Gold Coins"),
            CareerClass("Magnate",
                        "Gold 5",
                        ['INT'],
                        ['Language (Any one)', 'Intuition', 'Lore (Politics)', 'Perception'],
                        ['Coolheaded', 'Dealmaker', 'Public Speaker', 'Schemer'],
                        "2 sets of Quality Courtly Garb, 200 Gold Coins, Fiefdom, Jewellery worth 200 Gold Coins, Signet Ring"),
            CareerClass("Noble Lord",
                        "Gold 7",
                        ['WP'],
                        ['Lore (Any one)', 'Track'],
                        ['Commanding Presence', 'Iron Will', 'Warleader', 'Wealthy'],
                        "4 sets of Best Quality Courtly Garb, Quality Foil or Hand Mirror, 500 Gold Coins, Jewellery worth 500 Gold Coins, Province")
        ]


class CareerServant:
    def __init__(self):
        self.lvl = [
            CareerClass("Menial",
                        "Silver 1",
                        ['S', 'T', 'AG'],
                        ['Athletics', 'Climb', 'Drive', 'Dodge', 'Endurance', 'Intuition', 'Perception', 'Stealth (Any one)'],
                        ['Beneath Notice', 'Strong Back', 'Strong-minded', 'Sturdy'],
                        "Floor Brush"),
            CareerClass("Servant",
                        "Silver 3",
                        ['I'],
                        ['Animal Care', 'Consume Alcohol', 'Evaluate', 'Gamble', 'Gossip', 'Haggle'],
                        ['Etiquette (Servants)', 'Shadow', 'Tenacious', 'Well-prepared'],
                        "Livery"),
            CareerClass("Attendant",
                        "Silver 5",
                        ['INT'],
                        ['Charm', 'Cool', 'Intimidate', 'Lore (Local)'],
                        ['Embezzle', 'Resistance (Poison)', 'Suave', 'Supportive'],
                        "Quality Livery, Storm Lantern, Tinderbox, Lamp Oil"),
            CareerClass("Steward",
                        "Gold 1",
                        ['FEL'],
                        ['Leadership', 'Melee (Basic)'],
                        ['Etiquette (Any one)', 'Numismatics', 'Read/Write', 'Savvy'],
                        "Hand Weapon, Fine Clothes, Servant")
        ]


class CareerSpy:
    def __init__(self):
        self.lvl = [
            CareerClass("Informer",
                        "Brass 3",
                        ['AG', 'WP', 'FEL'],
                        ['Bribery', 'Charm', 'Cool', 'Gamble', 'Gossip', 'Haggle', 'Perception', 'Stealth (Any one)'],
                        ['Blather', 'Carouser', 'Gregarious', 'Shadow'],
                        "Charcoal Stick, Sling Bag with 2 different sets of clothing and Hooded Cloak"),
            CareerClass("Spy",
                        "Silver 3",
                        ['WS'],
                        ['Climb', 'Entertain (Act)', 'Intuition', 'Melee (Basic)', 'Secret Signs (Any one)', 'Sleight of Hand'],
                        ['Etiquette (Any one)', 'Lip Reading', 'Read/Write', 'Secret Identity'],
                        "Informer, Hand Weapon, Disguise Kit, Ring of Informers, Telescope"),
            CareerClass("Agent",
                        "Gold 1",
                        ['I'],
                        ['Animal Care', 'Animal Training (Pigeon)', 'Language (Any one)', 'Leadership'],
                        ['Attractive', 'Cat-tongued', 'Master of Disguise', 'Mimic'],
                        "Book (Cryptography), Ring of Spies and Informers, Loft of Homing Pigeons, Quill and Ink"),
            CareerClass("Spymaster",
                        "Gold 4",
                        ['INT'],
                        ['Lore (Any one)', 'Research'],
                        ['Briber', 'Schemer', 'Suave', 'Tower of Memories'],
                        "Office and Staff, Large Spy Ring of Agents, Spies, and Informers")
        ]


class CareerWarden:
    def __init__(self):
        self.lvl = [
            CareerClass("Custodian",
                        "Silver 1",
                        ['S', 'T', 'WP'],
                        ['Athletics', 'Charm Animal', 'Consume Alcohol', 'Cool', 'Endurance', 'Intuition', 'Perception', 'Trade (Any one)'],
                        ['Menacing', 'Night Vision', 'Sharp', 'Strike to Stun'],
                        "Keys, Lantern, Lamp Oil, Livery"),
            CareerClass("Warden",
                        "Silver 3",
                        ['WS'],
                        ['Animal Care', 'Melee (Basic)', 'Outdoor Survival', 'Ranged (Bow)', 'Ride (Horse)', 'Swim'],
                        ['Animal Affinity', 'Etiquette (Servants)', 'Strider (Any one)', 'Rover'],
                        "Hand Weapon or Bow with 10 arrows, Riding Horse with Saddle and Harness, Leather Jack"),
            CareerClass("Seneschal",
                        "Gold 1",
                        ['FEL'],
                        ['Bribery', 'Charm', 'Gossip', 'Leadership'],
                        ['Embezzle', 'Numismatics', 'Read/Write', 'Supportive'],
                        "Breastplate, Ceremonial Staff of Office, Staff of Wardens and Custodians"),
            CareerClass("Governor",
                        "Gold 3",
                        ['INT'],
                        ['Evaluate', 'Language (Any one)'],
                        ['Commanding Presence', 'Etiquette (Any one)', 'Savant (local)', 'Suave'],
                        "Aide, Governor’s Residence, Servant")
        ]


class CareerBailiff:
    def __init__(self):
        self.lvl = [
            CareerClass("Tax Collector",
                        "Silver 1",
                        ['WS', 'I', 'WP'],
                        ['Cool', 'Dodge', 'Endurance', 'Gossip', 'Haggle', 'Intimidate', 'Melee (Basic)', 'Perception'],
                        ['Embezzle', 'Numismatics', 'Strong Back', 'Tenacious'],
                        "Hand Weapon, Small Lock Box"),
            CareerClass("Bailiff",
                        "Silver 5",
                        ['FEL'],
                        ['Bribery', 'Charm', 'Evaluate', 'Intuition', 'Leadership', 'Lore (Local)'],
                        ['Break and Enter', 'Criminal', 'Public Speaker', 'Strike to Stun'],
                        "Leather Jack, 3 Tax Collectors"),
            CareerClass("Reeve",
                        "Gold 1",
                        ['AG'],
                        ['Animal Care', 'Lore (Heraldry)', 'Navigation', 'Ride (Horse)'],
                        ['Kingpin', 'Menacing', 'Nose for Trouble', 'Read/Write'],
                        "Horse with Saddle and Tack, Breastplate, Bailiff"),
            CareerClass("Magistrate",
                        "Gold 3",
                        ['INT'],
                        ['Language (Classical)', 'Lore (Law)'],
                        ['Commanding Presence', 'Iron Will', 'Savvy', 'Schemer'],
                        "Library (Law), Quality Robes, Seal of Office")
        ]


class CareerHedgeWitch:
    def __init__(self):
        self.lvl = [
            CareerClass("Hedge Apprentice",
                        "Brass 1",
                        ['T', 'I', 'DEX'],
                        ['Channelling', 'Endurance', 'Intuition', 'Lore (Folklore)', 'Lore (Herbs)', 'Outdoor Survival', 'Perception', 'Trade (Charms)'],
                        ['Fast Hands', 'Petty Magic', 'Rover', 'Strider (Woodlands)'],
                        "d10 Lucky Charms, Quarterstaff, Backpack"),
            CareerClass("Hedge Witch",
                        "Brass 2",
                        ['INT'],
                        ['Cool', 'Gossip', 'Heal', 'Lore (Local)', 'Trade (Charms)', 'Trade (Herbalist)'],
                        ['Aethyric Attunement', 'Animal Affinity', 'Arcane Magic (Hedgecraft)', 'Sixth Sense'],
                        "Antitoxin Kit, Healing Poultice, Trade Tools (Herbalist)"),
            CareerClass("Hedge Master",
                        "Brass 3",
                        ['FEL'],
                        ['Haggle', 'Lore (Genealogy)', 'Lore (Magic)', 'Lore (Spirits)'],
                        ['Craftsman (Herbalist)', 'Magical Sense', 'Pure Soul', 'Resistance (Disease)'],
                        "Isolated Hut, Apprentice"),
            CareerClass("Hedgewise",
                        "Brass 5",
                        ['WP'],
                        ['Intimidate', 'Pray'],
                        ['Acute Sense (Any one)', 'Master Craftsman (Herbalist)', 'Night Vision', 'Strong-minded'],
                        "Assortment of Animal Skulls, Ceremonial Cloak and Garland")
        ]


class CareerHerbalist:
    def __init__(self):
        self.lvl = [
            CareerClass("Herb Gatherer",
                        "Brass 2",
                        ['T', 'I', 'AG'],
                        ['Charm Animal', 'Climb', 'Endurance', 'Lore (Herbs)', 'Outdoor Survival', 'Perception', 'Swim', 'Trade (Herbalist)'],
                        ['Acute Sense (Taste)', 'Orientation', 'Rover', 'Strider (Any one)'],
                        "Boots, Cloak, Sling Bag containing an Assortment of Herbs"),
            CareerClass("Herbalist",
                        "Brass 4",
                        ['DEX'],
                        ['Consume Alcohol', 'Cool', 'Gossip', 'Haggle', 'Heal', 'Lore (Local)'],
                        ['Dealmaker', 'Nimble Fingered', 'Sharp', 'Sturdy'],
                        "Hand Weapon (Sickle), Healing Poultice, Trade Tools (Herbalist)"),
            CareerClass("Herb Master",
                        "Silver 1",
                        ['FEL'],
                        ['Intuition', 'Leadership', 'Lore (Medicine)', 'Trade (Poisons)'],
                        ['Craftsman (Herbalist)', 'Field Dressing', 'Hardy', 'Savvy'],
                        "Herb Gatherer, 3 Healing Poultices, Healing Draught, Workshop (Herbalist)"),
            CareerClass("Herbwise",
                        "Silver 3",
                        ['INT'],
                        ['Drive', 'Navigation'],
                        ['Concoct', 'Master Tradesman (Herbalist)', 'Resistance (Poison)', 'Savant (Herbs)'],
                        "Pony and Cart")
        ]


class CareerHunter:
    def __init__(self):
        self.lvl = [
            CareerClass("Trapper",
                        "Brass 2",
                        ['S', 'T', 'DEX'],
                        ['Charm Animal', 'Climb', 'Endurance', 'Lore (Beasts)', 'Outdoor Survival', 'Perception', 'Ranged (Sling)', 'Set Trap'],
                        ['Hardy', 'Rover', 'Strider (Any one)', 'Trapper'],
                        "Selection of Animal Traps, Hand Weapon, Sling with 10 Stone Bullets, Sturdy Boots and Cloak"),
            CareerClass("Hunter",
                        "Brass 4",
                        ['BS'],
                        ['Cool', 'Intuition', 'Melee (Basic)', 'Ranged (Sling)', 'Secret Signs (Hunter)', 'Stealth (Rural)'],
                        ['Accurate Shot', 'Fast Shot', 'Hunter’s Eye', 'Marksman'],
                        "Bow with 10 arrows, Sling with Ammunition"),
            CareerClass("Tracker",
                        "Silver 1",
                        ['I'],
                        ['Navigation', 'Ride (Horse)', 'Swim', 'Track'],
                        ['Acute Sense (Any one)', 'Deadeye Shot', 'Fearless (Animals)', 'Sharpshooter'],
                        "Backpack, Bedroll, Tent"),
            CareerClass("Huntsmaster",
                        "Silver 3",
                        ['INT'],
                        ['Animal Care', 'Animal Training (Any one)'],
                        ['Fearless (Monsters)', 'Robust', 'Sniper', 'Sure Shot'],
                        "Riding Horse with Saddle and Tack, Kennel of Hunting Dogs")
        ]


class CareerMiner:
    def __init__(self):
        self.lvl = [
            CareerClass("Prospector",
                        "Brass 2",
                        ['S', 'T', 'WP'],
                        ['Cool', 'Endurance', 'Intuition', 'Lore (Local)', 'Melee (Two-handed)', 'Outdoor Survival', 'Perception', 'Swim'],
                        ['Rover', 'Strider (Rocky)', 'Sturdy', 'Tenacious'],
                        "Charcoal Stick, Crude Map, Pan, Spade"),
            CareerClass("Miner",
                        "Brass 4",
                        ['WS'],
                        ['Climb', 'Consume Alcohol', 'Evaluate', 'Melee (Basic)', 'Secret Signs (Miner)', 'Trade (Explosives)'],
                        ['Night Vision', 'Strike Mighty Blow', 'Strong Back', 'Very Strong'],
                        "Davrich Lamp, Hand Weapon (Pick), Lamp Oil, Leather Jack"),
            CareerClass("Master Miner",
                        "Brass 5",
                        ['I'],
                        ['Gossip', 'Lore (Geology)', 'Stealth (Underground)', 'Trade (Engineer)'],
                        ['Careful Strike', 'Craftsman (Explosives)', 'Tinker', 'Tunnel Rat'],
                        "Great Weapon (Two-handed Pick), Helmet, Trade Tools (Engineer)"),
            CareerClass("Mine Foreman",
                        "Silver 4",
                        ['FEL'],
                        ['Charm', 'Leadership'],
                        ['Argumentative', 'Strong-minded', 'Embezzle', 'Read/Write'],
                        "Crew of Miners, Writing Kit")
        ]


class CareerMystic:
    def __init__(self):
        self.lvl = [
            CareerClass("Fortune Teller",
                        "Brass 1",
                        ['I', 'DEX', 'FEL'],
                        ['Charm', 'Entertain (Fortune Telling)', 'Dodge', 'Gossip', 'Haggle', 'Intuition', 'Perception', 'Sleight of Hand'],
                        ['Attractive', 'Luck', 'Second Sight', 'Suave'],
                        "Deck of Cards or Set of Dice, Chep Jewellery"),
            CareerClass("Mystic",
                        "Brass 2",
                        ['WP'],
                        ['Bribery', 'Cool', 'Entertain (Prophecy)', 'Evaluate', 'Intimidate', 'Lore (Astrology)'],
                        ['Detect Artefact', 'Holy Visions', 'Sixth Sense', 'Well-prepared'],
                        "Selection of Amulets"),
            CareerClass("Sage",
                        "Brass 3",
                        ['AG'],
                        ['Charm Animal', 'Entertain (Storytelling)', 'Language (Any one)', 'Trade (Writing)'],
                        ['Nose for Trouble', 'Petty Magic', 'Read/Write', 'Witch!'],
                        "Trade Tools (Writing)"),
            CareerClass("Seer",
                        "Brass 4",
                        ['INT'],
                        ['Lore (Prophecy)', 'Channelling (Azyr)'],
                        ['Arcane Magic (Celestial)', 'Magical Sense', 'Menacing', 'Strong-minded'],
                        "Trade Tools (Astrology)")
        ]


class CareerScout:
    def __init__(self):
        self.lvl = [
            CareerClass("Guide",
                        "Brass 3",
                        ['T', 'I', 'AG'],
                        ['Charm Animal', 'Climb', 'Endurance', 'Gossip', 'Lore (Local)', 'Melee (Basic)', 'Outdoor Survival', 'Perception'],
                        ['Orientation', 'Rover', 'Sharp', 'Strider (Any one)'],
                        "Hand Weapon, Leather Jack, Sturdy Boots and Cloak, Rope"),
            CareerClass("Scout",
                        "Brass 5",
                        ['BS'],
                        ['Athletics', 'Navigation', 'Ranged (Bow)', 'Ride (Horse)', 'Stealth (Rural)', 'Track'],
                        ['Combat Aware', 'Night Vision', 'Nose for Trouble', 'Seasoned Traveller'],
                        "Bow and 10 Arrows, Mail Shirt"),
            CareerClass("Pathfinder",
                        "Silver 1",
                        ['INT'],
                        ['Animal Care', 'Haggle', 'Secret Signs (Hunter)', 'Swim'],
                        ['Acute Sense (Sight)', 'Sixth Sense', 'Strong Legs', 'Very Resilient'],
                        "Map, Riding Horse with Saddle and Tack, Saddlebags with 2 weeks’ Rations, Tent"),
            CareerClass("Explorer",
                        "Silver 5",
                        ['DEX'],
                        ['Language (Any one)', 'Trade (Cartographer)'],
                        ['Hardy', 'Linguistics', 'Savant (Local)', 'Tenacious'],
                        "Selection of Maps, Trade Tools (Cartographer)")
        ]


class CareerVillager:
    def __init__(self):
        self.lvl = [
            CareerClass("Peasant",
                        "Brass 2",
                        ['S', 'T', 'AG'],
                        ['Animal Care', 'Athletics', 'Consume Alcohol', 'Endurance', 'Gossip', 'Melee (Brawling)', 'Lore (Local)', 'Outdoor Survival'],
                        ['Rover', 'Strong Back', 'Strong-minded', 'Stone Soup'],
                        "-"),
            CareerClass("Villager",
                        "Brass 3",
                        ['WS'],
                        ['Drive', 'Entertain (Storytelling)', 'Haggle', 'Melee (Basic)', 'Trade (Any one)'],
                        ['Animal Affinity', 'Hardy', 'Tenacious', 'Very Strong'],
                        "Leather Jerkin, Hand Weapon (Axe), Trade Tools (as Trade)"),
            CareerClass("Councillor",
                        "Brass 4",
                        ['FEL'],
                        ['Bribery', 'Charm', 'Intimidate', 'Leadership'],
                        ['Craftsman (Any one)', 'Dealmaker', 'Stout-hearted', 'Very Resilient'],
                        "Mule and Cart, Village Home and Workshop"),
            CareerClass("Village Elder",
                        "Silver 2",
                        ['INT'],
                        ['Intuition', 'Lore (History)'],
                        ['Master Tradesman (Any one)', 'Nimble Fingered', 'Public Speaker', 'Savant (Local)'],
                        "The Respect of the Village")
        ]


class CareerBountyHunter:
    def __init__(self):
        self.lvl = [
            CareerClass("Thief-taker",
                        "Silver 1",
                        ['WS', 'T', 'AG'],
                        ['Bribery', 'Charm', 'Gossip', 'Haggle', 'Intuition', 'Melee (Basic)', 'Outdoor Survival', 'Perception'],
                        ['Break and Enter', 'Shadow', 'Strike to Stun', 'Suave'],
                        "Hand Weapon, Leather Jerkin, Rope"),
            CareerClass("Bounty Hunter",
                        "Silver 3",
                        ['BS'],
                        ['Athletics', 'Endurance', 'Intimidate', 'Ranged (Crossbow)', 'Ranged (Entangling)', 'Track'],
                        ['Marksman', 'Relentless', 'Seasoned Traveller', 'Strong Back'],
                        "Crossbow and 10 bolts, Leather Skullcap, Manacles, Net, Warrant Papers"),
            CareerClass("Master Bounty Hunter",
                        "Silver 5",
                        ['S'],
                        ['Animal Care', 'Climb', 'Ride (Horse)', 'Swim'],
                        ['Accurate Shot', 'Careful Strike', 'Dual Wielder', 'Sprinter'],
                        "Mail Shirt, Riding Horse and Saddle"),
            CareerClass("Bounty Hunter General",
                        "Gold 1",
                        ['INT'],
                        ['Drive', 'Lore (Law)'],
                        ['Deadeye Shot', 'Fearless (Bounties)', 'Hardy', 'Sure Shot'],
                        "Draught Horse and Cart, Mail Shirt, 4 Pairs of Manacles")
        ]


class CareerCoachman:
    def __init__(self):
        self.lvl = [
            CareerClass("Postilion",
                        "Silver 1",
                        ['BS', 'T', 'WP'],
                        ['Animal Care', 'Charm Animal', 'Climb', 'Drive', 'Endurance', 'Perception', 'Ranged (Entangling)', 'Ride (Horse)'],
                        ['Animal Affinity', 'Seasoned Traveller', 'Trick Riding', 'Tenacious'],
                        "Warm Coat and Gloves, Whip"),
            CareerClass("Coachman",
                        "Silver 2",
                        ['AG'],
                        ['Consume Alcohol', 'Gossip', 'Intuition', 'Lore (Local)', 'Navigation', 'Ranged (Blackpowder)'],
                        ['Coolheaded', 'Crack the Whip', 'Gunner', 'Strong-minded'],
                        "Blunderbuss with 10 Shots, Coach Horn, Leather Jack, Hat	,  	Costume, Instrument, Selection of Scripts (that you can’t yet read), Throwing Weapons"),
            CareerClass("Coach Master",
                        "Silver 3",
                        ['WS'],
                        ['Animal Training (Horse)', 'Intimidate', 'Language (Any one)', 'Lore (Routes)'],
                        ['Accurate Shot', 'Dealmaker', 'Fearless (Outlaws)', 'Nose for Trouble'],
                        "Mail Shirt, Pistol, Quality Cloak"),
            CareerClass("Route Master",
                        "Silver 5",
                        ['I'],
                        ['Charm', 'Leadership'],
                        ['Fearless (Beastmen)', 'Marksman', 'Orientation', 'Rapid Reload'],
                        "Fleet of Coaches and Horses, Maps")
        ]


class CareerEntertainer:
    def __init__(self):
        self.lvl = [
            CareerClass("Busker",
                        "Brass 3",
                        ['AG', 'DEX', 'FEL'],
                        ['Athletics', 'Charm', 'Entertain (Any one)', 'Gossip', 'Haggle', 'Perform (Any one)', 'Play (Any one)', 'Sleight of Hand'],
                        ['Attractive', 'Mimic', 'Public Speaker', 'Suave'],
                        "Bowl, Instrument"),
            CareerClass("Entertainer",
                        "Brass 5",
                        ['WS'],
                        ['Entertain (Any one)', 'Ride (Any one)', 'Melee (Basic)', 'Perform (Any one)', 'Play (Any one) Ranged (Throwing)'],
                        ['Contortionist', 'Jump Up', 'Sharpshooter', 'Trick Riding'],
                        "Costume, Instrument, Selection of Scripts (that you can’t yet read), Throwing Weapons"),
            CareerClass("Troubadour",
                        "Silver 3",
                        ['BS'],
                        ['Animal Care', 'Animal Training', 'Art (Writing)', 'Language (Any one)'],
                        ['Blather', 'Master of Disguise', 'Perfect Pitch', 'Read/Write'],
                        "Trained Animal, Writing Kit"),
            CareerClass("Troupe Leader",
                        "Gold 1",
                        ['T'],
                        ['Drive', 'Leadership'],
                        ['Dealmaker', 'Etiquette (Any one)', 'Seasoned Traveller', 'Sharp'],
                        "Draught Horses and Wagon (Stage), Wardrobe of Costumes and Props, Troupe of Entertainers")
        ]


class CareerFlagellant:
    def __init__(self):
        self.lvl = [
            CareerClass("Zealot",
                        "Brass 0",
                        ['WS', 'S', 'T'],
                        ['Dodge', 'Endurance', 'Heal', 'Intimidate', 'Intuition', 'Lore (Theology)', 'Melee (Flail)', 'Outdoor Survival'],
                        ['Berserk Charge', 'Frenzy', 'Read/Write', 'Stone Soup'],
                        "Flail, Tattered Robes"),
            CareerClass("Flagellant",
                        "Brass 0",
                        ['WP'],
                        ['Art (Icons)', 'Athletics', 'Cool', 'Language (Classical)', 'Lore (The Empire)', 'Ranged (Sling)'],
                        ['Hardy', 'Hatred (Heretics)', 'Flagellant', 'Implacable'],
                        "Placard, Religious Symbol, Sling"),
            CareerClass("Penitent",
                        "Brass 0",
                        ['I'],
                        ['Charm', 'Language (Any one)', 'Lore (Theology)', 'Perception'],
                        ['Field Dressing', 'Furious Assault', 'Menacing', 'Seasoned Traveller'],
                        "Religious Relic"),
            CareerClass("Prophet of Doom",
                        "Brass 0",
                        ['FEL'],
                        ['Entertain (Speeches)', 'Leadership'],
                        ['Battle Rage', 'Fearless (Heretics)', 'Frightening', 'Impassioned Zeal'],
                        "Book (Religion), Followers (including Penitents, Flagellants and Zealots)")
        ]


class CareerMessenger:
    def __init__(self):
        self.lvl = [
            CareerClass("Runner",
                        "Brass 3",
                        ['T', 'I', 'AG'],
                        ['Athletics', 'Climb', 'Dodge', 'Endurance', 'Gossip', 'Navigation', 'Perception', 'Melee (Brawling)'],
                        ['Flee', 'Fleet Footed', 'Sprinter', 'Step Aside'],
                        "Scroll Case"),
            CareerClass("Messenger",
                        "Silver 1",
                        ['WS'],
                        ['Animal Care', 'Charm', 'Cool', 'Lore (Local)', 'Melee (Basic)', 'Ride (Horse)'],
                        ['Crack the Whip', 'Criminal', 'Orientation', 'Seasoned Traveller'],
                        "Hand Weapon, Leather Jack, Riding Horse with Saddle and Tack"),
            CareerClass("Courier",
                        "Silver 3",
                        ['WP'],
                        ['Charm Animal', 'Bribery', 'Consume Alcohol', 'Outdoor Survival'],
                        ['Nose for Trouble', 'Relentless', 'Tenacious', 'Trick Riding'],
                        "Backpack, Saddlebags, Shield"),
            CareerClass("Courier-Captain",
                        "Silver 5",
                        ['FEL'],
                        ['Intimidate', 'Leadership'],
                        ['Dealmaker', 'Hatred (Outlaws)', 'Kingpin', 'Very Resilient'],
                        "Couriers, Mail Shirt, Writing Kit")
        ]


class CareerPedlar:
    def __init__(self):
        self.lvl = [
            CareerClass("Vagabond",
                        "Brass 1",
                        ['T', 'DEX', 'WP'],
                        ['Charm', 'Endurance', 'Entertain (Storytelling)', 'Gossip', 'Haggle', 'Intuition', 'Outdoor Survival', 'Stealth (Rural or Urban)'],
                        ['Fisherman', 'Flee', 'Rover', 'Tinker'],
                        "Backpack, Bedroll, Goods worth 2d10 Brass Coins, Tent"),
            CareerClass("Pedlar",
                        "Brass 4",
                        ['FEL'],
                        ['Animal Care', 'Charm Animal', 'Consume Alcohol', 'Evaluate', 'Ride (Horse)', 'Trade (Tinker)'],
                        ['Dealmaker', 'Orientation', 'Seasoned Traveller', 'Strong Back'],
                        "Mule and Saddlebags, Goods worth 2d10 Silver Coins, Selection of Pots and Pans, Trade Tools (Tinker)"),
            CareerClass("Master Pedlar",
                        "Silver 1",
                        ['I'],
                        ['Drive', 'Intimidate', 'Language (Any one)', 'Perception'],
                        ['Numismatics', 'Sharp', 'Sturdy', 'Well-prepared', 'Very Resilient'],
                        "Cart, Goods worth at least 2d10 Gold Coins"),
            CareerClass("Wandering Trader",
                        "Silver 3",
                        ['INT'],
                        ['Lore (Local)', 'Lore (Geography)'],
                        ['Cat-tongued', 'Strong-minded', 'Suave', 'Tenacious'],
                        "Draught Horse and Wagon, Goods worth at least 5d10 Gold Coins, 50 Silver Coins")
        ]


class CareerRoadwarden:
    def __init__(self):
        self.lvl = [
            CareerClass("Toll Keeper",
                        "Brass 5",
                        ['BS', 'T', 'I'],
                        ['Bribery', 'Consume Alcohol', 'Gamble', 'Gossip', 'Haggle', 'Melee (Basic)', 'Perception', 'Ranged (Crossbow)'],
                        ['Coolheaded', 'Embezzle', 'Marksman', 'Numismatics'],
                        "Crossbow with 10 Bolts, Leather Jack"),
            CareerClass("Roadwarden",
                        "Silver 2",
                        ['WS'],
                        ['Animal Care', 'Endurance', 'Intimidate', 'Intuition', 'Outdoor Survival', 'Ride (Horse)'],
                        ['Crack the Whip', 'Criminal', 'Roughrider', 'Seasoned Traveller'],
                        "Hand Weapon, Mail Shirt, Riding Horse with Saddle and Harness, Rope"),
            CareerClass("Road Sergeant",
                        "Silver 4",
                        ['FEL'],
                        ['Athletics', 'Charm', 'Leadership', 'Ranged (Blackpowder)'],
                        ['Etiquette (Soldiers)', 'Fearless (Outlaws)', 'Hatred (Any one)', 'Nose for Trouble'],
                        "Squad of Roadwardens, Pistol with 10 Shots, Shield, Symbol of Rank"),
            CareerClass("Road Captain",
                        "Gold 1",
                        ['INT'],
                        ['Lore (Empire)', 'Navigation'],
                        ['Combat Aware', 'Commanding Presence', 'Kingpin', 'Public Speaker'],
                        "Light Warhorse, Pistol with 10 Shots, Quality Hat and Cloak, Unit of Roadwardens")
        ]


class CareerWitchHunter:
    def __init__(self):
        self.lvl = [
            CareerClass("Interrogator",
                        "Silver 1",
                        ['WS', 'T', 'WP'],
                        ['Charm', 'Consume Alcohol', 'Heal', 'Intimidate', 'Intuition', 'Lore (Torture)', 'Melee (Basic)', 'Perception'],
                        ['Coolheaded', 'Menacing', 'Read/Write', 'Resolute'],
                        "Hand Weapon, Instruments of Torture"),
            CareerClass("Witch Hunter",
                        "Silver 3",
                        ['BS'],
                        ['Cool', 'Dodge', 'Gossip', 'Lore (Witches)', 'Ranged (Any one)', 'Ride (Horse)'],
                        ['Dual Wielder', 'Marksman', 'Seasoned Traveller', 'Shadow'],
                        "Crossbow Pistol or Pistol, Hat (Henin), Leather Jack, Riding Horse with Saddle and Tack, Rope, Silvered Sword"),
            CareerClass("Inquisitor",
                        "Silver 5",
                        ['FEL'],
                        ['Endurance', 'Leadership', 'Lore (Law)', 'Lore (Local)'],
                        ['Fearless (Witches)', 'Nose for Trouble', 'Relentless', 'Strong-minded'],
                        "Quality Clothing, Subordinate Interrogators"),
            CareerClass("Witchfinder General",
                        "Gold 1",
                        ['INT'],
                        ['Lore (Chaos)', 'Lore (Politics)'],
                        ['Frightening', 'Iron Will', 'Magical Sense', 'Pure Soul'],
                        "Best Quality Courtly Garb, Subordinate Witch Hunters")
        ]


class CareerBoatman:
    def __init__(self):
        self.lvl = [
            CareerClass("Boat-hand",
                        "Silver 1",
                        ['S', 'T', 'AG'],
                        ['Consume Alcohol', 'Dodge', 'Endurance', 'Gossip', 'Melee (Basic)', 'Row', 'Sail', 'Swim'],
                        ['Dirty Fighting', 'Fisherman', 'Strong Back', 'Strong Swimmer'],
                        "Hand Weapon (Boat Hook), Leather Jack, Pole"),
            CareerClass("Boatman",
                        "Silver 2",
                        ['I'],
                        ['Athletics', 'Entertain (Storytelling)', 'Haggle', 'Intuition', 'Lore (Riverways)', 'Perception'],
                        ['Etiquette (Guilder)', 'Seasoned Traveller', 'Very Strong', 'Waterman'],
                        "Rope, Rowboat"),
            CareerClass("Bargeswain",
                        "Silver 3",
                        ['DEX'],
                        ['Climb', 'Entertain (Singing)', 'Heal', 'Trade (Boatbuilding)'],
                        ['Dealmaker', 'Embezzle', 'Nose for Trouble', 'Strike Mighty Blow'],
                        "Backpack, Trade Tools (Carpenter)"),
            CareerClass("Barge Master",
                        "Silver 5",
                        ['INT'],
                        ['Leadership', 'Navigation'],
                        ['Menacing', 'Orientation', 'Pilot', 'Public Speaker'],
                        "Hat, Riverboat and Crew")
        ]


class CareerHuffer:
    def __init__(self):
        self.lvl = [
            CareerClass("Riverguide",
                        "Brass 4",
                        ['WS', 'T', 'I'],
                        ['Consume Alcohol', 'Gossip', 'Intuition', 'Lore (Local)', 'Lore (Riverways)', 'Perception', 'Row', 'Swim'],
                        ['Fisherman', 'Night Vision', 'Orientation', 'Waterman'],
                        "Hand Weapon (Boat Hook), Storm Lantern and Oil"),
            CareerClass("Huffer",
                        "Silver 1",
                        ['WP'],
                        ['Charm', 'Cool', 'Entertain (Storytelling)', 'Language (Any one)', 'Melee (Basic)', 'Navigation'],
                        ['Dealmaker', 'Etiquette (Guilder)', 'Nose for Trouble', 'River Guide'],
                        "Leather Jerkin, Rope, Row Boat"),
            CareerClass("Pilot",
                        "Silver 3",
                        ['INT'],
                        ['Haggle', 'Intimidate', 'Lore (Local)', 'Lore (Wrecks)'],
                        ['Acute Sense (Sight)', 'Pilot', 'Sea Legs', 'Very Strong'],
                        "Pole, Storm Lantern and Oil"),
            CareerClass("Master Pilot",
                        "Silver 5",
                        ['FEL'],
                        ['Leadership', 'Sail'],
                        ['Sixth Sense', 'Sharp', 'Strong Swimmer', 'Tenacious'],
                        "Boathand, Small Riverboat")
        ]


class CareerRiverwarden:
    def __init__(self):
        self.lvl = [
            CareerClass("River Recruit",
                        "Silver 1",
                        ['BS', 'S', 'FEL'],
                        ['Athletics', 'Dodge', 'Endurance', 'Melee (Basic)', 'Perception', 'Row', 'Sail', 'Swim'],
                        ['Strong Swimmer', 'Strong Back', 'Very Strong', 'Waterman'],
                        "Hand Weapon (Sword), Leather Jack, Uniform"),
            CareerClass("Riverwarden",
                        "Silver 2",
                        ['WS'],
                        ['Bribery', 'Charm', 'Intimidate', 'Gossip', 'Lore (Riverways)', 'Ranged (Blackpowder)'],
                        ['Criminal', 'Gunner', 'Fisherman', 'Seasoned Traveller'],
                        "Lantern and Oil, Pistol with 10 shot, Shield"),
            CareerClass("Shipsword",
                        "Silver 4",
                        ['I'],
                        ['Climb', 'Cool', 'Intuition', 'Leadership'],
                        ['Fearless (Wreckers)', 'Hatred (Any one)', 'Pilot', 'Sea Legs'],
                        "Grappling Hook, Helmet, Mail Shirt"),
            CareerClass("Shipsword Master",
                        "Gold 1",
                        ['INT'],
                        ['Lore (Law)', 'Navigation'],
                        ['Commanding Presence', 'Kingpin', 'Menacing', 'Orientation'],
                        "Patrol Boats and Crew, Symbol of Rank")
        ]


class CareerRiverwoman:
    def __init__(self):
        self.lvl = [
            CareerClass("Greenfish",
                        "Brass 2",
                        ['T', 'AG', 'DEX'],
                        ['Athletics', 'Consume Alcohol', 'Dodge', 'Endurance', 'Gossip', 'Outdoor Survival', 'Row', 'Swim'],
                        ['Fisherman', 'Gregarious', 'Strider (Marshes)', 'Strong Swimmer'],
                        "Bucket, Fishing Rod and Bait, Leather Leggings"),
            CareerClass("Riverwoman",
                        "Brass 3",
                        ['WS'],
                        ['Gamble', 'Lore (Local)', 'Lore (Riverways)', 'Ranged (Entangling)', 'Ranged (Throwing)', 'Set Trap'],
                        ['Craftsman (Boatbuilder)', 'Rover', 'Strong Back', 'Waterman'],
                        "Eel Trap, Leather Jerkin, Net, Spear"),
            CareerClass("Riverwise",
                        "Brass 5",
                        ['I'],
                        ['Charm', 'Intuition', 'Melee (Polearm)', 'Perception'],
                        ['Savant (Riverways)', 'Stout-hearted', 'Tenacious', 'Very Strong'],
                        "Row Boat, Storm Lantern and Oil"),
            CareerClass("River Elder",
                        "Silver 2",
                        ['FEL'],
                        ['Entertain (Storytelling)', 'Lore (Folklore)'],
                        ['Master Craftsman (Boatbuilder)', 'Public Speaker', 'Sharp', 'Strong-minded'],
                        "Hut or Riverboat")
        ]


class CareerSeaman:
    def __init__(self):
        self.lvl = [
            CareerClass("Landsman",
                        "Silver 1",
                        ['AG', 'DEX', 'FEL'],
                        ['Climb', 'Consume Alcohol', 'Gamble', 'Gossip', 'Row', 'Melee (Brawling)', 'Sail', 'Swim'],
                        ['Fisherman', 'Strider (Coastal)', 'Strong Back', 'Strong Swimmer'],
                        "Bucket, Brush, Mop"),
            CareerClass("Seaman",
                        "Silver 3",
                        ['WS'],
                        ['Athletics', 'Dodge', 'Endurance', 'Entertain (Singing)', 'Language (Any one)', 'Melee (Basic)'],
                        ['Catfall', 'Sea Legs', 'Seasoned Traveller', 'Strong Legs'],
                        "Hand Weapon (Boat Hook), Leather Jerkin"),
            CareerClass("Boatswain",
                        "Silver 5",
                        ['I'],
                        ['Cool', 'Leadership', 'Perception', 'Trade (Carpenter)'],
                        ['Old Salt', 'Strike Mighty Blow', 'Tenacious', 'Very Strong'],
                        "Trade Tools (Carpenter)"),
            CareerClass("Ship’s Master",
                        "Gold 2",
                        ['INT'],
                        ['Charm', 'Navigation'],
                        ['Orientation', 'Pilot', 'Public Speaker', 'Savvy'],
                        "Shipping Charts, Sailing Ship and Crew, Sextant, Spyglass")
        ]


class CareerSmuggler:
    def __init__(self):
        self.lvl = [
            CareerClass("River Runner",
                        "Brass 2",
                        ['AG', 'DEX', 'WP'],
                        ['Athletics', 'Bribery', 'Cool', 'Consume Alcohol', 'Row', 'Sail', 'Stealth (Rural or Urban)', 'Swim'],
                        ['Criminal', 'Fisherman', 'Strider (Marshes)', 'Strong Back'],
                        "Large Sack, Mask or Scarves, Tinderbox, Storm Lantern and Oil"),
            CareerClass("Smuggler",
                        "Brass 3",
                        ['I'],
                        ['Haggle', 'Charm', 'Gossip', 'Lore (Local)', 'Melee (Basic)', 'Perception', 'Secret Signs (Smuggler)'],
                        ['Dealmaker', 'Etiquette (Criminals)', 'Waterman', 'Very Strong'],
                        "2 Barrels, Hand Weapon, Leather Jack, Row Boat"),
            CareerClass("Master Smuggler",
                        "Brass 5",
                        ['INT'],
                        ['Evaluate', 'Intimidate', 'Intuition', 'Lore (Riverways)'],
                        ['Briber', 'Fearless (Riverwardens)', 'Pilot', 'Strong Swimmer'],
                        "River Runner, Speedy Riverboat"),
            CareerClass("Smuggler King",
                        "Silver 2",
                        ['FEL'],
                        ['Language (Any one)', 'Leadership'],
                        ['Kingpin', 'Savvy', 'Strider (Coastal)', 'Sea Legs'],
                        "Disguise Kit, Small Fleet of Riverboats")
        ]


class CareerStevedore:
    def __init__(self):
        self.lvl = [
            CareerClass("Dockhand",
                        "Brass 3",
                        ['WS', 'T', 'I'],
                        ['Athletics', 'Climb', 'Consume Alcohol', 'Dodge', 'Endurance', 'Gossip', 'Melee (Basic)', 'Swim'],
                        ['Dirty Fighting', 'Strong Back', 'Sturdy', 'Very Strong'],
                        "Hand Weapon (Boat Hook), Leather Gloves"),
            CareerClass("Stevedore",
                        "Silver 1",
                        ['S'],
                        ['Bribery', 'Entertain (Storytelling)', 'Gamble', 'Intimidate', 'Perception', 'Stealth (Urban)'],
                        ['Criminal', 'Etiquette (Guilders)', 'Strong Legs', 'Tenacious'],
                        "Guild Licence, Leather Jerkin, Pipe and Tobacco, Porter Cap"),
            CareerClass("Foreman",
                        "Silver 3",
                        ['WP'],
                        ['Cool', 'Evaluate', 'Intuition', 'Leadership'],
                        ['Dealmaker', 'Embezzle', 'Etiquette (Criminals)', 'Public Speaker'],
                        "Gang of Stevedores, Whistle"),
            CareerClass("Dock Master",
                        "Silver 5",
                        ['INT'],
                        ['Charm', 'Lore (Taxes)'],
                        ['Kingpin', 'Menacing', 'Numismatics', 'Read/Write'],
                        "Office and Staff, Writing Kit")
        ]


class CareerWrecker:
    def __init__(self):
        self.lvl = [
            CareerClass("Cargo Scavenger",
                        "Brass 2",
                        ['WS', 'S', 'I'],
                        ['Climb', 'Consume Alcohol', 'Dodge', 'Endurance', 'Row', 'Melee (Basic)', 'Outdoor Survival', 'Swim'],
                        ['Break and Enter', 'Criminal', 'Fisherman', 'Strong Back'],
                        "Crowbar, Large Sack, Leather Gloves"),
            CareerClass("Wrecker",
                        "Brass 3",
                        ['WP'],
                        ['Bribery', 'Cool', 'Intuition', 'Navigation', 'Perception', 'Set Trap'],
                        ['Flee', 'Rover', 'Strong Swimmer', 'Trapper'],
                        "Hand Weapon (Boat Hook), Leather Jack, Storm Lantern and Oil"),
            CareerClass("River Pirate",
                        "Brass 5",
                        ['BS'],
                        ['Gossip', 'Intimidate', 'Ranged (Crossbow)', 'Stealth (Rural)'],
                        ['Dirty Fighting', 'Etiquette (Criminals)', 'Menacing', 'Waterman'],
                        "Crossbow with 10 Bolts, Grappling Hook and Rope, Riverboat"),
            CareerClass("Wrecker Captain",
                        "Silver 2",
                        ['FEL'],
                        ['Leadership', 'Lore (Riverways)'],
                        ['Furious Assault', 'In-fighter', 'Pilot', 'Warrior Born'],
                        "Fleet of Riverboats and Wrecker Crew, Keg of Ale, Manacles")
        ]


class CareerBawd:
    def __init__(self):
        self.lvl = [
            CareerClass("Hustler",
                        "Brass 1",
                        ['AG', 'DEX', 'FEL'],
                        ['Bribery', 'Charm', 'Consume Alcohol', 'Entertain (Any one)', 'Gamble', 'Gossip', 'Haggle', 'Intimidate'],
                        ['Attractive', 'Alley Cat', 'Blather', 'Gregarious'],
                        "Flask of Spirits"),
            CareerClass("Bawd",
                        "Brass 3",
                        ['I'],
                        ['Dodge', 'Endurance', 'Intuition', 'Lore (Local)', 'Melee (Basic)', 'Perception'],
                        ['Ambidextrous', 'Carouser', 'Criminal', 'Resistance (Disease)'],
                        "Dose of Weirdroot, Quality Clothing"),
            CareerClass("Procurer",
                        "Silver 1",
                        ['WP'],
                        ['Cool', 'Evaluate', 'Language (Any one)', 'Lore (Law)'],
                        ['Dealmaker', 'Embezzle', 'Etiquette (Any one)', 'Suave'],
                        "A Ring of Hustlers"),
            CareerClass("Ringleader",
                        "Silver 3",
                        ['INT'],
                        ['Leadership', 'Lore (Heraldry)'],
                        ['Briber', 'Kingpin', 'Numismatics', 'Savvy'],
                        "Townhouse with Discreet Back Entrance, a Ring of Bawds")
        ]


class CareerCharlatan:
    def __init__(self):
        self.lvl = [
            CareerClass("Swindler",
                        "Brass 3",
                        ['I', 'DEX', 'FEL'],
                        ['Bribery', 'Consume Alcohol', 'Charm', 'Entertain (Storytelling)', 'Gamble', 'Gossip', 'Haggle', 'Sleight of Hand'],
                        ['Cardsharp', 'Diceman', 'Etiquette (Any one)', 'Luck'],
                        "Backpack, 2 Sets of Clothing, Deck of Cars, Dice"),
            CareerClass("Charlatan",
                        "Brass 5",
                        ['WP'],
                        ['Cool', 'Dodge', 'Entertain (Acting)', 'Evaluate', 'Intuition', 'Perception'],
                        ['Blather', 'Criminal', 'Fast Hands', 'Secret Identity'],
                        "1 Forged Document, 2 Sets of Quality Clothing, Selection of Coloured Powders and Water, Selection of Trinkets and Charms"),
            CareerClass("Con Artist",
                        "Silver 2",
                        ['AG'],
                        ['Language (Thief)', 'Lore (Heraldry)', 'Pick Lock', 'Secret Signs (Thief)'],
                        ['Attractive', 'Cat-tongued', 'Dealmaker', 'Read/Write'],
                        "Disguise Kit, Lock Picks, Multiple Forged Documents"),
            CareerClass("Scoundrel",
                        "Silver 4",
                        ['INT'],
                        ['Lore (Genealogy)', 'Research'],
                        ['Gregarious', 'Master of Disguise', 'Nose for Trouble', 'Suave'],
                        "Forged Seal, Writing Kit")
        ]


class CareerFence:
    def __init__(self):
        self.lvl = [
            CareerClass("Broker",
                        "Silver 1",
                        ['I', 'AG', 'FEL'],
                        ['Charm', 'Dodge', 'Evaluate', 'Gamble', 'Gamble', 'Gossip', 'Haggle', 'Melee (Basic)'],
                        ['Alley Cat', 'Cardsharp', 'Dealmaker', 'Gregarious'],
                        "Hand Weapon, Stolen goods worth 3d10 Shillings"),
            CareerClass("Fence",
                        "Silver 2",
                        ['DEX'],
                        ['Cool', 'Intimidate', 'Intuition', 'Perception', 'Secret Signs (Thief)', 'Trade (Engraver)'],
                        ['Criminal', 'Etiquette (Criminals)', 'Numismatics', 'Savvy'],
                        "Eye-glass, Trade Tools (Engraver), Writing Kit"),
            CareerClass("Master Fence",
                        "Silver 3",
                        ['INT'],
                        ['Bribery', 'Entertain (Storytelling)', 'Lore (Art)', 'Lore (Local)'],
                        ['Kingpin', 'Strike to Stun', 'Suave', 'Super Numerate'],
                        "Pawnbroker’s Shop"),
            CareerClass("Black Marketeer",
                        "Silver 4",
                        ['WP'],
                        ['Lore (Heraldry)', 'Research'],
                        ['Dirty Fighting', 'Iron Will', 'Menacing', 'Briber'],
                        "Hired Muscle, Network of Informants, Warehouse")
        ]


class CareerGraveRobber:
    def __init__(self):
        self.lvl = [
            CareerClass("Body Snatcher",
                        "Brass 2",
                        ['S', 'I', 'WP'],
                        ['Climb', 'Cool', 'Dodge', 'Drive', 'Gossip', 'Intuition', 'Perception', 'Stealth (Any one)'],
                        ['Alley Cat', 'Criminal', 'Flee', 'Strong Back'],
                        "Crowbar, Handcart, Hooded Cloak, Tarpaulin"),
            CareerClass("Grave Robber",
                        "Brass 3",
                        ['WS'],
                        ['Bribery', 'Endurance', 'Evaluate', 'Haggle', 'Lore (Medicine)', 'Melee (Basic)'],
                        ['Break and Enter', 'Night Vision', 'Resistance (Disease)', 'Very Strong'],
                        "Backpack, Hand Weapon, Spade, Storm Lantern and Oil"),
            CareerClass("Tomb Robber",
                        "Silver 1",
                        ['DEX'],
                        ['Drive', 'Lore (History)', 'Pick Lock', 'Set Trap'],
                        ['Read/Write', 'Strike Mighty Blow', 'Tenacious', 'Tunnel Rat'],
                        "Hand Weapon (Pick), Horse and Cart, Leather Jack, Rope, Trade Tools (Thief)"),
            CareerClass("Treasure Hunter",
                        "Silver 5",
                        ['INT'],
                        ['Navigation', 'Trade (Engineer)'],
                        ['Fearless (Undead)', 'Sixth Sense', 'Strong-minded', 'Trapper'],
                        "Bedroll, Maps, Tent, Trade Tools (Engineer), Writing Kit")
        ]


class CareerOutlaw:
    def __init__(self):
        self.lvl = [
            CareerClass("Brigand",
                        "Brass 1",
                        ['WS', 'S', 'T'],
                        ['Athletics', 'Consume Alcohol', 'Cool', 'Endurance', 'Gamble', 'Intimidate', 'Melee (Basic)', 'Outdoor Survival'],
                        ['Combat Aware', 'Criminal', 'Rover', 'Flee'],
                        "Bedroll, Hand Weapon, Leather Jerkin, Tinderbox"),
            CareerClass("Outlaw",
                        "Brass 2",
                        ['BS'],
                        ['Dodge', 'Heal', 'Lore (Local)', 'Perception', 'Ranged (Bow)', 'Stealth (Rural)'],
                        ['Dirty Fighting', 'Marksman', 'Strike to Stun', 'Trapper'],
                        "Bow with 10 Arrows, Shield, Tent"),
            CareerClass("Outlaw Chief",
                        "Brass 4",
                        ['I'],
                        ['Gossip', 'Intuition', 'Leadership', 'Ride (Horse)'],
                        ['Rapid Reload', 'Roughrider', 'Menacing', 'Very Resilient'],
                        "Helmet, Riding Horse with Saddle and Tack, Sleeved Mail Shirt, Band of Outlaws"),
            CareerClass("Bandit King",
                        "Silver 2",
                        ['FEL'],
                        ['Charm', 'Lore (Empire)'],
                        ['Deadeye Shot', 'Fearless (Roadwardens)', 'Iron Will', 'Robust'],
                        "‘Fiefdom’ of Outlaw Chiefs, Lair")
        ]


class CareerRacketeer:
    def __init__(self):
        self.lvl = [
            CareerClass("Thug",
                        "Brass 3",
                        ['WS', 'S', 'T'],
                        ['Consume Alcohol', 'Cool', 'Dodge', 'Endurance', 'Intimidate', 'Lore (Local)', 'Melee (Brawling)', 'Stealth (Urban)'],
                        ['Criminal', 'Etiquette (Criminals)', 'Menacing', 'Strike Mighty Blow'],
                        "Brass Knuckles, Leather Jack"),
            CareerClass("Racketeer",
                        "Brass 5",
                        ['FEL'],
                        ['Bribery', 'Charm', 'Evaluate', 'Gossip', 'Language (Estalian or Tilean)', 'Melee (Basic)'],
                        ['Embezzle', 'Dirty Fighting', 'Strike to Stun', 'Warrior Born'],
                        "Hand Weapon, Hat, Mail Shirt"),
            CareerClass("Gang Boss",
                        "Silver 3",
                        ['WP'],
                        ['Intuition', 'Leadership', 'Perception', 'Ranged (Crossbow)'],
                        ['Fearless (Watchmen)', 'Iron Will', 'Resistance (Poison)', 'Robust'],
                        "Crossbow Pistol with 10 Bolts, Gang of Thugs and Racketeers, Lair"),
            CareerClass("Crime Lord",
                        "Silver 5",
                        ['INT'],
                        ['Lore (Law)', 'Lore (Politics)'],
                        ['Commanding Presence', 'Kingpin', 'Frightening', 'Wealthy'],
                        "Network of Informers, Quality Clothing and Hat, Subordinate Gang Bosses")
        ]


class CareerThief:
    def __init__(self):
        self.lvl = [
            CareerClass("Prowler",
                        "Brass 1",
                        ['I', 'AG', 'WP'],
                        ['Athletics', 'Climb', 'Cool', 'Dodge', 'Endurance', 'Intuition', 'Perception', 'Stealth (Urban)'],
                        ['Alley Cat', 'Criminal', 'Flee', 'Strike to Stun'],
                        "Crowbar, Leather Jerkin, Sack"),
            CareerClass("Thief",
                        "Brass 3",
                        ['DEX'],
                        ['Evaluate', 'Gossip', 'Lore (Local)', 'Pick Lock', 'Secret Signs (Thief)', 'Sleight of Hand'],
                        ['Break and Enter', 'Etiquette (Criminals)', 'Fast Hands', 'Shadow'],
                        "Trade Tools (Thief), Rope"),
            CareerClass("Master Thief",
                        "Brass 5",
                        ['S'],
                        ['Bribery', 'Gamble', 'Intimidate', 'Ranged (Crossbow)'],
                        ['Night Vision', 'Nimble Fingered', 'Step Aside', 'Trapper'],
                        "Crossbow Pistol with 10 Bolts, Throwing Knives"),
            CareerClass("Cat Burglar",
                        "Silver 3",
                        ['FEL'],
                        ['Charm', 'Set Trap'],
                        ['Catfall', 'Scale Sheer Surface', 'Strong Legs', 'Wealthy'],
                        "Dark Clothing, Grappling Hook, Mask or Scarves")
        ]


class CareerWitch:
    def __init__(self):
        self.lvl = [
            CareerClass("Hexer",
                        "Brass 1",
                        ['WS', 'T', 'WP'],
                        ['Channelling', 'Cool', 'Endurance', 'Gossip', 'Intimidate', 'Language (Magick)', 'Sleight of Hand', 'Stealth (Rural)'],
                        ['Criminal', 'Menacing', 'Petty Magic', 'Instinctive Diction'],
                        "Candles, Chalk, Doll, Pins"),
            CareerClass("Witch",
                        "Brass 2",
                        ['I'],
                        ['Charm Animal', 'Dodge', 'Intuition', 'Melee (Polearm)', 'Perception', 'Trade (Herbalist)'],
                        ['Arcane Magic (Witchery)', 'Attractive', 'Sixth Sense', 'Witch!'],
                        "Quarterstaff, Sack, Selection of Herbs, Trade Tools (Herbalist)"),
            CareerClass("Wyrd",
                        "Brass 3",
                        ['FEL'],
                        ['Bribery', 'Charm', 'Haggle', 'Lore (Dark Magic)'],
                        ['Animal Affinity', 'Fast Hands', 'Frightening', 'Magical Sense'],
                        "Backpack, Cloak with Several Pockets, Lucky Charm"),
            CareerClass("Warlock",
                        "Brass 5",
                        ['INT'],
                        ['Lore (Daemonology)', 'Lore (Magic)'],
                        ['Aethyric Attunement', 'Luck', 'Strong-minded', 'Very Resilient'],
                        "Robes, Skull")
        ]


class CareerCavalryman:
    def __init__(self):
        self.lvl = [
            CareerClass("Horseman",
                        "Silver 2",
                        ['WS', 'S', 'AG'],
                        ['Animal Care', 'Charm Animal', 'Endurance', 'Language (Battle)', 'Melee (Basic)', 'Outdoor Survival', 'Perception', 'Ride (Horse)'],
                        ['Combat Aware', 'Crack the Whip', 'Lightning Reflexes', 'Roughrider'],
                        "Hand Weapon, Leather Jack, Riding Horse with Saddle and Tack"),
            CareerClass("Cavalryman",
                        "Silver 4",
                        ['BS'],
                        ['Charm', 'Consume Alcohol', 'Cool', 'Gossip', 'Melee (Cavalry)', 'Ranged (Blackpowder)'],
                        ['Etiquette (Soldiers)', 'Gunner', 'Seasoned Traveller', 'Trick Riding'],
                        "Breastplate, Demilance, Helmet, Light Warhorse with Saddle and Tack, Pistol with 10 Shots, Shield"),
            CareerClass("Cavalry Sergeant",
                        "Gold 1",
                        ['I'],
                        ['Intimidate', 'Intuition', 'Leadership', 'Lore (Warfare)'],
                        ['Combat Reflexes', 'Fast Shot', 'Hatred (Any one)', 'Warleader'],
                        "Sash"),
            CareerClass("Cavalry Officer",
                        "Gold 2",
                        ['FEL'],
                        ['Gamble', 'Lore (Heraldry)'],
                        ['Accurate Shot', 'Inspiring', 'Reaction Strike', 'Robust'],
                        "Deck of Cards, Quality Clothing")
        ]


class CareerGuard:
    def __init__(self):
        self.lvl = [
            CareerClass("Sentry",
                        "Silver 1",
                        ['WS', 'T', 'AG'],
                        ['Consume Alcohol', 'Endurance', 'Entertain (Storytelling)', 'Gamble', 'Gossip', 'Intuition', 'Melee (Basic)', 'Perception'],
                        ['Diceman', 'Etiquette (Servants)', 'Strike to Stun', 'Tenacious'],
                        "Hand Weapon, Leather Jerkin, Storm Lantern with Oil"),
            CareerClass("Guard",
                        "Silver 2",
                        ['I'],
                        ['Athletics', 'Cool', 'Dodge', 'Intimidate', 'Melee (Polearm)', 'Ranged (Bow)'],
                        ['Relentless', 'Reversal', 'Shieldsman', 'Strike Mighty Blow'],
                        "Bow with 10 Arrows, Sleeved Mail Shirt, Shield, Spear"),
            CareerClass("Honour Guard",
                        "Silver 3",
                        ['S'],
                        ['Heal', 'Language (Battle)', 'Lore (Etiquette)', 'Melee (Two-handed)'],
                        ['Fearless (Intruders)', 'Jump Up', 'Stout-hearted', 'Unshakeable'],
                        "Great Weapon or Halberd, Helmet, Uniform"),
            CareerClass("Guard Officer",
                        "Silver 5",
                        ['INT'],
                        ['Leadership', 'Lore (Warfare)'],
                        ['Combat Master', 'Furious Assault', 'Iron Will', 'Robust'],
                        "Breastplate")
        ]


class CareerKnight:
    def __init__(self):
        self.lvl = [
            CareerClass("Squire",
                        "Silver 3",
                        ['S', 'I', 'AG'],
                        ['Athletics', 'Animal Care', 'Charm Animal', 'Heal', 'Lore (Heraldry)', 'Melee (Cavalry)', 'Ride (Horse)', 'Trade (Farrier)'],
                        ['Etiquette (Any one)', 'Roughrider', 'Sturdy', 'Warrior Born'],
                        "Leather Jack, Mail Shirt, Riding Horse with Saddle and Tack, Shield and Trade Tools (Farrier)"),
            CareerClass("Knight",
                        "Silver 5",
                        ['WS'],
                        ['Cool', 'Dodge', 'Endurance', 'Intimidate', 'Language (Battle)', 'Melee (Any one)'],
                        ['Menacing', 'Seasoned Traveller', 'Shieldsman', 'Strike Mighty Blow'],
                        "Destrier with Saddle and Tack, Melee Weapon (Any one), Lance, Plate Armour and Helm"),
            CareerClass("First Knight",
                        "Gold 2",
                        ['WP'],
                        ['Charm', 'Consume Alcohol', 'Leadership', 'Lore (Warfare)'],
                        ['Fearless (Any one)', 'Stout-hearted', 'Unshakeable', 'Warleader'],
                        "Barding, Small Unit of Knights"),
            CareerClass("Knight of the Inner Circle",
                        "Gold 4",
                        ['FEL'],
                        ['Lore (Any one)', 'Secret Signs (Knightly Order)'],
                        ['Disarm', 'Inspiring', 'Iron Will', 'Strike to Injure'],
                        "Plumed Great Helm, Squire, Large Unit of Knights or Several Small Units of Knights")
        ]


class CareerPitFighter:
    def __init__(self):
        self.lvl = [
            CareerClass("Pugilist",
                        "Brass 4",
                        ['WS', 'S', 'T'],
                        ['Athletics', 'Cool', 'Dodge', 'Endurance', 'Gamble', 'Intimidate', 'Melee (Any one)', 'Melee (Brawling)'],
                        ['Dirty Fighting', 'In-fighter', 'Iron Jaw', 'Reversal'],
                        "Bandages, Brass Knuckles, Hand Weapon, Leather Jack"),
            CareerClass("Pit Fighter",
                        "Silver 2",
                        ['I'],
                        ['Haggle', 'Intuition', 'Melee (Basic)', 'Melee (Flail or Two-handed)', 'Perception', 'Ranged (Entangling)'],
                        ['Ambidextrous', 'Combat Reflexes', 'Dual Wielder', 'Shieldsman'],
                        "Flail or Great Weapon, Hand Weapon, Net or Whip, Shield or Buckler"),
            CareerClass("Pit Champion",
                        "Silver 5",
                        ['AG'],
                        ['Consume Alcohol', 'Gossip', 'Lore (Anatomy)', 'Perform (Fight)'],
                        ['Combat Master', 'Disarm', 'Menacing', 'Robust'],
                        "Breast Plate, Helmet"),
            CareerClass("Pit Legend",
                        "Gold 2",
                        ['FEL'],
                        ['Charm', 'Ranged (Any one)'],
                        ['Frightening', 'Furious Assault', 'Implacable', 'Reaction Strike'],
                        "Quality Helmet")
        ]


class CareerProtagonist:
    def __init__(self):
        self.lvl = [
            CareerClass("Braggart",
                        "Brass 2",
                        ['WS', 'T', 'AG'],
                        ['Athletics', 'Dodge', 'Endurance', 'Entertain (Taunt)', 'Gossip', 'Haggle', 'Intimidate', 'Melee (Any one)'],
                        ['In-fighter', 'Dirty Fighting', 'Menacing', 'Warrior Born'],
                        "Brass Knuckles, Hood or Mask, Leather Jack"),
            CareerClass("Protagonist",
                        "Silver 1",
                        ['I'],
                        ['Bribery', 'Charm', 'Intuition', 'Melee (Basic)', 'Perception', 'Ride (Horse)'],
                        ['Combat Reflexes', 'Criminal', 'Reversal', 'Strike to Stun'],
                        "Hand Weapon, Mail Shirt, Riding Horse with Saddle and Tack, Shield"),
            CareerClass("Hitman",
                        "Silver 4",
                        ['BS'],
                        ['Climb', 'Cool', 'Navigation', 'Ranged (Thrown)'],
                        ['Careful Strike', 'Disarm', 'Marksman', 'Relentless'],
                        "Cloak, Garotte, Poison, Throwing Knives"),
            CareerClass("Assassin",
                        "Gold 1",
                        ['FEL'],
                        ['Entertain (Acting)', 'Ranged (Crossbow)'],
                        ['Accurate Shot', 'Ambidextrous', 'Furious Assault', 'Strike to Injure'],
                        "Crossbow with 10 shots, Disguise Kit")
        ]


class CareerGiantSlayer:
    def __init__(self):
        self.lvl = [
            CareerClass("Troll Slayer",
                        "Brass 2",
                        ['WS', 'S', 'WP'],
                        ['Consume Alcohol', 'Cool', 'Dodge', 'Endurance', 'Gamble', 'Heal', 'Lore (Trolls)', 'Melee (Basic)'],
                        ['Dual Wielder', 'Fearless (Everything)', 'Frenzy', 'Slayer'],
                        "Axe, Flask of Spirits, Shame, Tattoos"),
            CareerClass("Giant Slayer",
                        "Brass 2",
                        ['T'],
                        ['Evaluate', 'Intimidate', 'Language (Battle)', 'Lore (Giants)', 'Melee (Two-handed)', 'Outdoor Survival'],
                        ['Hardy', 'Implacable', 'Menacing', 'Reversal'],
                        "Great Axe, Jewellery, Troll’s Head"),
            CareerClass("Dragon Slayer",
                        "Brass 2",
                        ['AG'],
                        ['Entertain (Storytelling)', 'Lore (Dragons)', 'Perception', 'Ranged (Thrown)'],
                        ['Ambidextrous', 'Furious Assault', 'Relentless', 'Robust'],
                        "Giant’s Head, Throwing Axes"),
            CareerClass("Daemon Slayer",
                        "Brass 2",
                        ['I'],
                        ['Intuition', 'Lore (Chaos)'],
                        ['Combat Master', 'Frightening', 'Strike Mighty Blow', 'Very Strong'],
                        "Dragon’s Head")
        ]


class CareerSoldier:
    def __init__(self):
        self.lvl = [
            CareerClass("Recruit",
                        "Silver 1",
                        ['WS', 'T', 'WP'],
                        ['Athletics', 'Climb', 'Cool', 'Dodge', 'Endurance', 'Language (Battle)', 'Melee (Basic)', 'Play (Drum or Fife)'],
                        ['Diceman', 'Marksman', 'Strong Back', 'Warrior Born'],
                        "Hand Weapon (Sword), Leather Armor, Uniform"),
            CareerClass("Soldier",
                        "Silver 3",
                        ['BS'],
                        ['Consume Alcohol', 'Gamble', 'Gossip', 'Melee (Any one)', 'Ranged (Any one)', 'Outdoor Survival'],
                        ['Drilled', 'Etiquette (Soldiers)', 'Rapid Reload', 'Shieldsman'],
                        "Breastplate, Helmet, Weapon (Any one)"),
            CareerClass("Sergeant",
                        "Silver 5",
                        ['I'],
                        ['Heal', 'Intuition', 'Leadership', 'Perception'],
                        ['Combat Aware', 'Enclosed Fighter', 'Unshakeable', 'Warleader'],
                        "Symbol of Rank, Unit of Troops"),
            CareerClass("Officer",
                        "Gold 1",
                        ['FEL'],
                        ['Lore (Warfare)', 'Navigation'],
                        ['Inspiring', 'Public Speaker', 'Seasoned Traveller', 'Stout-hearted'],
                        "Letter of Commission, Light Warhorse with Saddle and Tack, Map, Orders, Unit of Soldiers, Quality Uniform, Symbol of Rank")
        ]


class CareerWarriorPriest:
    def __init__(self):
        self.lvl = [
            CareerClass("Novitiate Priest",
                        "Brass 2",
                        ['WS', 'T', 'WP'],
                        ['Cool', 'Dodge', 'Endurance', 'Heal', 'Leadership', 'Lore (Theology)', 'Melee (Any one)', 'Pray'],
                        ['Bless (Any one)', 'Etiquette (Cultists)', 'Read/Write', 'Strong-minded'],
                        "Book (Religion), Leather Jerkin, Religious Symbol, Robes, Weapon (Any one)"),
            CareerClass("Warrior Priest",
                        "Silver 2",
                        ['S'],
                        ['Charm', 'Entertain (Speeches)', 'Intimidate', 'Language (battle)', 'Melee (Any one)', 'Ranged (Any one)'],
                        ['Dual Wielder', 'Inspiring', 'Invoke (Any one)', 'Seasoned Traveller'],
                        "Breastplate, Weapon (Any one)"),
            CareerClass("Priest Sergeant",
                        "Silver 3",
                        ['I'],
                        ['Animal Care', 'Intuition', 'Perception', 'Ride (Horse)'],
                        ['Combat Aware', 'Holy Visions', 'Pure Soul', 'Stout-hearted'],
                        "Light Warhorse with Saddle and Tack"),
            CareerClass("Priest Captain",
                        "Silver 4",
                        ['FEL'],
                        ['Consume Alcohol', 'Lore (Warfare)'],
                        ['Fearless (Any one)', 'Furious Assault', 'Holy Hatred', 'Warleader'],
                        "Religious Relic")
        ]
