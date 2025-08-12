import random

class Pistol:
    def __init__(self, name="Flintlock Pistol", damage=50):
        self.name = name
        self.damage = damage
        self.ammo = 15  # Default ammo capacity
        self.description = "A classic flintlock pistol, perfect for long-range combat."

    def attack(self):
        actual_damage = random.randint(int(self.damage * 0.8), int(self.damage * 1.2))
        print(f"{self.name} deals {actual_damage} damage. Ammo left: {self.ammo}")
        if self.ammo > 0:
            self.ammo -= 1
        else:
            print(f"{self.name} is out of ammo!")