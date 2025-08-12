class Ruffian:
    def __init__(self, name="Ruffian", health=50, attack_power=10):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.description = "A rough and tough enemy, ready to fight."

    def attack(self):
        return self.attack_power

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")