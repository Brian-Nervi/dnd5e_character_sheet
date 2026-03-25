import character

def test_equipments():
    char = character.Character("Test", "fighter", "Folk Hero", "Elf", 10, 10, 10, 10, 10, 10)
    char.get_equipment()
    print(char.equipment)
    
test_equipments()