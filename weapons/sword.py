import random

class Sword:
    def __init__(self, name="Cutlass", damage=25):
        self.name = name
        self.damage = damage
        self.durability = 100
        self.description = "A sharp sword, perfect for slicing through enemies."

    def attack(self):
        actual_damage = random.randint(int(self.damage * 0.8), int(self.damage * 1.2))
        self.lose_durability(actual_damage)
        print(f"{self.name} deals {actual_damage} damage. Durability left: {self.durability}")

    def lose_durability(self, amount):
        self.durability = max(0, self.durability - amount)
        if self.durability == 0:
            print(f"{self.name} is broken!")

    def __str__(self):
        return f"{self.name} (Damage: {self.damage})"