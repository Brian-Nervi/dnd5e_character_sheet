races = {
    "Human": {"size": "medium", "speed": 30, "ability_score_increase": {"all": 1}, "languages": ["Common", "one extra"]},
    "Elf": {"size": "medium", "speed": 30, "ability_score_increase": {"dexterity": 2}, "languages": ["Common", "Elvish"]},
    "Dwarf": {"size": "medium", "speed": 25, "ability_score_increase": {"constitution": 2}, "languages": ["Common", "Dwarvish"]},
    "Halfling": {"size": "small", "speed": 25, "ability_score_increase": {"dexterity": 2}, "languages": ["Common", "Halfling"]},
    "Dragonborn": {"size": "medium", "speed": 30, "ability_score_increase": {"strength": 2, "charisma": 1}, "languages": ["Common", "Draconic"]},
    "Gnome": {"size": "small", "speed": 25, "ability_score_increase": {"intelligence": 2}, "languages": ["Common", "Gnomish"]},
    "Half-elf": {"size": "medium", "speed": 30, "ability_score_increase": {"charisma": 2, "any_other_1": 1, "any_other_2": 1}, "languages": ["Common", "Elvish", "one extra"]},
    "Half-orc": {"size": "medium", "speed": 30, "ability_score_increase": {"strength": 2, "constitution": 1}, "languages": ["Common", "Orcish"]},
    "Tiefling": {"size": "medium", "speed": 30, "ability_score_increase": {"charisma": 2, "intelligence": 1}, "languages": ["Common", "Infernal"]}
}

backgrounds = {
    "Acolyte": {"skill_proficiencies": ["Insight", "Religion"], "tools": [""], "languages": ["two of your choice"], "equipment": ["a holy symbol", "a prayer book", "5 sticks of incense", "vestments", "common clothes", "pouch (15gp)"]},
    "Charlatan": {"skill_proficiencies": ["Deception", "Performance"], "tools": ["disguise kit", "forgery kit"], "languages": [""], "equipment": ["fine clothes", "disguise kit", "tools of con of choice", "pouch (15gp)"]},
    "Criminal": {"skill_proficiencies": ["Deception", "Stealth"], "tools": ["one type of gaming set", "thieves' tools"], "languages": [""], "equipment": ["a crowbar", "dark common clothes with hood", "pouch (15gp)"]},
    "Entertainer": {"skill_proficiencies": ["Acrobatics", "Performance"], "tools": ["disguise kit", "one type of musical instrument"], "languages": [""], "equipment": ["a musical instrument", "favor of an admirer", "costume", "pouch (15gp)"]},
    "Folk Hero": {"skill_proficiencies": ["Animal Handling", "Survival"], "tools": ["one type of artisan's tools", "vehicles (land)"], "languages": [""], "equipment": ["artisan's tools", "a shovel", "an iron pot", "common clothes", "pouch (10gp)"]},
    "Guild Artisan": {"skill_proficiencies": ["Insight", "Persuasion"], "tools": ["one type of artisan's tools"], "languages": ["one of your choice"], "equipment": ["artisan's tools", "letter of introduction", "traveler's clothes", "pouch (15gp)"]},
    "Hermit": {"skill_proficiencies": ["Medicine", "Religion"], "tools": ["herbalism kit"], "languages": ["one of your choice"], "equipment": ["a winter blanket", "common clothes", "herbalism kit", "notes of study", "pouch (5gp)"]},
    "Noble": {"skill_proficiencies": ["History", "Persuasion"], "tools": ["one type of gaming set"], "languages": ["one of your choice"], "equipment": ["fine clothes", "signet ring", "scroll of pedigree", "pouch (25gp)"]},
    "Outlander": {"skill_proficiencies": ["Athletics", "Survival"], "tools": ["one type of musical instrument"], "languages": ["one of your choice"], "equipment": ["a staff", "a hunting trap", "trophy from an animal", "traveler's clothes", "pouch (10gp)"]},
    "Sage": {"skill_proficiencies": ["Arcana", "History"], "tools": [""], "languages": ["two of your choice"], "equipment": ["bottle of ink", "a quill", "a small knife", "letter from a dead colleague", "common clothes", "pouch (10gp)"]},
    "Sailor": {"skill_proficiencies": ["Athletics", "Perception"], "tools": ["navigator's tools", "vehicles (water)"], "languages": [""], "equipment": ["a belaying pin (club)", "50ft silk rope", "lucky charm", "common clothes", "pouch (10gp)"]},
    "Soldier": {"skill_proficiencies": ["Athletics", "Intimidation"], "tools": ["one type of gaming set", "vehicles (land)"], "languages": [""], "equipment": ["insignia of rank", "trophy from fallen enemy", "bone dice or deck of cards", "common clothes", "pouch (10gp)"]},
    "Urchin": {"skill_proficiencies": ["Sleight of Hand", "Stealth"], "tools": ["disguise kit", "thieves' tools"], "languages": [""], "equipment": ["a small knife", "map of your home city", "a pet mouse", "token of parents", "common clothes", "pouch (10gp)"]},
}

classes = {
    "Barbarian": {"hit_die": 12, "primary_ability": "Strength"},
    "Bard": {"hit_die": 8, "primary_ability": "Charisma"},
    "Druid": {"hit_die": 8, "primary_ability": "Wisdom"},
    "Fighter": {"hit_die": 10, "primary_ability": "Strength or Dexterity"},
    "Monk": {"hit_die": 8, "primary_ability": "Dexterity and Wisdom"},
    "Paladin": {"hit_die": 10, "primary_ability": "Strength and Charisma"},
    "Ranger": {"hit_die": 10, "primary_ability": "Dexterity and Wisdom"},
    "Rogue": {"hit_die": 8, "primary_ability": "Dexterity"},
    "Sorcerer": {"hit_die": 6, "primary_ability": "Charisma"},
    "Warlock": {"hit_die": 8, "primary_ability": "Charisma"},
    "Wizard": {"hit_die": 6, "primary_ability": "Intelligence"},
    "artificer": {"hit_die": 8, "primary_ability": "Intelligence"}
}