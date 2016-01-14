class charSheet:

    def __init__(self):
        #Instanzvariablen festlegen
        #Dem Konstruktor als args mitgeben oder nicht ?
        self.name = '' 
        self.age = 0
        self.size = 0
        self.deity = '' #Wie festlegen was uebergeben werden darf ?
                        #Durch Funktionen abkapseln ?
        self.alignment = '' # Evtl sowas durch enumerate() von einer Liste übergeben ? (Anstatt str)
        self.homeland = ''
        self.race = ''
        self.gender = ''
        self.height = ''
        self.hair = ''
        self.eyes = ''
        self.level = 0

        self.hitpoints = 0 #hitpoints total
        self.wounds = 0 # damage taken
        self.nonlethal_damage = 0 #nonlethal damage taken

        self.initiative = 0 # wuerde dann mit modifier(self.attributes["Dexterity"]) + misc_modifier
                                                                    #Was auch immer das ist ^

        self.armor_class = 0       #Armor classes
        self.touch_armor_class = 0
        self.flat_footed_ac = 0

        #Grundattribute
        self.attributes = {
                "Strength": 10,
                "Dexterity": 10,
                "Constitution": 10,
                "Intelligence": 10,
                "Wisdom": 10,
                "Charisma": 10
                }

        #Rettungswuerfe
        self.fortitude = 0
        self.reflex = 0
        self.wisdom = 0

        #Base Attack Bonus
        self.bab = 0

        #CMB
        self.cmb = 0

        #Sprachen
        self.languages = [] #Sprachen hier anhaengen

        self.skills = {
                #Skillname : rank, ohne Attribut Modifier oder Aehnliches
                "Acrobatics": 0,
                "Appraise": 0,
                "Bluff": 0,
                "Climb": 0,
                #"Craft1": 0, #Evtl einzeln listen ?
                #"Craft2": 0,
                #"Craft3": 0,
                "Diplomacy": 0,
                "Disable Device": 0,
                "Disguise": 0,
                "Escape Artist": 0,
                "Fly": 0,
                "Handle Animal": 0,
                "Heal": 0,
                "Intimidate": 0,
                "Knowledge (Arcana)": 0,
                "Knowledge (Dungeoneering)": 0,
                "Knowledge (Engineering)": 0,
                "Knowledge (Geography)": 0,
                "Knowledge (History)": 0,
                "Knowledge (Local)": 0,
                "Knowledge (Nature)": 0,
                "Knowledge (Nobility)": 0,
                "Knowledge (Planes)": 0,
                "Knowledge (Religion)": 0,
                "Linguistics": 0,
                "Perception": 0,
                "Perform": 0,
                #"Profession1": 0, #Evtl einzeln listen ?
                #"Profession2": 0,
                #"Profession3": 0,
                "Ride": 0,
                "Sense Motive": 0,
                "Sleight of Hand": 0,
                "Spellcraft": 0, 
                "Stealth": 0,
                "Survival": 0,
                "Swim": 0,
                "Use Magic Device": 0
                }

        #Buffs
        self.buffs = [
                #hier Buff-objekte einreihen
                ]

    def modifier(attr):
        return floor((attr - 10) / 2)
