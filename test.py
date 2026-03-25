import character

def test_equipments():
    char = character.Character("Test", "Artificer", "Folk Hero", "Elf", 10, 10, 10, 10, 10, 10)
    char.get_data_from_database()
    
    print(char.return_character_sheet())
    
test_equipments()