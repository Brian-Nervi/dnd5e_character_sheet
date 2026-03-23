from inputchecks import background_check, class_check, name_check, race_check, stats_check
import database
import character


def main():
    char = character.Character("", "", "", "", 0, 0, 0, 0, 0, 0) # we need to initialize the character object before we can use it, but we will overwrite these values with the user input later.
    print("Lets build a character!")
    print("What is your characters name?")
    while not name_check(name := input()):
        print("Please enter a valid name (only letters, between 3 and 20 characters).")
    char.name = name.capitalize() 
    print("What is your characters class?")
    while not class_check(Class := input()):
        print("Please enter a valid class :" + ", ".join(database.classes.keys()) + ".")
    char.Class = Class.capitalize() 
    print("What is your characters background? (only this backgrounds are implemented: " + ", ".join(database.backgrounds.keys()) + ")")
    while not background_check(background := input()):
        print("Please enter a valid background (" + ", ".join(database.backgrounds.keys()) + ").")
    char.background = background.capitalize() 
    print("What is your characters race? (only this races are implemented: " + ", ".join(database.races.keys()) + ")")
    while not race_check(race := input()):
        print("Please enter a valid race (" + ", ".join(database.races.keys()) + ").")
    char.race = race.capitalize() 
    for stat in ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]:
        print(f"What is your characters {stat}?")
        while not stats_check(stat_value := input()):
            print("Please enter a valid stat (a number between 6 and 18).")
        char.__setattr__(stat, int(stat_value))   
    char.get_data_from_database()# we need to get the data from the database before we can print the character sheet, otherwise the equipment, languages, skill proficiencies, and tool proficiencies will be missing from the character sheet.
    
    print("\nYour character is being made...\n")
    print(char.return_character_sheet())



main()