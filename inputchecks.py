import database


def name_check(name):
    if name_is_alpha(name):
        if (len(name) > 2 and len(name) < 20):
            return True
    return False

def name_is_alpha(name):
    return name.isalpha()

def class_check(Class):
    valid_classes = list(database.classes.keys())
    return Class.lower() in [c.lower() for c in valid_classes]

def background_check(background):
    valid_backgrounds = list(database.backgrounds.keys())
    return background.lower() in [r.lower() for r in valid_backgrounds]

def race_check(race):
    valid_races = list(database.races.keys())
    return race.lower() in [r.lower() for r in valid_races]

def stats_check(stats):
    if stats.isdigit():
        if (int(stats) >= 6 and int(stats) <= 18):
            return True
    return False


 #this is used when you need to check if a choice is valid and if it has been chosen already. 
def validation_check(choice, database_list, char_database_list, type_of_choice):
    if choice.lower() in database_list: # if choice is valid
        if choice.lower() not in char_database_list: # if choice hasnt been chosen already
            print(f"You have chosen {choice} as a {type_of_choice}.")
            return choice # good case
        else: 
            print(f"You have already have {choice} as a {type_of_choice}. Please choose a different {type_of_choice} from ({', '.join([c for c in database_list if c not in char_database_list])}).")
            return None #if choice is valid but has been chosen already return None
    print(f"{choice} is not a valid {type_of_choice}. Please choose a valid {type_of_choice}.")
    return None #if choice is not valid return None
             
    
