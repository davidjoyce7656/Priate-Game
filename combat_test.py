from characters import captainjack, firstmateanne, customcharacter
from enemies import ruffian
from weapons import sword


def test_combat():
    print("Testing Combat Mechanics")
    
    player = captainjack.CaptainJack()
    enemy = ruffian.Ruffian()
    
    print(f"\n{player._name} encounters a {enemy.name}!")
    enemy.take_damage(player.get_strength())
    print(f"{enemy.name} has {enemy.health} health left.")
    
    print(f"\n{enemy.name} attacks {player._name}!")
    enemy.attack(player)
    print(f"{player._name} has {player.health} health left.")
    
if __name__ == "__main__":
    test_combat()
    print("\nCombat test completed successfully.")