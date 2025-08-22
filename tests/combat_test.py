from characters.captainjack import CaptainJack
from characters.firstmateanne import FirstMateAnne
from characters.customcharacter import CustomCharacter
from enemies.ruffian import Ruffian
from weapons.sword import Sword


def test_combat():
    print("Testing Combat Mechanics")
    
    # Captain Jack vs Ruffian
    player = CaptainJack()
    enemy = Ruffian()
    print(f"\n{player._name} encounters a {enemy.name}!")
    enemy.take_damage(player.get_strength())
    print(f"{enemy.name} has {enemy.health} health left.")
    enemy.attack(player)
    print(f"{player._name} has {player.health} health left.")

    # First Mate Anne vs Ruffian
    anne = FirstMateAnne()
    enemy2 = Ruffian()
    print(f"\n{anne._name} encounters a {enemy2.name}!")
    enemy2.take_damage(anne.get_strength())
    print(f"{enemy2.name} has {enemy2.health} health left.")
    enemy2.attack(anne)
    print(f"{anne._name} has {anne.health} health left.")

    # Custom Character vs Ruffian
    custom = CustomCharacter("Player Custom", health=100)  # Add health argument
    enemy3 = Ruffian()
    print(f"\n{custom._name} encounters a {enemy3.name}!")
    enemy3.take_damage(custom.get_strength())
    print(f"{enemy3.name} has {enemy3.health} health left.")
    enemy3.attack(custom)
    print(f"{custom._name} has {custom.health} health left.")
    
def test_weapon_pick_up():
    player_character = CaptainJack()
    
    print("\nYou find a sword on the ground.")
    pick = input("Do you want to pick up the sword? (yes/no): ")
    if pick.lower() in ['yes', 'y']:
        sword = Sword()
        player_character.add_item_to_inventory(sword)
    else:
        print("You leave the sword behind.")

    # To check inventory at any time:
    check = input("Do you want to check your inventory? (yes/no): ")
    if check.lower() in ['yes', 'y']:
        player_character.show_inventory()

if __name__ == "__main__":
    test_combat()
    print("\nCombat test completed successfully.")
    
    test_weapon_pick_up()
    print("\nWeapon pick-up test completed successfully.")