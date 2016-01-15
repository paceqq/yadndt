from math import floor
from deities import *

class CharSheet:

    def __init__(self, char_name, deity_name):
        #Instanzvariablen festlegen
        #Dem Konstruktor als args mitgeben oder nicht ?

        #Konvention: Methoden Testen Argumente, wenn Argument nicht Anwendbar -> None
        #To-Do: Exception handling

        self.name = self.set_name(char_name)
        self.age = 0
        self.size = 0
        self.deity = self.set_deity(deity_name) #Wie festlegen was uebergeben werden darf ? Durch Funktionen abkapseln ?
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

        self.spells_per_day = {
                #Lvl:Anzahl
                0: 0,
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 0,
                8: 0,
                9: 0
                }

        self.spells = [
                #Wirkbare Zauber hier einfügen
                ]

        self.feats = [
                #hier Feat-Objekte einreihen
                ]

        self.gear = [
                #hier Item-Objekte oder Vererbungen dieser einfügen
                ]

    #Hier Uebergreifende quasi Konstanten festlegen
    #Deities werden ausgelager, da fickend lange Liste
    #from deities import ...


    #Hier Hilfsfunktionen
    def modifier(attr):
        return floor((attr - 10) / 2)

    #Hier set-Funktionen, die Eingaben ueberpruefen (spaeter)
    def set_deity(self, name): #Hier vielleicht noch Schutz gegen falsches Aufrufen 
        return Deity.get_deity(name)

    def set_name(self, name):
        return name



