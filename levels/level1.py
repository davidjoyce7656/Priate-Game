from weapons.sword import Sword
from items.apple import Apple
from items.compass import Compass
from items.map import Map
from items.planks import Plank
from enemies.skeleton import Skeleton

import random
#from enemies import Ruffian


# First level of the game
def first_level(player_character):
    enemy_count = random.randint(1, 3)  # Randomly choose how many enemies to spawn
    cave_explored = False
    planks_taken = False
    
    print("Welcome to Level 1: The Pirate's Cove!")
    print("You find yourself at the entrance of a dark cave, rumored to be the hideout of a notorious pirate gang.")
    print("Prepare yourself for the challenges ahead!")
    
    print("\nYou can choose to explore the cave or rest and prepare.")
    choice = input("Do you want to (1) Explore the cave or (2) Rest and prepare? ")
    if choice == '1':
        print("\nYou bravely venture into the cave, ready to face whatever dangers lie ahead.")
        # Here you can add combat encounters, puzzles, or treasure finding logic
        print("As you explore, you discover a sword, should you pick it up? (yes/no): ")
        pick_up = input().lower()
        if pick_up in ['yes', 'y']:
            sword = Sword()
            player_character.add_item_to_inventory(sword)
            print(f"You picked up a {sword.name}.")
        print("\nAhead you can feel a breeze, indicating a way out of the cave. But you also hear noises coming from deeper inside.")
        print("There is a split path: (1) Follow the breeze to exit or (2) Investigate the noises.")
        choice = input("Choose your path (1 or 2): ")
        if choice == '1':
            print("\nYou follow the breeze and find your way out of the cave, escaping safely.")
            print("But now you've relised your stranded on a mysterious island! Wondering, 'How did I get here?'")
            print("Do you want to (1) Explore the island or (2) Rest and prepare?")
            choice = input("Choose your action (1 or 2): ")
            if choice == '1':
                print("\nYou decide to explore the island, looking for resources and a way to signal for help.")
                print("As you explore, you discover a small boat on the shore. It is broken but can be repaired.")
                print("\nYou also find an unlocked chest, should you open it? (Y/N)")
                open_chest = input().lower()
                if open_chest in ['yes', 'y']:
                    print("\nYou open the chest and find some useful supplies: a map, a compass, and some food.")
                    # Here you can add logic to add these items to the player's inventory
                    print("Do you wish to pick these itens up? (yes/no)")
                    pick_items = input().lower()
                    if pick_items in ['yes', 'y']:
                        print()
                        player_character.add_item_to_inventory(Map(5,5))
                        player_character.add_item_to_inventory(Compass())
                        player_character.add_item_to_inventory(Apple())
                    print("\nThese items have been added to your inventory.")
            elif choice == '2':
                print("\nYou decide to rest and prepare. You set up a small camp")
                check = input("Do you want to check your inventory? (yes/no): ")
                if check.lower() in ['yes', 'y']:
                    player_character.show_inventory()
        elif choice == '2':
            print("\nYou decide to investigate the noises, moving cautiously deeper into the cave.")
            print(f"As you go deeper, you encounter {enemy_count} skeletons guarding something behind them!")
            for i in range(enemy_count):
                skeleton = Skeleton()
                print(f"A wild {skeleton._name} appears!")
                while skeleton.is_alive():
                    # Player's turn
                    input("Press Enter to attack...")
                    if random.random() < 0.8:  # 80% chance to hit
                        damage = player_character.get_strength() + random.randint(0, 3)
                        print(f"\nYou attack the {skeleton._name} for {damage} damage!")
                        if skeleton.take_damage(damage):
                            break
                    else:
                        print(f"You swing at the {skeleton._name}, but miss!")
                 # Skeleton's turn (if still alive)
                    if skeleton.is_alive():
                        input("Press Enter to continue...")
                        if random.random() < 0.7:  # 70% chance to hit
                            enemy_damage = skeleton.attack()
                            print(f"\nThe {skeleton._name} attacks you for {enemy_damage} damage!")
                            player_character.take_damage(enemy_damage)
                            if player_character.health <= 0:
                                print("You have been defeated! Game Over.")
                                return
                        else:
                            print(f"\nThe {skeleton._name} swings at you, but misses!")
            print("\nYou defeat the skeletons and find planks. Do you want to take them? They could come useful later? (yes/no)")
            take_planks = input().lower()
            if take_planks in ['yes', 'y']:
                planks_taken = True
                cave_explored = True
                print("\nYou take the planks, they might be useful later.")
                player_character.add_item_to_inventory(Plank())
                
    elif choice == '2':
        print("\nYou decide to rest and prepare. You sharpen your sword and check your supplies.")
        check = input("Do you want to check your inventory? (yes/no): ")
        if check.lower() in ['yes', 'y']:
            player_character.show_inventory()
    if not cave_explored:        
        print("\nDo you wish to eplore more of the island or set up a camp for the night?")
        choice = input("Choose your action (1 to explore, 2 to camp): ")
        if choice == '1':
            print("\nYou decide to explore more of the island, looking for resources and a way to signal for help.")
            print("You remembered, there was a path you saw earlier that led deeper into the cave. Should you investigate it? (yes/no):")
            investigate = input().lower()
            if investigate in ['yes', 'y']:
                print("You venture back into the cave, following the path you saw earlier.")
                print(f"As you go deeper, you encounter {enemy_count} sskeletons guarding something behind them!")
                for i in range(enemy_count):
                    skeleton = Skeleton()
                    print(f"A wild {skeleton._name} appears!")
                    while skeleton.is_alive():
                        # Player's turn
                        input("Press Enter to attack...")
                        if random.random() < 0.8:  # 80% chance to hit
                            damage = player_character.get_strength() + random.randint(0, 3)
                            print(f"\nYou attack the {skeleton._name} for {damage} damage!")
                            if skeleton.take_damage(damage):
                                break
                        else:
                            print(f"You swing at the {skeleton._name}, but miss!")

                        # Skeleton's turn (if still alive)
                        if skeleton.is_alive():
                            input("Press Enter to continue...")
                            if random.random() < 0.4:  # 40% chance to hit
                                enemy_damage = skeleton.attack()
                                print(f"\nThe {skeleton._name} attacks you for {enemy_damage} damage!")
                                player_character.take_damage(enemy_damage)
                                if player_character.health <= 0:
                                    print("You have been defeated! Game Over.")
                                    return
                            else:
                                print(f"\nThe {skeleton._name} swings at you, but misses!")
            print("\nYou defeat the skeletons and find planks. Do you want to take them? They could come useful later? (yes/no)")
            take_planks = input().lower()
            if take_planks in ['yes', 'y']:
                planks_taken = True
                cave_explored = True
                print("\nYou take the planks, they might be useful for repairing the boat.")
                player_character.add_item_to_inventory(Plank())
        else:
            if cave_explored == True and planks_taken == True:
                print("\nYou set up a camp for the night, resting and preparing for the challenges ahead.")
            print()