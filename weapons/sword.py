class Sword:
    def __init__(self, name="Basic Sword", damage=5):
        self.name = name
        self.damage = damage
        self.durability = 100  # Default durability

    def attack(self):
        return f"{self.name} deals {self.damage} damage."
    
    
    def __str__(self):
        return f"{self.name} (Damage: {self.damage})"