from sword import Sword
from rifle import Rifle

def test_weapons():
    # Create instances of weapons
    sword = Sword()
    rifle = Rifle()

    # Test sword attack
    print("Testing Sword:")
    sword.attack()
    print()

    # Test rifle attack
    print("\nTesting Rifle:")
    rifle.attack()
    rifle.attack()
    rifle.attack()
    rifle.attack()
    print()
    
if __name__ == "__main__":
    test_weapons()