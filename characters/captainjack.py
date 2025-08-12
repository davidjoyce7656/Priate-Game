class CaptainJack:
    def __init__(self, strength=6, agility=8, intelligence=7, luck=9, health=100):
        self._name = "Captain Jack"
        self._description = "Captain Jack is a legendary pirate known for his daring escapades and unmatched skill in navigation. With his trusty sword and a heart full of courage, he leads his crew through treacherous waters in pursuit of the greatest treasures the world has to offer."
        self.strength = strength
        self.agility = agility 
        self.intelligence = intelligence
        self.luck = luck
        self.health = health

    def name(self):
        return self._name

    def description(self):
        return self._description
    
    def special_ability(self):
        return "Captain Jack can charm his way out of any situation, gaining the trust of even the most hardened sailors. His charisma allows him to gather information and resources that others might miss."
    
    def display_stats(self):
        return f"Strength: {self.strength}\nAgility: {self.agility}\nIntelligence: {self.intelligence}\nLuck: {self.luck}"
    
    def get_strength(self):
        return self.strength
    
    def get_agility(self):
        return self.agility
    
    def get_intelligence(self):
        return self.intelligence
    
    def get_luck(self):
        return self.luck
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self._name} takes {damage} damage! Health left: {self.health}")
        if self.health <= 0:
            print(f"{self._name} has been defeated!")