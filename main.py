class Field:
    def __init__(self, size, ships):
        self.size = size
        self.ships_alive = ships
        self.grid = []
        for i in range(size):
            self.grid.append([None] * self.size)

