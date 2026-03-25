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
    "Acolyte": {
        "skill_proficiencies": ["insight", "religion"],
        "tools": [],
        "languages": ["two of your choice"],
        "equipment": ["a holy symbol", "a prayer book", "5 sticks of incense", "vestments", "common clothes"],
        "gold": 15
    },
    "Charlatan": {
        "skill_proficiencies": ["deception", "performance"],
        "tools": ["disguise kit", "forgery kit"],
        "languages": [],
        "equipment": ["fine clothes", "disguise kit", "choice of tools of con"],
        "gold": 15
    },
    "Criminal": {
        "skill_proficiencies": ["deception", "stealth"],
        "tools": ["choice of gaming set", "thieves' tools"],
        "languages": [],
        "equipment": ["a crowbar", "dark common clothes with hood"],
        "gold": 15
    },
    "Entertainer": {
        "skill_proficiencies": ["acrobatics", "performance"],
        "tools": ["disguise kit", "choice of musical instrument"],
        "languages": [],
        "equipment": ["choice of musical instrument", "favor of an admirer", "costume"],
        "gold": 15
    },
    "Folk hero": {
        "skill_proficiencies": ["animal handling", "survival"],
        "tools": ["choice of artisan's tools", "vehicles (land)"],
        "languages": [],
        "equipment": ["artisan's tools", "a shovel", "an iron pot", "common clothes"],
        "gold": 10
    },
    "Guild artisan": {
        "skill_proficiencies": ["insight", "persuasion"],
        "tools": ["choice of artisan's tools"],
        "languages": ["one of your choice"],
        "equipment": ["artisan's tools", "letter of introduction", "traveler's clothes"],
        "gold": 15
    },
    "Hermit": {
        "skill_proficiencies": ["medicine", "religion"],
        "tools": ["herbalism kit"],
        "languages": ["one of your choice"],
        "equipment": ["a winter blanket", "common clothes", "herbalism kit", "notes of study"],
        "gold": 5
    },
    "Noble": {
        "skill_proficiencies": ["history", "persuasion"],
        "tools": ["choice of gaming set"],
        "languages": ["one of your choice"],
        "equipment": ["fine clothes", "signet ring", "scroll of pedigree"],
        "gold": 25
    },
    "Outlander": {
        "skill_proficiencies": ["athletics", "survival"],
        "tools": ["choice of musical instrument"],
        "languages": ["one of your choice"],
        "equipment": ["a staff", "a hunting trap", "trophy from an animal", "traveler's clothes"],
        "gold": 10
    },
    "Sage": {
        "skill_proficiencies": ["arcana", "history"],
        "tools": [],
        "languages": ["two of your choice"],
        "equipment": ["bottle of ink", "a quill", "a small knife", "letter from a dead colleague", "common clothes"],
        "gold": 10
    },
    "Sailor": {
        "skill_proficiencies": ["athletics", "perception"],
        "tools": ["navigator's tools", "vehicles (water)"],
        "languages": [],
        "equipment": ["a belaying pin (club)", "50ft silk rope", "lucky charm", "common clothes"],
        "gold": 10
    },
    "Soldier": {
        "skill_proficiencies": ["athletics", "intimidation"],
        "tools": ["choice of gaming set", "vehicles (land)"],
        "languages": [],
        "equipment": ["insignia of rank", "trophy from fallen enemy", "bone dice or deck of cards", "common clothes"],
        "gold": 10
    },
    "Urchin": {
        "skill_proficiencies": ["sleight of hand", "stealth"],
        "tools": ["disguise kit", "thieves' tools"],
        "languages": [],
        "equipment": ["a small knife", "map of your home city", "a pet mouse", "token of parents", "common clothes"],
        "gold": 10
    }
}
 
classes = {
    "Artificer": {
        "hit_die": 8,
        "equipment": [
            "choice of two simple weapons",
            "light crossbow and 20 bolts",
            {"option": ["studded leather armor", "scale mail"]},
            "thieves' tools",
            "dungeoneer's pack"
        ],
        "proficiencies": {
            "armor": ["light", "medium", "shields"],
            "weapons": ["simple", "firearms"],
            "tools": ["thieves' tools", "tinker's tools", "choice of artisan's tools"],
            "saving_throws": ["CON", "INT"],
            "skills": {"count": 2, "options": ["Arcana", "History", "Investigation", "Medicine", "Nature", "Perception", "Sleight of Hand"]}
        }
    },
    "Barbarian": {
        "hit_die": 12,
        "equipment": [
            {"option": ["greataxe", "choice of martial melee weapon"]},
            {"option": ["two handaxes", "choice of simple weapon"]},
            "explorer's pack",
            "four javelins"
        ],
        "proficiencies": {
            "armor": ["light", "medium", "shields"],
            "weapons": ["simple", "martial"],
            "tools": [],
            "saving_throws": ["STR", "CON"],
            "skills": {"count": 2, "options": ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]}
        }
    },
    "Bard": {
        "hit_die": 8,
        "equipment": [
            {"option": ["rapier", "longsword", "choice of simple weapon"]},
            {"option": ["diplomat's pack", "entertainer's pack"]},
            {"option": ["lute", "choice of other musical instrument"]},
            "leather armor",
            "dagger"
        ],
        "proficiencies": {
            "armor": ["light"],
            "weapons": ["simple", "hand crossbows", "longswords", "rapiers", "shortswords"],
            "tools": ["choice of musical intstrument","choice of musical intstrument","choice of musical intstrument"],
            "saving_throws": ["DEX", "CHA"],
            "skills": {"count": 3, "options": ["Any"]}
        }
    },
    "Cleric": {
        "hit_die": 8,
        "equipment": [
            {"option": ["mace", "warhammer"]},
            {"option": ["scale mail", "leather armor", "chain mail"]},
            {"option": ["light crossbow and 20 bolts", "choice of simple weapon"]},
            {"option": ["priest's pack", "explorer's pack"]},
            "shield",
            "holy symbol"
        ],
        "proficiencies": {
            "armor": ["light", "medium", "shields"],
            "weapons": ["simple"],
            "tools": [],
            "saving_throws": ["WIS", "CHA"],
            "skills": {"count": 2, "options": ["History", "Insight", "Medicine", "Persuasion", "Religion"]}
        }
    },
    "Druid": {
        "hit_die": 8,
        "equipment": [
            {"option": ["wooden shield", "choice of simple weapon"]},
            {"option": ["scimitar", "choice of simple melee weapon"]},
            "leather armor",
            "explorer's pack",
            "druidic focus"
        ],
        "proficiencies": {
            "armor": ["light", "medium", "shields (non-metal)"],
            "weapons": ["clubs", "daggers", "darts", "javelins", "maces", "quarterstaffs", "scimitars", "sickles", "slings", "spears"],
            "tools": ["herbalism kit"],
            "saving_throws": ["INT", "WIS"],
            "skills": {"count": 2, "options": ["Animal Handling", "Arcana", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"]}
        }
    },
    "Fighter": {
        "hit_die": 10,
        "equipment": [
            {"option": ["chain mail", "leather armor, longbow and 20 arrows"]},
            {"option": ["choice of martial weapon and a shield", "choice of two martial weapons"]},
            {"option": ["light crossbow and 20 bolts", "two handaxes"]},
            {"option": ["dungeoneer's pack", "explorer's pack"]}
        ],
        "proficiencies": {
            "armor": ["all armor", "shields"],
            "weapons": ["simple", "martial"],
            "tools": [],
            "saving_throws": ["STR", "CON"],
            "skills": {"count": 2, "options": ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"]}
        }
    },
    "Monk": {
        "hit_die": 8,
        "equipment": [
            {"option": ["shortsword", "choice of simple weapon"]},
            {"option": ["dungeoneer's pack", "explorer's pack"]},
            "10 darts"
        ],
        "proficiencies": {
            "armor": ["none"],
            "weapons": ["simple", "shortswords"],
            "tools": ["choice of one type of artisan's tools or choice ofmusical instrument"],
            "saving_throws": ["STR", "DEX"],
            "skills": {"count": 2, "options": ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"]}
        }
    },
    "Paladin": {
        "hit_die": 10,
        "equipment": [
            {"option": ["choice of martial weapon and a shield", "choice of two martial weapons"]},
            {"option": ["five javelins", "choice of simple melee weapon"]},
            {"option": ["priest's pack", "explorer's pack"]},
            "chain mail",
            "holy symbol"
        ],
        "proficiencies": {
            "armor": ["all armor", "shields"],
            "weapons": ["simple", "martial"],
            "tools": [],
            "saving_throws": ["WIS", "CHA"],
            "skills": {"count": 2, "options": ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"]}
        }
    },
    "Ranger": {
        "hit_die": 10,
        "equipment": [
            {"option": ["scale mail", "leather armor"]},
            {"option": ["two shortswords", "choice of two simple melee weapons"]},
            {"option": ["dungeoneer's pack", "explorer's pack"]},
            "longbow and a quiver of 20 arrows"
        ],
        "proficiencies": {
            "armor": ["light", "medium", "shields"],
            "weapons": ["simple", "martial"],
            "tools": [],
            "saving_throws": ["STR", "DEX"],
            "skills": {"count": 3, "options": ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"]}
        }
    },
    "Rogue": {
        "hit_die": 8,
        "equipment": [
            {"option": ["rapier", "shortsword"]},
            {"option": ["shortbow and 20 arrows", "shortsword"]},
            {"option": ["burglar's pack", "dungeoneer's pack", "explorer's pack"]},
            "leather armor",
            "two daggers",
            "thieves' tools"
        ],
        "proficiencies": {
            "armor": ["light"],
            "weapons": ["simple", "hand crossbows", "longswords", "rapiers", "shortswords"],
            "tools": ["thieves' tools"],
            "saving_throws": ["DEX", "INT"],
            "skills": {"count": 4, "options": ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"]}
        }
    },
    "Sorcerer": {
        "hit_die": 6,
        "equipment": [
            {"option": ["light crossbow and 20 bolts", "choice of simple weapon"]},
            {"option": ["component pouch", "arcane focus"]},
            {"option": ["dungeoneer's pack", "explorer's pack"]},
            "two daggers"
        ],
        "proficiencies": {
            "armor": ["none"],
            "weapons": ["daggers", "darts", "slings", "quarterstaffs", "light crossbows"],
            "tools": [],
            "saving_throws": ["CON", "CHA"],
            "skills": {"count": 2, "options": ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"]}
        }
    },
    "Warlock": {
        "hit_die": 8,
        "equipment": [
            {"option": ["light crossbow and 20 bolts", "choice of simple weapon"]},
            {"option": ["component pouch", "arcane focus"]},
            {"option": ["scholar's pack", "dungeoneer's pack"]},
            "leather armor",
            "choice of simple weapon",
            "two daggers"
        ],
        "proficiencies": {
            "armor": ["light"],
            "weapons": ["simple"],
            "tools": [],
            "saving_throws": ["WIS", "CHA"],
            "skills": {"count": 2, "options": ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"]}
        }
    },
    "Wizard": {
        "hit_die": 6,
        "equipment": [
            {"option": ["quarterstaff", "dagger"]},
            {"option": ["component pouch", "arcane focus"]},
            {"option": ["scholar's pack", "explorer's pack"]},
            "spellbook"
        ],
        "proficiencies": {
            "armor": ["none"],
            "weapons": ["daggers", "darts", "slings", "quarterstaffs", "light crossbows"],
            "tools": [],
            "saving_throws": ["INT", "WIS"],
            "skills": {"count": 2, "options": ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]}
        }
    }
}

languages = ["Common", "Dwarvish", "Elvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orc", "Abyssal", "Celestial", "Draconic", "Deep Speech", "Infernal", "Primordial", "Sylvan", "Undercommon"]


weapons = {
    "martial":{
        "melee": ["battleaxe", "flail", "glaive", "greataxe", "greatsword", "halberd", "lance", "longsword", "maul", "morningstar", "pike", "rapier", "scimitar", "shortsword", "trident", "war pick", "warhammer", "whip"],
        "ranged": ["blowgun", "hand crossbow", "heavy crossbow", "longbow", "net"]
    },
    "simple":{
        "melee": ["club", "dagger", "greatclub", "handaxe", "javelin", "light hammer", "mace", "quarterstaff", "sickle", "spear"],
        "ranged": ["light crossbow", "dart", "shortbow", "sling"]

    }
}

musical_instruments = ["bagpipes", "drum", "dulcimer", "flute", "lute", "lyre", "horn", "pan flute", "shawm", "viol"]

tools_of_con = ["disguise kit", "forgery kit", "choice of gaming set", "poker set"]

gaming_sets = ["dice set", "dragonchess set", "playing card set", "three-dragon ante set"]

skills = ["acrobatics", "animal handling", "arcana", "athletics", "deception", "history", "insight", "intimidation", "investigation", "medicine", "nature", "perception", "performance", "persuasion", "religion", "sleight of hand", "stealth", "survival"]

tools = ["alchemist's supplies", "brewer's supplies", "calligrapher's supplies", "carpenter's tools", "cartographer's tools", "cobbler's tools", "cook's utensils", "glassblower's tools", "jeweler's tools", "leatherworker's tools", "mason's tools", "smith's tools", "tinker's tools", "weaver's tools", "woodcarver's tools"]