class FirstMateAnne:
    def __init__(self, strength=5, agility=6, intelligence=9, luck=7):
        self._name = "First Mate Anne"
        self._description = "A skilled navigator and loyal companion, known for her sharp wit and bravery."
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.luck = luck
        
    def name(self):
        return self._name
       
    def description(self):
        return self._description
    
    def special_ability(self):
        return "First Mate Anne can read the stars and navigate through the most treacherous waters. Her ability to find safe passage ensures the crew's survival in the most dangerous of seas."
    
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