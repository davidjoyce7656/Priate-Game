class Apple:
    def __init__(self, name="Apple", health_boost=10, energy_boost=5, type="Food"):
        self.name = name
        self.type = type
        self.health_boost = health_boost
        self.energy_boost = energy_boost

    def consume(self, player):
        player.health += self.health_boost
        player.energy += self.energy_boost
        return f"{player.name} ate an apple! Health +{self.health_boost}, Energy +{self.energy_boost}"
