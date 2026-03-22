import database

class character:
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

        