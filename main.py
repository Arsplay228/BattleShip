class Field:
    def __init__(self, size, ships):
        self.size = size
        self.ships_alive = ships
        self.grid = []
        for i in range(size):
            self.grid.append([None] * self.size)

    def display(self, show_ships=False):
        letters = "    A B C D E F G H I J"
        print(letters)
        for i, row in enumerate(self.grid):
            display_row = ""
            for cell in row:
                if cell is None:
                    display_row += "O "
                else:
                    display_row += "■ "
            if i + 1 != 10:
                print(i + 1, " ", display_row)
            else:
                print(i + 1, "", display_row)

Field(10, 1).display()
