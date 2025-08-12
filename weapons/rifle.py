import random

class Rifle:
    def __init__(self, name="Blunderbuss", damage=70):
        self.name = name
        self.damage = damage
        self.ammo = 10
        self.description = "A reliable rifle for long-range combat."

    def attack(self):
        actual_damage = random.randint(int(self.damage * 0.8), int(self.damage * 1.2))
        print(f"{self.name} deals {actual_damage} damage. Ammo left: {self.ammo}")
        if self.ammo > 0:
            self.ammo -= 1
        else:
            print(f"{self.name} is out of ammo!")