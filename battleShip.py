class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0

    def place_ship(self, board, start_row, start_col, direction):
        if direction == 'H':
            if start_col + self.size > len(board[0]):
                return False
            for i in range(self.size):
                if board[start_row][start_col + i] != ' ':
                    return False
            for i in range(self.size):
                board[start_row][start_col + i] = self.name[0]
                self.positions.append((start_row, start_col + i))
        elif direction == 'V':
            if start_row + self.size > len(board):
                return False
            for i in range(self.size):
                if board[start_row + i][start_col] != ' ':
                    return False
            for i in range(self.size):
                board[start_row + i][start_col] = self.name[0]
                self.positions.append((start_row + i, start_col))
        else:
            return False
        return True

    def hit(self):
        self.hits += 1
        return self.hits == self.size

class Destroyer(Ship):
    def __init__(self):
        super().__init__('Destructor', 2)

class Submarine(Ship):
    def __init__(self):
        super().__init__('Submarino', 3)

class Battleship(Ship):
    def __init__(self):
        super().__init__('Acorazado', 4)

class Player:
    def __init__(self, name):
        self.name = name
        self.board = [[' ' for _ in range(10)] for _ in range(10)]
        self.ships = []
        self.hits = [[' ' for _ in range(10)] for _ in range(10)]

    def place_ships(self):
        for ship_class in [Destroyer, Submarine, Battleship]:
            ship = ship_class()
            while True:
                print(f"{self.name}, coloca tu {ship.name} (tamaño {ship.size})")
                start_row = int(input("Fila inicial (0-9): "))
                start_col = int(input("Columna inicial (0-9): "))
                direction = input("Dirección (H para horizontal, V para vertical): ").upper()
                if ship.place_ship(self.board, start_row, start_col, direction):
                    self.ships.append(ship)
                    break
                else:
                    print("No se puede colocar el barco aquí. Inténtalo de nuevo.")

    def print_board(self, board):
        for row in board:
            print(' '.join(row))

    def attack(self, opponent):
        while True:
            print(f"{self.name}, es tu turno de atacar.")
            row = int(input("Fila (0-9): "))
            col = int(input("Columna (0-9): "))
            if 0 <= row < 10 and 0 <= col < 10:
                if opponent.board[row][col] != ' ':
                    print("¡Impacto!")
                    self.hits[row][col] = 'X'
                    for ship in opponent.ships:
                        if (row, col) in ship.positions:
                            if ship.hit():
                                print(f"¡Has hundido el {ship.name}!")
                            break
                else:
                    print("Agua.")
                    self.hits[row][col] = 'O'
                opponent.board[row][col] = self.hits[row][col]
                break
            else:
                print("Posición no válida. Inténtalo de nuevo.")

    def all_ships_sunk(self):
        return all(ship.hits == ship.size for ship in self.ships)

class BattleshipGame:
    def __init__(self):
        self.player1 = Player(input("Nombre del Jugador 1: "))
        self.player2 = Player(input("Nombre del Jugador 2: "))

    def play(self):
        print(f"{self.player1.name}, coloca tus barcos.")
        self.player1.place_ships()
        print(f"{self.player2.name}, coloca tus barcos.")
        self.player2.place_ships()

        current_player = self.player1
        opponent = self.player2

        while True:
            current_player.print_board(current_player.hits)
            current_player.attack(opponent)
            if opponent.all_ships_sunk():
                print(f"¡{current_player.name} ha ganado!")
                break
            current_player, opponent = opponent, current_player

if __name__ == "__main__":
    game = BattleshipGame()
    game.play()