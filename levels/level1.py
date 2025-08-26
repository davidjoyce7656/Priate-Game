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
    chest_opened = False
    planks_taken = False
    
    print("Welcome to Level 1: The Pirate's Cove!")
    print("\nYou wake up in a dimly lit cave, the sound of waves crashing against the shore echoes in the distance.")
    print("Wondering how you got here, you decide to explore your surroundings.")
    
    while not cave_explored:
        print("\nYou see a narrow path leading out of the cave and a small chest in the corner.")
        choice = input("Do you want to (1) explore the cave or (2) open the chest ('i' to check inventory)? ")
        
        while chest_opened == False:
            if choice == '1':
                print("\nYou decide to explore the cave first.")
                print("As you walk deeper into the cave, you notice the walls are damp and covered in moss.")
                print("Suddenly, you hear a noise behind you. You turn around to see a group of skeleton pirates emerging from the shadows!")
                print(f"There are {enemy_count} skeleton pirates!")
                print("You relised you have no weapon to fight them with.")
                print("You run back to the cave entrance to open the chest.")
                break
            elif choice == '2':
                print("\nYou open the chest and find a few useful items inside.")
                player_character.add_item_to_inventory(Apple())
                player_character.add_item_to_inventory(Compass())
                player_character.add_item_to_inventory(Map(5, 5))
                print("You take an apple, a compass, and a map from the chest.")
                chest_opened = True
            elif choice.lower() == 'i':
                player_character.show_inventory()
                break
            else:
                print("Invalid choice, please try again.")
        
            if chest_opened == True:          
                while not cave_explored:
                    print("\nYou decide to continue exploring the cave.")
                    print("You found a sword on the ground along the way and pick it up.")
                    sword = Sword()
                    player_character.add_item_to_inventory(sword)
                    print("\nYou then come to a fork in the path of the cave. The path on left looks dark and ominous, while the path on the right is dimly lit by glowing fungi.")
                    fork_choice = input("Do you want to go (1) left or (2) right ('i' to check inventory)? ")
                    if fork_choice == '1':
                        print("\nYou venture down the dark path, your heart pounding with each step.")
                        print("Suddenly, you hear a low growl and see a pair of glowing eyes staring at you from the shadows.")
                        print("A wild skeleton appears!")
                        skeleton = Skeleton()
                        while skeleton.is_alive() and player_character.health > 0:
                            action = input("Do you want to (1) attack or (2) flee? ")
                            if action == '1':
                                damage = random.randint(5, 15) + player_character.get_strength()
                                print(f"You attack the skeleton for {damage} damage!")
                                if skeleton.take_damage(damage):
                                    print("You have defeated the skeleton!")
                                    break
                                enemy_damage = skeleton.attack()
                                player_character.take_damage(enemy_damage)
                            elif action == '2':
                                print("You flee back to the cave entrance.")
                                break
                            else:
                                print("Invalid choice, please try again.")
                    elif fork_choice == '2':
                        print("\nYou walk down the dimly lit path, the glowing fungi casting eerie shadows on the walls.")
                        print("As you proceed, you find a pile of wooden planks that look sturdy enough to use.")
                        take_planks = input("Do you want to take the planks? (yes/no) ")
                        if take_planks.lower() in ['yes', 'y']:
                            player_character.add_item_to_inventory(Plank())
                            planks_taken = True
                            if planks_taken == True and cave_explored != True:
                                print("You turn back to the fork in the cave and take the left path.")
                                print("\nYou venture down the dark path, your heart pounding with each step.")
                        print("Suddenly, you hear a low growl and see a pair of glowing eyes staring at you from the shadows.")
                        print("A wild skeleton appears!")
                        skeleton = Skeleton()
                        while skeleton.is_alive() and player_character.health > 0:
                            action = input("Do you want to (1) attack or (2) flee? ")
                            if action == '1':
                                damage = random.randint(5, 15) + player_character.get_strength()
                                print(f"You attack the skeleton for {damage} damage!")
                                if skeleton.take_damage(damage):
                                    print("You have defeated the skeleton!")
                                    break
                                enemy_damage = skeleton.attack()
                                player_character.take_damage(enemy_damage)
                            elif action == '2':
                                print("You flee back to the cave entrance.")
                                break
                            else:
                                print("Invalid choice, please try again.")
                        else:
                            break
                        print("You eventually find your way out of the cave and onto a sandy beach.")
                        cave_explored = True
                    elif fork_choice.lower() == 'i':
                        player_character.show_inventory()
    
    print("\nYou have successfully navigated through the cave and reached the beach.")
    