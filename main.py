from inputchecks import background_check, class_check, name_check, race_check, stats_check
import database
import character


def main():
    print("Lets build a character!")
    print("What is your characters name?")
    while not name_check(name := input()):
        print("Please enter a valid name (only letters, between 3 and 20 characters).")
    print("What is your characters class?")
    while not class_check(Class := input()):
        print("Please enter a valid class :" + ", ".join(database.classes.keys()) + ".")
    print("What is your characters background? (only this backgrounds are implemented: " + ", ".join(database.backgrounds.keys()) + ")")
    while not background_check(background := input()):
        print("Please enter a valid background (" + ", ".join(database.backgrounds.keys()) + ").")
    print("What is your characters race? (only this races are implemented: " + ", ".join(database.races.keys()) + ")")
    while not race_check(race := input()):
        print("Please enter a valid race (" + ", ".join(database.races.keys()) + ").")
    print("What are your characters stats? lets start with strength")
    while not stats_check(strength := input()):
        print("Please enter a valid stat (a number between 6 and 18).")
    print("dexterity?")
    while not stats_check(dexterity := input()):
        print("Please enter a valid stat (a number between 6 and 18).")
    print("constitution?")
    while not stats_check(constitution := input()):
        print("Please enter a valid stat (a number between 6 and 18).")
    print("intelligence?")
    while not stats_check(intelligence := input()):
        print("Please enter a valid stat (a number between 6 and 18).")
    print("wisdom?")
    while not stats_check(wisdom := input()):
        print("Please enter a valid stat (a number between 6 and 18).")
    print("charisma?")
    while not stats_check(charisma := input()):
        print("Please enter a valid stat (a number between 6 and 18).")

    print("Your character is being made...")
    # Here we would create the character object and save it to a file or database, but for now we will just print the character sheet.
    char = character.character(name, Class, background, race, int(strength), int(dexterity), int(constitution), int(intelligence), int(wisdom), int(charisma))
    char.race_modifiers()
    print("Name: " + char.name.capitalize())
    print("Class: " + char.Class.capitalize())
    print("Background: " + char.background.capitalize())
    print("Race: " + char.race.capitalize())
    print("Strength: " + str(char.strength))
    print("Dexterity: " + str(char.dexterity))
    print("Constitution: " + str(char.constitution))
    print("Intelligence: " + str(char.intelligence))
    print("Wisdom: " + str(char.wisdom))
    print("Charisma: " + str(char.charisma))



main()