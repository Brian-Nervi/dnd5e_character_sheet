from operator import index

import database
from inputchecks import language_check

class Character:
    def __init__(self, name, Class, background, race, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = name.capitalize()
        self.Class = Class.capitalize()
        self.background = background.capitalize()
        self.race = race.capitalize()
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        
    

    def race_modifiers(self):
        # uses the data from database.py to calculate the ability score modifiers for the character based on their race.
        race_data = database.races[self.race]
        for ability, modifier in race_data["ability_score_increase"].items():
            if ability == "all":
                self.strength += modifier
                self.dexterity += modifier
                self.constitution += modifier
                self.intelligence += modifier
                self.wisdom += modifier
                self.charisma += modifier
            elif ability == "strength":
                self.strength += modifier
            elif ability == "dexterity":
                self.dexterity += modifier
            elif ability == "constitution":
                self.constitution += modifier
            elif ability == "intelligence":
                self.intelligence += modifier
            elif ability == "wisdom":
                self.wisdom += modifier
            elif ability == "charisma":
                self.charisma += modifier
            elif ability == "any_other_1":
                print("You have 1 extra ability score increase from your race. Which ability score do you want to increase? (strength, dexterity, constitution, intelligence, wisdom, charisma)")
                self.extra_modifiers_1()
            elif ability == "any_other_2":    
                print("You have another extra ability score increase")
                self.extra_modifiers_1()

                # for now we will ignore the "any other" modifiers, but in the future we could ask the user which ability they want to increase.

    def extra_modifiers_1(self):
        #this function will prompt the user to choose which ability score they want to increase for the "any other" modifiers, and then apply those modifiers to the character.
        
        add_to = input().lower()
        while add_to not in ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]:
            print("Please enter a valid ability score (strength, dexterity, constitution, intelligence, wisdom, charisma).")
            add_to = input().lower()
        if add_to == "strength":
            self.strength += 1
        elif add_to == "dexterity":
            self.dexterity += 1
        elif add_to == "constitution":
            self.constitution += 1
        elif add_to == "intelligence":  
            self.intelligence += 1
        elif add_to == "wisdom":            
            self.wisdom += 1
        elif add_to == "charisma":
            self.charisma += 1

    def return_character_sheet(self):
        # this function will return a string representation of the character sheet, which we can then print to the console or save to a file.
        character_sheet = f"Name: {self.name}\nClass: {self.Class}\nBackground: {self.background}\nRace: {self.race}\nStrength: {self.strength}\nDexterity: {self.dexterity}\nConstitution: {self.constitution}\nIntelligence: {self.intelligence}\nWisdom: {self.wisdom}\nCharisma: {self.charisma}\nEquipment: {', '.join(self.equipment)}\nLanguages: {', '.join(self.languages)}\nSkill Proficiencies: {', '.join(self.skill_proficiencies)}\nTool Proficiencies: {', '.join(self.tool_proficiencies)}"
        return character_sheet
    
    def get_data_from_database(self): #inside this funtion we are going to get all the relevant data from database.py
        self.race_modifiers()
        self.get_languages()
        self.get_equipment()
        self.skill_proficiencies = database.backgrounds[self.background]["skill_proficiencies"]
        self.tool_proficiencies = database.backgrounds[self.background]["tools"]
    
    def get_extra_language_options(self):
        # this function will check for any extra language options that the user can choose based on their class, background, or race, and then prompt the user to choose those options, and then store those options in the character object so that we can use that data later when we print the character sheet or save it to a file.
        if "one extra" in self.languages:
            print("You have an extra language option from your race. Which language do you want to learn? (choose from: " + ", ".join(database.languages) + ")")
            self.add_language(input().capitalize())
            self.languages.remove("one extra") # we remove the "one extra"
        if "one of your choice" in self.languages:
            print("You have an extra language option from your background. Which language do you want to learn? (choose from: " + ", ".join(database.languages) + ")")
            self.add_language(input().capitalize())
            self.languages.remove("one of your choice") # we remove the "one of your choice"
        if "two of your choice" in self.languages:
            print("You have two extra language options from your background. Which languages do you want to learn? (choose from: " + ", ".join(database.languages) + ")")
            print("First language:")
            self.add_language(input().capitalize())
            print("Second language:")
            self.add_language(input().capitalize())
            self.languages.remove("two of your choice") # we remove the "two of your choice"

    def is_language_duplicate(self, language): #checks if languague is already in self.languages
        if language in self.languages:
            return True
        return False

    def get_languages(self):
        self.languages = [] # initialize the languages
        self.languages.extend(database.races[self.race]["languages"])
        self.languages.extend(database.backgrounds[self.background]["languages"])
        self.get_extra_language_options() 

    def add_language(self, language):
        if language_check(language):
            if not self.is_language_duplicate(language):
                self.languages.append(language.capitalize())
            else:
                print("Your character already knows that language. Please choose a different language.")
                self.add_language(input().capitalize())
        else:
            print("Please enter a valid language (choose from: " + ", ".join(database.languages) + ").")
            self.add_language(input().capitalize())

    def get_equipment(self):
        self.equipment = [] # initialize the equipment
        self.equipment.extend(database.classes[self.Class]["equipment"])
        self.equipment.extend(database.backgrounds[self.background]["equipment"])
        self.get_equipment_options()
        
    #get every instance of equipment where the user has to choose between multiple options, and then prompt the user to choose between those options, and then store the chosen option in the character object so that we can use that data later when we print the character sheet
    def get_equipment_options(self):
        # this function will check for any extra equipment options that the user can choose based on their class and background, and then prompt the user to choose those options.
        for item in self.equipment:
            index = self.equipment.index(item)
            if "option" in item:
                print("You have an equipment option. Which one do you want to choose? (choose from: " + " OR ".join(item["option"]) + ")")
                choice = input().lower()
                while choice not in item["option"]:
                    print("Please enter a valid choice (choose from: " + " OR ".join(item["option"]) + ").")
                    choice = input().lower()
                self.equipment[index] = choice
                if "choice of" in choice:                    
                    if "simple" in choice:
                        if "melee" in self.equipment[index]:
                            print("You have an equipment option. Which simple melee weapon do you want to choose? (choose from: " + ", ".join(database.weapons["simple"]["melee"]) + ")")                        
                            choice = input().lower()
                            while choice not in database.weapons["simple"]["melee"]:
                                print("Please enter a valid choice (choose from: " + ", ".join(database.weapons["simple"]["melee"]) + ").")
                                choice = input().lower()
                            self.equipment[index] = choice
                        else:
                            print("You have an equipment option. Which simple weapon do you want to choose? (choose from: " + ", ".join(database.weapons["simple"]) + ")")                        
                            choice = input().lower()
                            while choice not in database.weapons["simple"]:
                                print("Please enter a valid choice (choose from: " + ", ".join(database.weapons["simple"]) + ").")
                                choice = input().lower()
                            if choice == "melee":
                                print("choose a simple melee weapon (choose from: " + ", ".join(database.weapons["simple"]["melee"]) + ")")                        
                                choice = input().lower()
                                while choice not in database.weapons["simple"]["melee"]:
                                    print("Please enter a valid choice (choose from: " + ", ".join(database.weapons["simple"]["melee"]) + ").")
                                    choice = input().lower()
                                self.equipment[index] = choice
                            if choice == "ranged":
                                print("choose a simple ranged weapon (choose from: " + ", ".join(database.weapons["simple"]["ranged"]) + ")")                        
                                choice = input().lower()
                                while choice not in database.weapons["simple"]["ranged"]:
                                    print("Please enter a valid choice (choose from: " + ", ".join(database.weapons["simple"]["ranged"]) + ").")
                                    choice = input().lower()
                                self.equipment[index] = choice
                    if "martial" in choice:
                        if "melee" in choice:
                            print("You have an equipment option. Which martial melee weapon do you want to choose? (choose from: " + ", ".join(database.weapons["martial"]["melee"]) + ")")                        
                            choice = input().lower()
                            while choice not in database.weapons["martial"]["melee"]:
                                print("Please enter a valid choice (choose from: " + ", ".join(database.weapons["martial"]["melee"]) + ").")
                                choice = input().lower()
                            self.equipment[index] = choice
                        else:
                            print("You have an equipment option. Which martial weapon do you want to choose? (choose from: " + ", ".join(database.weapons["martial"]) + ")")                        
                            choice = input().lower()
                            if choice not in database.weapons["martial"]:
                                print("Please enter a valid choice (choose from: " + ", ".join(database.weapons["martial"]) + ").")
                                choice = input().lower()
                            if choice == "melee":
                                print("choose a martial melee weapon (choose from: " + ", ".join(database.weapons["martial"]["melee"]) + ")")                        
                                choice = input().lower()
                                while choice not in database.weapons["martial"]["melee"]:
                                    print("Please enter a valid choice (choose from: " + ", ".join(database.weapons["martial"]["melee"]) + ").")
                                    choice = input().lower()
                                self.equipment[index] = choice
                            if choice == "ranged":
                                print("choose a martial ranged weapon (choose from: " + ", ".join(database.weapons["martial"]["ranged"]) + ")")                        
                                choice = input().lower()
                                while choice not in database.weapons["martial"]["ranged"]:
                                    print("Please enter a valid choice (choose from: " + ", ".join(database.weapons["martial"]["ranged"]) + ").")
                                    choice = input().lower()
                                self.equipment[index] = choice
                    if "musical instrument" in choice:
                        print("You have an equipment option. Which musical instrument do you want to choose? (choose from: " + ", ".join(database.musical_instruments) + ")")                        
                        choice = input().lower()
                        while choice not in database.musical_instruments:
                            print("Please enter a valid choice (choose from: " + ", ".join(database.musical_instruments) + ").")
                            choice = input().lower()
                        self.equipment[index] = choice
        