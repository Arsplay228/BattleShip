import random
from dataclasses import field


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
                if cell == "X":
                    display_row += "X "
                elif cell == "#":
                    display_row += "# "
                elif cell == "S":
                    display_row += "■ " if show_ships else "O "
                else:
                    display_row += "O "
            if i + 1 != 10:
                print(i + 1, " ", display_row)
            else:
                print(i + 1, "", display_row)


class BattleshipGame:
    def __init__(self):
        self.size = 10
        self.ships = 15
        self.player_field = Field(self.size, self.ships)
        self.computer_field = Field(self.size, self.ships)
        self.play()

    # Это функция расстановки кораблей, она уже полностью написана
    def place_ships_randomly(self, field, num_ships):
        for _ in range(num_ships):
            placed = False
            while not placed:
                x = random.randint(0, self.size - 1)
                y = random.randint(0, self.size - 1)
                coords = (x, y)

                if self.is_valid_ship_placement(field, coords):
                    field.grid[coords[0]][coords[1]] = "S"
                    placed = True

    # Это функция проверки расстановки кораблей, она уже полностью написана
    def is_valid_ship_placement(self, field, coords, ship_length=1, ):
        x, y = coords

        # Проверка на наличие соседних клеток по горизонтали и вертикали
        for i in range(ship_length + 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    new_x, new_y = x + j, y + k
                    if 0 <= new_x < self.size and 0 <= new_y < self.size and field.grid[new_x][new_y] == "S":
                        return False

        return True

    def play(self):
        print("Расстановка кораблей компьютера:")
        self.place_ships_randomly(self.computer_field, self.ships)
        self.computer_field.display(show_ships=False)

        print("Ваша расстановка кораблей:")
        self.place_ships_randomly(self.player_field, self.ships)
        self.player_field.display(show_ships=True)

        while True:
            x = input("Введите букву")
            y = int(input("Введите число"))

            self.player_turn(x, y)
            print("Расстановка кораблей компьютера:")
            self.computer_field.display(show_ships=False)
            print("Ваша расстановка кораблей:")
            self.player_field.display(show_ships=True)

            if self.computer_field.ships_alive <= 1:
                print("Вы победили!")
                break

            self.computer_turn()
            print("Расстановка кораблей компьютера:")
            self.computer_field.display(show_ships=False)
            print("Ваша расстановка кораблей:")
            self.player_field.display(show_ships=True)

            if self.player_field.ships_alive <= 1:
                print("Вы проиграли!")
                break

    def player_turn(self, x, y):
        letters = "ABCDEFGHIJ"
        x_index = letters.index(x.upper())
        y_index = y - 1
        cell = self.computer_field.grid[y_index][x_index]
        if cell == "S":
            print("Вы попали!")
            self.computer_field.grid[y_index][x_index] = "X"
            self.computer_field.ships_alive -= 1
        else:
            self.computer_field.grid[y_index][x_index] = "#"
            print("Промах!")

    def computer_turn(self):
        x_index = random.randint(0, self.size - 1)
        y_index = random.randint(0, self.size - 1)
        cell = self.player_field.grid[y_index][x_index]
        if cell == "S":
            print("Компьютер попал!")
            self.computer_field.grid[y_index][x_index] = "X"
            self.computer_field.ships_alive -= 1
        else:
            self.computer_field.grid[y_index][x_index] = "#"
            print("Компьютер промахнулся!")





BattleshipGame().play()