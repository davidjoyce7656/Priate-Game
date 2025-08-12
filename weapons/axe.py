import random

class Axe:
    def __init__(self, name="Boarding Axe", damage=35):
        self.name = name
        self.damage = damage
        self.durability = 80  # Default durability for the axe
        self.description = "A heavy axe, perfect for chopping through armor and shields."

    def attack(self):
        actual_damage = random.randint(int(self.damage * 0.8), int(self.damage * 1.2))
        self.lose_durability(actual_damage)
        print(f"{self.name} deals {actual_damage} damage. Durability left: {self.durability}")

    def lose_durability(self, amount):
        self.durability = max(0, self.durability - amount)