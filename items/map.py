class Map:
    def __init__(self, width, height, default_tile='.', name="Map", type="Tool"):
        self.name = name
        self.width = width
        self.height = height
        self.grid = [[default_tile for _ in range(width)] for _ in range(height)]
        self.type = type

    def set_tile(self, x, y, tile):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = tile

    def get_tile(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None

    def display(self):
        for row in self.grid:
            print(' '.join(row))