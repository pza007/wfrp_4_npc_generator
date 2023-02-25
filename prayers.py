class PrayerClass:
    def __init__(self, _range, target, duration, description):
        self._range = _range   # str
        self.target = target  # str
        self.duration = duration  # str
        self.description = description  # str


blessings_all = {
    'Battle':           PrayerClass('6 yards', '1', '6 rounds', 'Your target gains +10 WS.'),
    'Breath':           PrayerClass('6 yards', '1', '6 rounds', 'Your target does not need to breathe and ignores rules for suffocation.'),
    'Charisma':         PrayerClass('6 yards', '1', '6 rounds', 'Your target gains +10 Fellowship.'),
    'Conscience':       PrayerClass('6 yards', '1', '6 rounds', 'Your target must pass a Routine (+20) Willpower Test to break any of the Strictures of your deity. If they fail, they are overcome with Shame and do not take the action.'),
    'Courage':          PrayerClass('6 yards', '1', '6 rounds', 'Your target gains +10 Willpower.'),
    'Finesse':          PrayerClass('6 yards', '1', '6 rounds', 'Your target gains +10 Dexterity.'),
    'Fortune':          PrayerClass('6 yards', '1', '6 rounds', 'Your target’s next failed test may be rerolled. The reroll must stand.'),
    'Grace':            PrayerClass('6 yards', '1', '6 rounds', 'Your target gains +10 Agility.'),
    'Hardiness':        PrayerClass('6 yards', '1', '6 rounds', 'Your target gains +10 Toughness.'),
    'Healing':          PrayerClass('Touch',   '1', 'Instant',  'Your target heals +1 Wound.'),
    'Hunt':             PrayerClass('6 yards', '1', '6 rounds', 'Your target gains +10 Ballistic Skill.'),
    'Might':            PrayerClass('6 yards', '1', '6 rounds', 'Your target gains +10 Strength.'),
    'Protection':       PrayerClass('6 yards', '1', '6 rounds', 'Enemies must make a Average (+20) Willpower Test to attack your target as shame wells within for considering violence. If they fail, they must choose a different target, or a different Action.'),
    'Recuperation':     PrayerClass('Touch',   '1', 'Instant',  'Your target may reduce the duration of 1 disease with which they are afflicted by 1 day. This prayer may only be attempted once per instance of a disease per person.'),
    'Righteousness':    PrayerClass('6 yards', '1', '6 rounds', 'Your target’s weapon counts as Magical.'),
    'Savagery':         PrayerClass('6 yards', '1', '6 rounds', 'When your target next inflicts a Critical Wound, roll twice and choose the best result.'),
    'Tenacity':         PrayerClass('6 yards', '1', 'Instant',  'Your target may remove 1 condition.'),
    'Wisdom':           PrayerClass('6 yards', '1', '6 rounds', 'Your target gains +10 Intelligence.'),
    'Wit':              PrayerClass('6 yards', '1', '6 rounds', 'Your target gains +10 Initiative.')
}
blessings_Manann = {
    'Battle':           blessings_all['Battle'],
    'Breath':           blessings_all['Breath'],
    'Courage':          blessings_all['Courage'],
    'Hardiness':        blessings_all['Hardiness'],
    'Savagery':         blessings_all['Savagery'],
    'Tenacity':         blessings_all['Tenacity']
}
blessings_Morr = {
    'Breath':           blessings_all['Breath'],
    'Courage':          blessings_all['Courage'],
    'Fortune':          blessings_all['Fortune'],
    'Righteousness':    blessings_all['Righteousness'],
    'Tenacity':         blessings_all['Tenacity'],
    'Wisdom':           blessings_all['Wisdom']
}
blessings_Myrmidia = {
    'Battle':           blessings_all['Battle'],
    'Conscience':       blessings_all['Conscience'],
    'Courage':          blessings_all['Courage'],
    'Fortune':          blessings_all['Fortune'],
    'Protection':       blessings_all['Protection'],
    'Righteousness':    blessings_all['Righteousness']
}
blessings_Ranald = {
    'Charisma':         blessings_all['Charisma'],
    'Conscience':       blessings_all['Conscience'],
    'Finesse':          blessings_all['Finesse'],
    'Fortune':          blessings_all['Fortune'],
    'Protection':       blessings_all['Protection'],
    'Wit':              blessings_all['Wit']
}
blessings_Rhya = {
    'Breath':           blessings_all['Breath'],
    'Conscience':       blessings_all['Conscience'],
    'Grace':            blessings_all['Grace'],
    'Healing':          blessings_all['Healing'],
    'Protection':       blessings_all['Protection'],
    'Recuperation':     blessings_all['Recuperation']
}
blessings_Shallya = {
    'Breath':           blessings_all['Breath'],
    'Conscience':       blessings_all['Conscience'],
    'Healing':          blessings_all['Healing'],
    'Protection':       blessings_all['Protection'],
    'Recuperation':     blessings_all['Recuperation'],
    'Tenacity':         blessings_all['Tenacity']
}
blessings_Sigmar = {
    'Battle':           blessings_all['Battle'],
    'Courage':          blessings_all['Courage'],
    'Hardiness':        blessings_all['Hardiness'],
    'Might':            blessings_all['Might'],
    'Protection':       blessings_all['Protection'],
    'Righteousness':    blessings_all['Righteousness']
}
blessings_Taal = {
    'Battle':           blessings_all['Battle'],
    'Breath':           blessings_all['Breath'],
    'Conscience':       blessings_all['Conscience'],
    'Hardiness':        blessings_all['Hardiness'],
    'Hunt':             blessings_all['Hunt'],
    'Savagery':         blessings_all['Savagery']
}
blessings_Ulric = {
    'Battle':           blessings_all['Battle'],
    'Courage':          blessings_all['Courage'],
    'Hardiness':        blessings_all['Hardiness'],
    'Might':            blessings_all['Might'],
    'Savagery':         blessings_all['Savagery'],
    'Tenacity':         blessings_all['Tenacity']
}
blessings_Verena = {
    'Conscience':       blessings_all['Conscience'],
    'Courage':          blessings_all['Courage'],
    'Fortune':          blessings_all['Fortune'],
    'Righteousness':    blessings_all['Righteousness'],
    'Wisdom':           blessings_all['Wisdom'],
    'Wit':              blessings_all['Wit']
}
blessings_by_god = {
    'Manann':           blessings_Manann,
    'Morr':             blessings_Morr,
    'Myrmidia':         blessings_Myrmidia,
    'Ranald':           blessings_Ranald,
    'Rhya':             blessings_Rhya,
    'Shallya':          blessings_Shallya,
    'Sigmar':           blessings_Sigmar,
    'Taal':             blessings_Taal,
    'Ulric':            blessings_Ulric,
    'Verena':           blessings_Verena
}


miracles_Manann = {
    'Becalm':               PrayerClass('[bI] miles', '1 sailing vessel within Line of Sight', '1 hour', 'You steal the wind from the sails of a ship or boat. It is completely becalmed. Even in stormy weather an area of eerie calm and smooth waters surrounds the vessel while gales, lashing rains and towering crests surge and crash around it. This area of calm extends for Initiative yards from the vessel, and if the ship is propelled by some other method, such as oars, the area of calm travels with it.'),
    'Drowned Man’s Face':   PrayerClass('[FEL] yards', '1', '[bFEL] rounds', 'You implore Manann to drown your foes. Your targets’ lungs continuously fill with saltwater while the Miracle is active, and their hair floats around their head as if submerged. Your targets gains a Fatigued Condition, and are subject to the rules for Drowning and Suffocation (page 181) while the Miracle is in effect. When the Miracle ends, your targets must attempt a Challenging (–20) Endurance Test. If a Failure is scored, also inflict a Prone Condition.'),
    'Fair Winds':           PrayerClass('[bI] miles', '1 sailing vessel within Line of Sight', '1 hour', 'The target vessels’ sails fill with favourable winds, speeding them safely towards their destination. While this Miracle is active, the sailing vessel moves at top speed, no matter the prevailing wind, tide, or current, and all Tests made to steer the vessel gain a bonus of +10.'),
    'Manann’s Bounty':      PrayerClass('Touch', '1', 'Instant', 'You implore Manann to provide you with sustenance. Reaching into a body of water you catch enough fish to feed 1 person; if you reach into the sea, you provide enough fish for 2 people. For every +2 SL, you may feed another person.'),
    'Sea Legs':             PrayerClass('[FEL] yards', '1', '[bFEL] rounds', 'Your targets are immediately drenched in saltwater, and reel as if on the rolling deck of a tempest-tossed vessel. Their hair is whipped by spectral winds, and a torrent of spray lashes their skin. They gain one each of the Blinded, Deafened, and Fatigued Conditions, and must attempt an Average (+20) Agility Test to use their Move. If they fail, they also gain a Prone Condition.'),
    'Waterwalk':            PrayerClass('You', 'You', '[bFEL] minutes', 'You call on Manann to allow you to cross a stretch of open water as if it were solid ground. This only works on larger bodies of water that are at least 10 yards wide. Anything smaller is too far removed from Manann’s domain for it to be noticed.')
}
miracles_Morr = {
    'Death Mask':           PrayerClass('You', 'You', '[bFEL] rounds', 'Morr works through you, piercing the Portal to make his presence known to your foes. Your visage takes on a cadaverous mien, and you gain Fear 1.'),
    'Destroy Undead':       PrayerClass('You', 'AoE', 'Instant', 'You call the power of Morr to smite all Undead. A black fire ripples forth from your body in a perfect circle for [bFEL] yards. All potential targets with the Undead Creature Trait lose 1d10 Wounds, ignoring Toughness Bonus and AP. Any Undead destroyed by this Miracle can never be raised with Necromancy again under normal conditions. For every +2 SL, you may increase the area of effect by +[bFEL] yards.'),
    'Dooming':              PrayerClass('Touch', '1', 'Instant', 'Gazing deeply into your target’s eyes while muttering a threnody to Morr, you are granted a vision of the target’s Doom, a glimpse of what the future holds. This is almost always related to the target’s death. This Miracle may only be performed on a character once, after which the Doomed Talent may be purchased with XP as if it were in the target’s Career.'),
    'Last Rites':           PrayerClass('1 yard', '1', 'Instant', 'You chant a solemn requiem over a corpse. This miracle ensures that the soul is sent through the portal to Morr’s realm, and guarantees the cadaver may not be targeted by any Necromantic spells. If the Miracle targets a foe with the Undead and Construct Creature Traits, it will be destroyed.'),
    'Portal’s Threshold':   PrayerClass('Touch', 'AoE', 'Special', 'You draw a line up to 8 yards long on the ground while incanting a dirge to Morr. Upon enacting the Miracle, an indistinct, shadowy portal seems to manifest to the hoarse croaking of ravens. Creatures with the Undead Creature Trait must pass a Challenging (+0) Willpower Test to cross the line. Creatures with both Undead and Construct simply cannot cross the line. The Miracle remains in effect until dawn.'),
    'Stay Morr’s Hand':     PrayerClass('Touch', '1', '[bFEL] hours (Special)', 'You touch the eyes of someone close to death and request Morr guide the soul within, but not take it. The target must have 0 Wounds and be willing. For the duration of the Miracle, the target gains the Unconscious Condition and will not deteriorate until the Miracle ends, staving off disease, ignoring critical wounds and poisons, and similar. This miracle comes to an end should appropriate healing be provided, or should you perform the last rights. If you do this, which takes about a minute, the target’s soul will pass through Morr’s portal upon death, and the resulting corpse may never be targeted by Necromancy.')
}
miracles_Myrmidia = {
    'Blazing Sun':          PrayerClass('You', 'AoE', 'Instant', 'You call on Myrmidia to scour the battlefield of dishonourable foes, and a blinding flash of golden light bursts forth. All non- Myrmidians looking in your direction receive 1 Blinded Condition. For every +2 SL, they receive +1 Blinded Condition.'),
    'Eagle’s Eye':          PrayerClass('[FEL] yards', 'You', '[bFEL] rounds', 'You call on Myrmidia to send a Divine Servant to grant you knowledge of your enemies. A spectral Eagle manifests, soaring into the sky above. The eagle looks like and has the capabilities of a normal eagle, but cannot physically affect the world, or be harmed in any way. While the Miracle is in effect, you can see through the eagle’s eyes and control its flight, surveying the battlefield and spying upon your enemies. Your vision is acute, but you do not have access to any of your own sense-enhancing Talents such as Night Vision. While looking through the eagle’s eyes, you cannot see through your own eyes, leaving you potentially vulnerable.'),
    'Fury’s Call':          PrayerClass('[FEL] yards', '[bINT] allies', '[bFEL] rounds', 'Your passionate prayers instil your allies with a furious disdain for their foes. All allies affected receive the Hatred Psychology towards any engaging them in combat.'),
    'Inspiring':            PrayerClass('[FEL] yards', '[bINT] allies', '[bFEL] rounds', 'Your rousing prayers inspire discipline and coordination within the ranks. Affected targets gain the +1 Drilled Talent.'),
    'Shield of Myrmidia':   PrayerClass('[FEL] yards', '[bINT] allies', '[bFEL] rounds', 'Your stalwart prayers incite Myrmidia to shield your allies in glittering, gossamer strands of light, warding enemy blows. All those affected gain +1 AP on all locations.'),
    'Spear of Myrmidia':    PrayerClass('You', 'You', '[bFEL] rounds', 'If wielding a spear, it gains the Impact Quality, and counts as Magical.')
}
miracles_Ranald = {
    'An Invitation':        PrayerClass('1 yard', '1', 'Instant', 'You spin one of Ranald’s riddles concerning portals, and whether they exist if closed. A door, window, or hatch you target has one method of securing it undone — a lock unlocks, a latch unlatches, a rope unties. For every +2 SL you may target another method of securing the door, window, or hatch.'),
    'Cat’s Eyes':           PrayerClass('[FEL] yards', 'You', '[bFEL] rounds', 'Does anything exist that cannot be seen? You riddle with Ranald, who sends a Divine Servant in the form of a cat as an answer. The cat looks like and has the capabilities of a normal cat, but cannot be harmed in any way. While the Miracle is in effect, you perceive everything the cat perceives — sight, sound, touch — and control its movement. Your senses are as sharp as a cat’s, but you do not have access to any of your own sense-enhancing Talents such as Night Vision. While the Miracle is in effect, you cannot perceive anything through your own senses, leaving you vulnerable.'),
    'Ranald’s Grace':       PrayerClass('Touch', '1', '[bAG] rounds', 'You call on Ranald to let your target negotiate the riddles of reality. Your target gains +10 Agility, +10 Stealth, and +1 Catfall Talent for the duration of the Miracle.'),
    'Rich Man, Poor Man, Beggar Man, Thief': PrayerClass('1', '1', '[bFEL] minutes', 'You smile at Ranald as you cheekily ask others what, exactly, is wealth? For each target affected, choose one option: • the target’s purse appears empty • the target’s purse appears full • the target’s attire appears cheap and unremarkable • the target’s attire appears rich and finely crafted • a single valuable item is impossible to perceive For every +2 SL you may select an additional effect for one of your targets.'),
    'Stay Lucky':           PrayerClass('You', 'You', 'Special', 'Crossing your fingers, you pose Ranald’s enigma and ask what, exactly, is luck? Gain +1 Fortune point. For every +2 SL you may gain an extra +1 Fortune point, which may take you beyond your normal maximum. You may not invoke this Miracle again until you reach 0 Fortune points.'),
    'You Ain’t Seen Me, Right?': PrayerClass('[FEL] yards', '1', '[bFEL] rounds', 'You spin a complex conundrum concerning the reality of that which is unperceived. Targets affected by this Miracle may pass unnoticed and remarked, providing they do nothing to draw attention to themselves, such as touching, attacking, calling out to someone, casting a spell, or making a loud noise. You may only invoke this Miracle if no-one is looking directly at you.')
}
miracles_Rhya = {
    'Rhya’s Children':      PrayerClass('You', 'AoE', '[bFEL] rounds', 'Laying hands on the earth, you chant a prayer to Rhya appealing for her aid in understanding her Realm. This Miracle may only be invoked outdoors, outside settlements. You sense the presence and passing of all sentient creatures within Fellowship yards. Each +2 SL extents the area of effect by +[FEL] yards.'),
    'Rhya’s Harvest':       PrayerClass('Touch', 'You', '1 round', 'You chant to Rhya, and life springs forth. Edible fruit, vegetables, and fungi grow at the point where you touch. For each round in which the Miracle is in effect, you cause enough food to feed 1 person to grow. The type of food depends on your location: in a cavern you may grow mushrooms, while outdoors you may cause many different fruits and vegetables to spring forth.'),
    'Rhya’s Shelter':       PrayerClass('You', 'You', 'Special', 'You sing one of Rhya’s hymns concerning shelter and safety. You may only invoke this Miracle outdoors and outside settlements. You discover a perfect natural shelter. Some combination of earth, and trees has formed a perfect location to camp for the night. The spot is protected from all naturally occurring wind and rain, and lasts as long as you remain camped there. The shelter is large enough for 1 person. For every +2 SL it fits another individual. When you break camp, the shelter cannot be rediscovered, as though it only existed through your goddess’s will.'),
    'Rhya’s Succour':       PrayerClass('[FEL] yards', '[bFEL] allies', 'Instant', 'You chant Rhya’s song of revitalisation. All affected targets have 1 Condition removed. If this removes all suffered Conditions, the targets feel as refreshed as if they had just awoken from a good night’s sleep, and gain a bonus of +10 to any tests on their next Turn.'),
    'Rhya’s Touch':         PrayerClass('Touch', '1', 'Special', 'You lay hands upon an injured or diseased target as you sing your prayers. Choose one of the following effects: • Heal Fellowship Bonus wounds • Cure 1 naturally occurring disease For every + 2 SL, you may choose another effect, and may choose the same effect repeatedly. This Miracle is slow, with the effects taking at least 10 minutes to manifest. If interrupted, the Miracle will need to be attempted again.'),
    'Rhya’s Union':         PrayerClass('Touch', 'Special', '[bFEL] hours', 'You bless and consecrate the union between two souls. While the Miracle is in effect, if biologically possible, the couple will conceive a child.')
}
miracles_Shallya = {
    'Anchorite’s Endurance':    PrayerClass('[FEL] yards', '1', '[bFEL] rounds', 'Your earnest prayers appeal to Shallya to grant the target the strength to endure. The target feels no pain, and suffers no penalties caused by Conditions.'),
    'Balm to a Wounded Mind':   PrayerClass('Touch', '1', '[bFEL] minutes', 'You call on Shallya to calm the troubled mind of your targets. All Psychology traits are removed for the duration, and afterwards the targets enter deep and restful slumbers that last until next sunrise, assuming they are not disturbed. Unwilling targets may make a Challenging (+0) Cool Test to resist sleeping.'),
    'Bitter Catharsis':         PrayerClass('Touch', '1', 'Instant', 'In answer to your heartfelt prayers, Shallya draws a poison or disease into you and purges it, completely removing it from your target’s system. For every +2 SL you may purge another disease or poison. For each poison removed or disease cured in this manner, you suffer Wounds equal to 1d10 – your Fellowship Bonus, not modified for Toughness Bonus or Armour Points.'),
    'Martyr':                   PrayerClass('[FEL] yards', '1', '[bFEL] rounds', 'You intone prayers concerning Shallya’s need to take on the world’s pain. Any Damage taken by your targets are instead suffered by you. If you suffer any Damage because of this Miracle, your Toughness Bonus is doubled for the purposes of calculating the Wounds suffered from that Damage.'),
    'Shallya’s Tears':          PrayerClass('Touch', '1', 'Special', 'You passionately appeal to Shallya to spare a poor, wounded soul as tears flow freely down your cheeks. You pray for 10 – [bFEL] rounds, at which point you heal the target of 1 Critical Wound. For every +2 SL you may heal another Critical Wound. If your prayer is interrupted, the target receives no benefit. This Miracle cannot reattach amputated body parts.'),
    'Unblemished Innocence':    PrayerClass('Touch', '1', 'Instant', 'Laying hands on the afflicted, you beg Shallya to rid them of recently acquired corruption. The target loses 1 Corruption point, and can lose another per +2 SL scored. However, the Chaos Gods do not like to be so directly opposed. Should an attempt to invoke the Miracle Fumble, you and the target both gain 1d10 Corruption points on top of any other effects. This Miracle must be enacted within an hour of the target gaining a Corruption point.')
}
miracles_Sigmar = {
    'Beacon of Righteous Virtue':   PrayerClass('You', 'Aoe', '[bFEL] rounds', 'As you bellow prayers in Sigmar’s name, you become infused with holy fire of righteousness. All allies with Line of Sight to you instantaneously remove all Broken Conditions, and gain the Fearless Talent while the Miracle is in effect and they remain in your Line of Sight. Any Greenskins with Line of Sight to you are subject to Fear 1.'),
    'Heed Not the Witch':           PrayerClass('You', 'Aoe', '[bFEL] rounds', 'You call on Sigmar to protect those close to you from the fell influence of Chaos. Any spells that target anyone or anywhere within Fellowship Bonus yards suffer a penalty of –20 to Language (Magick) Tests, in addition to any other penalties. For every +2 SL, you may increase the area of effect by your [bFEL] yards.'),
    'Sigmar’s Fiery Hammer':        PrayerClass('You', 'You', '[bFEL] rounds', 'You chant benedictions of Sigmar’s might. If wielding a warhammer, it counts as Magical, deals +[bFEL] Damage, and any target struck receives the Ablaze and Prone Conditions.'),
    'Soulfire':                     PrayerClass('You', 'AoE', 'Instant', 'You call the power of Sigmar to smite the enemies of the Empire. A holy fire explodes from your body blasting outwards for [bFEL] yards. All targets within range take 1d10 Wounds ignoring Toughness Bonus and APs. Targets with the Undead and Daemon Creature Traits also gain the Ablaze Condition. For every +2 SL, you may increase the area of effect by +[bFEL] yards, or cause an extra +2 Damage to any Greenskins, Undead, or servants of the Ruinous Powers affected.'),
    'Twin-tailed Comet':            PrayerClass('[FEL] yards', 'AoE', 'Instant', 'You invoke litanies to Sigmar, calling on him to smite his foes. A twin-tailed comet, blazing a trail of fire in its wake, plummets from the heavens to strike a point within Line of Sight and range. Everything within Fellowship Bonus yards of the point of impact suffers 1d10 + SL Damage, ignoring Toughness Bonus and Armour Points, and gains the Ablaze condition. The target location must be outdoors, and may only target those Sigmar would deem an enemy.'),
    'Vanquish the Unrighteous':     PrayerClass('[FEL] yards', '[bFEL] allies', '[bFEL] rounds', 'Your prayers instil your chosen allies with a furious disdain for the enemies of Sigmar. All allies affected receive the Hatred Psychology towards Greenskins, Undead, and any associated with Chaos.')
}
miracles_Taal = {
    'Animal Instincts':           PrayerClass('Touch', '1', '[bFEL] hours', 'You intone chants describing Taal’s extraordinary senses, and calling upon him for aid. While the Miracle is in effect, you gain +1 Acute Sense (choose one) Talent and, if you rest, you will automatically awaken should any threats come within [I] yards.'),
    'King of the Wild':           PrayerClass('[FEL] yards', '1', '[bFEL] rounds', 'You chant a low prayer, and Taal answers with a wild animal appropriate for the surrounding area, which will act according to your wishes for the duration of the Miracle. See The Beasts of the Reikland on page 314 for sample animals that may be summoned.'),
    'Leaping Stag':               PrayerClass('You', 'You', '[bFEL] rounds', 'You chant to Father Taal, and he grants you his favour, imbuing you with speed and agility. You gain +1 Movement and +1 Strong Legs Talent. Further, you automatically pass all Athletics Tests to jump with at least +0 SL; should you score lower, increase the SL to 0.'),
    'Lord of the Hunt':           PrayerClass('You', 'You', '[bFEL] hours', 'You call on Taal to guide you in the hunt for your quarry, which must be an animal you have seen, or an individual you know (as limited by the GM). While the Miracle is in effect, you cannot lose your quarry’s trail save by supernatural means. Should your quarry enter a settlement, the trail ends there. You also receive +10 bonus to all Tests regarding your quarry while under the influence of the Miracle. '),
    'Tooth and Claw':             PrayerClass('You', 'You', '[bFEL] rounds', 'You call on Taal to grant you the ferocious might of his kingdom. Gain the Bite ([bS+3]) and Weapon ([bS+4]) Creature Traits. These attacks are Magical.'),
    'Tanglefoot':                 PrayerClass('[FEL] yards', 'AoE', 'Instant', 'You call on Taal, chanting prayers to protect his wild places. Roots, vines, and creepers wrap themselves around your foes. All targets within [bFEL] yards of the target point gain an Entangled Condition. For every +2 SL you may increase the area of effect by [bFEL] yards, or inflict an extra Entangled Condition. Tanglefoot has a Strength equal to [WP] for the purposes of breaking free.')
}
miracles_Ulric = {
    'Hoarfrost’s Chill':          PrayerClass('You', 'AoE', '[bFEL] rounds', 'You scream angry prayers, and cold Ulric answers. Your eyes gain a steely blue glint and the air around you grows unnaturally cold. You cause Fear (1) (see page 190) in all enemies, and all within [FEL] yards range lose –1 Advantage at the start of each Round, as they are chilled to the bone.'),
    'Howl of the Wolf':           PrayerClass('[FEL] yards', 'Special', '[bFEL] rounds', 'You howl for Ulric’s aid, and he sends a minor Divine Servant in the form of a White Wolf. The wolf fights your enemies for the duration of the Miracle, before vanishing to Ulric’s Hunting Grounds with a spectral, blood-chilling howl. The White Wolves have the statistics of a Wolf (see page 317) with the Frenzy, Magical, and Size (Large) Creature Traits. '),
    'Ulric’s Fury':               PrayerClass('[FEL] yards', '1', '[bFEL] rounds', 'You chant furious prayers, and Ulric’s ferocity spreads. Targets gain the Frenzy psychology.'),
    'Pelt of the Winter Wolf':    PrayerClass('Touch', '1', '[bFEL] hours', 'Your bellowed prayers bring Ulric’s attention, allowing your targets to survive the bite of his realm. While targets still feel the pain and discomfort caused by cold and wintry weather, they suffer no mechanical penalties.'),
    'The Snow King’s Judgement':  PrayerClass('[FEL] yards', '1', 'Instant', 'You call on Ulric to make manifest his disdain for the weak, the cowardly and the deceitful. The target suffers 1d10 wounds ignoring Toughness Bonus and Armour Points. If the GM rules that the target is neither weak, cowardly, or deceitful, you suffer the effects instead.'),
    'Winter’s Bite':              PrayerClass('You', 'You', '[bFEL] rounds', 'You roar prayers concerning Blitzbeil, Ulric’s ever-thirsty axe. If wielding an axe, it counts as Magical, causes an additional + SL Damage, and any living targets struck must make a Challenging (+0) Endurance Test or gain a Stunned Condition. Further, struck targets lose any Bleeding Conditions as their blood freezes; similarly, attacks from your axe cannot cause any Bleeding Conditions.')
}
miracles_Verena = {
    'As Verena Is My Witness':      PrayerClass('You', 'You', '[bFEL] rounds', 'By calling Verena as your witness, the truth of your words shines out for all to see. For the duration of the Miracle, providing you speak only the truth, all listeners will believe you speak truly. This does not necessarily mean they will agree with your conclusions, of course.'),
    'Blind Justice':                PrayerClass('You', 'You', '[bFEL] rounds', 'You articulate prayers concerning Verena’s acute perceptions, able pierce through to the truth of all things. You may make a Simple Challenging (+0) Perception Test to see through spells and Miracles of involving illusion or misdirection. You may also make a Average (+20) Intuition Test to tell whether a character speaking to you is lying. Note: this will only tell you if the character believes they speak the truth, it will not alert you if they are mistaken.'),
    'Shackles of Truth':            PrayerClass('[FEL] yards', '1', '[bFEL] rounds', 'Your appeal to Verena, requesting her judgement concerning a suspected criminal. If your target committed a crime and claims they did not, while affected by this miracle they gain an Entangled Condition that cannot be removed for the duration. If you have falsely accused the target, Verena is displeased with your lack of wisdom: you gain +1 Sin point and must immediately roll on The Wrath of the Gods table.'),
    'Sword of Justice':             PrayerClass('You', 'You', '[bFEL] rounds', 'You pray to Verena to guide your blade to strike down the unjust. If wielding a sword, it ignores APs, and counts as Magical. Further, if struck opponents are criminals (as determined by the GM), they must make an Average (+20) Endurance or suffer an Unconscious Condition that lasts for at least [bFEL] rounds. If any crime is perpetrated on the unconscious opponents, you suffer +1 Sin point per crime. '),
    'Truth Will Out':               PrayerClass('[bFEL] yards', '1', 'Instant', 'You intone prayers of Verena’s ability to find any truth. You may ask the targets a single question. It will be immediately answered truthfully and fully. If desired, targets may attempt to resist, by contesting your SL with a Average (+20) Cool Test. If successful, they may stubbornly refuse to answer. If they achieve +2 SL they may withhold minor information. +4 SL allows them to withhold significant information while +6 SL allows them to lie outright. You will know if they resist successfully, though you will lack specific knowledge about their deceit, or proof of their dishonesty. '),
    'Wisdom of the Owl':            PrayerClass('You', 'You', '[bFEL] rounds', 'You call on Verena to instil you with her wisdom and knowledge. You gain a bonus of +20 on all Intelligence Tests while this Miracle is in effect. Further, your pupils dilate widely, and your gaze becomes piercing and unsettling: gain +1 Menacing and Acute Sense (Sight) Talent.')
}
miracles_by_god = {
    'Manann':           miracles_Manann,
    'Morr':             miracles_Morr,
    'Myrmidia':         miracles_Myrmidia,
    'Ranald':           miracles_Ranald,
    'Rhya':             miracles_Rhya,
    'Shallya':          miracles_Shallya,
    'Sigmar':           miracles_Sigmar,
    'Taal':             miracles_Taal,
    'Ulric':            miracles_Ulric,
    'Verena':           miracles_Verena
}
