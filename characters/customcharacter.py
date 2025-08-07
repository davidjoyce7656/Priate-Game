class CustomCharacter:
    def __init__(self, _name, strength=5, agility=5, intelligence=5, luck=5):
        self._name = _name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.luck = luck
        
    def set_special_ability(self, ability):
        self.special_ability = ability
    
    def display_info(self):
        return f"Name: {self._name}"
    
    def display_stats(self):
        print(f"Strength: {self.strength}\nAgility: {self.agility}\nIntelligence: {self.intelligence}\nLuck: {self.luck}")
    
    def add_strength(self, points):
        self.strength += points
        
    def add_agility(self, points):
        self.agility += points
        
    def add_intelligence(self, points):
        self.intelligence += points
        
    def add_luck(self, points):
        self.luck += points
    
    def get_strength(self):
        return self.strength
    
    def get_agility(self):
        return self.agility
    
    def get_intelligence(self):
        return self.intelligence    
    
    def get_luck(self):
        return self.luck
    