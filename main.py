from characters import captainjack, firstmateanne, customcharacter
    
maxAP_points = 10
print("Pirate Adventure Game")

def main():
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
        pirate_name = input("Enter your pirate name: ")
        character = customcharacter.CustomCharacter(pirate_name)
        print("\nNext, allocate your character's stats.")
        print("\nYou have a total of 10 points to distribute among Strength, Agility, Intelligence, and Luck.")
        print(character.display_stats())
        points_used = 0
        for _ in range(maxAP_points):
            stat_choice = input("Choose a stat to increase\n1) Strength\n2) Agility\n3) Intelligence\n4) Luck ").lower()
            if stat_choice == '1':
                points = int(input("How many points to add to Strength? "))
                if points + character.get_strength() > 10:
                    print("You cannot exceed the maximum of 10 points in any stat.")
                    continue
                points_used += points
                print(points_used)
                character.add_strength(points)
                character.display_stats()
                if points_used == maxAP_points:
                    print("You have used all your points.")
                    break
            elif stat_choice == '2':
                points = int(input("How many points to add to Agility? "))
                if points + character.get_agility() > 10:
                    print("You cannot exceed the maximum of 10 points in any stat.")
                    continue
                points_used += points
                print(points_used)
                character.add_agility(points)
                character.display_stats()
                if points_used == maxAP_points:
                    print("You have used all your points.")
                    break
            elif stat_choice == '3':
                points = int(input("How many points to add to Intelligence? "))
                if points + character.get_intelligence() > 10:
                    print("You cannot exceed the maximum of 10 points in any stat.")
                    continue
                points_used += points
                print(points_used)
                character.add_intelligence(points)
                character.display_stats()
                if points_used == maxAP_points:
                    print("You have used all your points.")
                    break
            elif stat_choice == '4':
                points = int(input("How many points to add to Luck? "))
                if points + character.get_luck() > 10:
                    print("You cannot exceed the maximum of 10 points in any stat.")
                    continue
                points_used += points
                print(points_used)
                character.add_luck(points)
                character.display_stats()
            else:
                print("Invalid choice, try again.")
        
    else:
        print("Invalid choice, defaulting to Captain Jack.")
        character = captainjack

    
    print("\nPreess Enter to continue to start your adventure...")
    play = input()

    print("\nYour adventure begins now!")

if __name__ == "__main__":
    main()