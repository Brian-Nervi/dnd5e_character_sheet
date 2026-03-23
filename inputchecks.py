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

def language_check(language): #only checks if the language is valid, does not check for duplicates. returns True or false if false
    valid_languages = database.languages
    return language.capitalize() in [l.capitalize() for l in valid_languages]

