import character

def test_equipments():
    char = character.Character("Test", "Fighter", "Soldier", "Elf", 10, 10, 10, 10, 10, 10)
    char.get_data_from_database()
    print(char.equipment)   
    #print(char.return_character_sheet())
    
test_equipments()