import random

class Skeleton:
    def __init__(self):
        self._name = "Skeleton Pirate"
        self._health = 50
        self._strength = random.randint(5, 10)
        self._agility = random.randint(3, 7)
        self._intelligence = 2  # skeletons aren’t smart
        self._luck = random.randint(1, 5)
        self._weapon = "Rusty Cutlass"

    def description(self):
        return (f"A cursed skeleton pirate wielding a {self._weapon}. "
                f"It rattles as it moves, eyes glowing faintly.")

    def attack(self):
        base_damage = self._strength + random.randint(0, 3)
        if random.randint(1, 100) <= (self._luck * 2):  # small chance of crit
            print("⚡ The Skeleton lands a CRITICAL HIT!")
            return base_damage * 2
        return base_damage

    def take_damage(self, amount):
        self._health -= amount
        if self._health <= 0:
            print("💀 The Skeleton crumbles into a pile of bones!")
            return True  # enemy defeated
        else:
            print(f"💀 Skeleton has {self._health} HP left.")
            return False

    def is_alive(self):
        return self._health > 0
