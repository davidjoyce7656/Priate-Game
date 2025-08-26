class Compass:
    """
    A simple Compass item for the Pirate Game.
    """

    def __init__(self, name="Compass", direction="North", type="Tool"):
        self.name = name
        self.direction = direction
        self.type = type

    def set_direction(self, direction):
        """
        Set the compass to point to a new direction.
        """
        self.direction = direction

    def get_direction(self):
        """
        Get the current direction the compass is pointing to.
        """
        return self.direction

    def __str__(self):
        return f"Compass pointing {self.direction}"