from characters import captainjack, firstmateanne, customcharacter
    
print("Pirate Adventure Game")

def main():
    maxAP_points = 10
    print("Welcome to the Pirate Adventure Game!")
    print("You are a brave pirate on a quest for treasure.")
    
    print("Who will you be?")
    print("1. Captain Jack")
    print("2. First Mate Anne")
    print("3. Create your own character")
    choice = input("Choose your character (1, 2 or 3): ")
    if choice == '1':
        character = captainjack.CaptainJack()
        print(f"You are now playing as {character._name}.\n")
        print(character.description())

        print("\nSpecial Ability:")
        print(character.special_ability())

        print("\nCharacter Stats:")
        print("Strength:", character.get_strength())
        print("Agility:", character.get_agility())
        print("Intelligence:", character.get_intelligence())
        print("Luck:", character.get_luck())
    elif choice == '2':
        character = firstmateanne.FirstMateAnne()
        print(f"You are now playing as {character._name}.\n")
        print(character.description())

        print("\nSpecial Ability:")
        print(character.special_ability())

        print("\nCharacter Stats:")
        print("Strength:", character.get_strength())
        print("Agility:", character.get_agility())
        print("Intelligence:", character.get_intelligence())
        print("Luck:", character.get_luck())
    elif choice == '3':
        character_created = False
        while not character_created:
            pirate_name = input("Enter your pirate name: ")
            character = customcharacter.CustomCharacter(pirate_name)
            print("\nNext, allocate your character's stats.")
            print("\nYou have a total of 10 points to distribute among Strength, Agility, Intelligence, and Luck.\n")
            print("*" * 20)
            character.display_stats()
            print("*" * 20)
            points_used = 0
            for _ in range(maxAP_points):
                stat_choice = input("Choose a stat to increase\n1) Strength\n2) Agility\n3) Intelligence\n4) Luck\n").lower()
                if stat_choice == '1':
                    points = int(input("How many points to add to Strength? "))
                    if points + character.get_strength() > 10:
                        print("You cannot exceed the maximum of 10 points in any stat.")
                        continue
                    if points + points_used > maxAP_points:
                        print("Exceeding the maximum points allowed.")
                        continue
                    points_used += points
                    points_remaining = maxAP_points - points_used
                    print("*" * 20)
                    print(f"Points remaining: {points_remaining}")
                    character.add_strength(points)
                    character.display_stats()
                    print("*" * 20)
                    if points_used >= maxAP_points:
                        print("You have used all your points.")
                        break
                elif stat_choice == '2':
                    points = int(input("How many points to add to Agility? "))
                    if points + character.get_agility() > 10:
                        print("You cannot exceed the maximum of 10 points in any stat.")
                        continue
                    if points + points_used > maxAP_points:
                        print("Exceeding the maximum points allowed.")
                        continue
                    points_used += points
                    print(points_used)
                    points_remaining = maxAP_points - points_used
                    print("*" * 20)
                    print(f"Points remaining: {points_remaining}")
                    character.add_agility(points)
                    character.display_stats()
                    print("*" * 20)
                    if points_used >= maxAP_points:
                        print("You have used all your points.")
                        break
                elif stat_choice == '3':
                    points = int(input("How many points to add to Intelligence? "))
                    if points + character.get_intelligence() > 10:
                        print("You cannot exceed the maximum of 10 points in any stat.")
                        continue
                    if points + points_used > maxAP_points:
                        print("Exceeding the maximum points allowed.")
                        continue
                    points_used += points
                    print(points_used)
                    points_remaining = maxAP_points - points_used
                    print("*" * 20)
                    print(f"Points remaining: {points_remaining}")
                    character.add_intelligence(points)
                    character.display_stats()
                    print("*" * 20)
                    if points_used >= maxAP_points:
                        print("You have used all your points.")
                        break
                elif stat_choice == '4':
                    points = int(input("How many points to add to Luck? "))
                    if points + character.get_luck() > 10:
                        print("You cannot exceed the maximum of 10 points in any stat.")
                        continue
                    if points + points_used > maxAP_points:
                        print("Exceeding the maximum points allowed.")
                        continue
                    points_used += points
                    print(points_used)
                    points_remaining = maxAP_points - points_used
                    print("*" * 20)
                    print(f"Points remaining: {points_remaining}")
                    character.add_luck(points)
                    character.display_stats()
                    print("*" * 20)
                    if points_used >= maxAP_points:
                        print("You have used all your points.")
                        break
                else:
                    print("Invalid choice, try again.")
            print("Next, we will choose your special ability.")
            ability_chosen = False
            while not ability_chosen:
                print("1. Sword Mastery")
                print("2. Navigation Expert")
                print("3. Treasure Hunter")
                ability_choice = input("Choose your special ability (1, 2 or 3): ")
                if ability_choice == '1':
                    print("Ability Descirption")
                    print("You have mastered the art of sword fighting, increasing your combat effectiveness.")
                    print("Do you want to set this as your special ability? (yes/no)")
                    confirm = input().lower()
                    if confirm == 'yes' or confirm == 'y':
                        character.set_special_ability("Sword Mastery")
                        print("You have chosen Sword Mastery.")
                        ability_chosen = True
                    else:
                        print("You have not chosen a special ability.")
                elif ability_choice == '2':
                    print("Ability Description")
                    print("You are an expert navigator, allowing you to find hidden paths and shortcuts.")
                    print("Do you want to set this as your special ability? (yes/no)")
                    confirm = input().lower()
                    if confirm == 'yes' or confirm == 'y':
                        character.set_special_ability("Navigation Expert")
                        print("You have chosen Navigation Expert.")
                        ability_chosen = True
                    else:
                        print("You have not chosen a special ability.")
                elif ability_choice == '3':
                    print("Ability Description")
                    print("You have a keen eye for treasure, increasing your chances of finding valuable loot.")
                    print("Do you want to set this as your special ability? (yes/no)")
                    confirm = input().lower()
                    if confirm == 'yes' or confirm == 'y':
                        character.set_special_ability("Treasure Hunter")
                        print("You have chosen Treasure Hunter.")
                        ability_chosen = True
                    else:
                        print("You have not chosen a special ability.")
            print("Character Summary")
            print(character.display_info())
            print(character.display_stats())
            print(f"Special Ability: {character.special_ability}")
            print("If you are happy with your character, press Enter to continue.")
            user_input = input()
            if user_input == "":
                character_created = True
                print("Your character has been created successfully!")
            else:
                print("Let's try creating your character again.")
        
    else:
        print("Invalid choice, defaulting to Captain Jack.")
        character = captainjack

    
    print("\nPreess Enter to continue to start your adventure...")
    play = input()

    print("\nYour adventure begins now!")

if __name__ == "__main__":
    main()