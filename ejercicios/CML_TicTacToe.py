# Python exercises for AI Programming Course: Tic Tac Toe
# Exercises solved by Carmen Montalvo Luque, 11/2025

# =====================================================
# Ejercicio 1
#
# Implementa el juego Tic Tac Toe usando Programación Orientada a Objetos
# y después usa la versión implementada para crear una nueva clase Jugador
# de manera que quien juegue sea el ordenador usando el algoritmo MINIMAX.
# =====================================================

import random
import math

# ---------- TicTacToe implementation ----------

class TicTacToe:
    def __init__(self):
        self.board = [None] * 9
        self.current_winner = None

    def make_move(self, pos, player):
        if self.board[pos] is None:
            self.board[pos] = player
            if self.winner(pos, player):
                self.current_winner = player
            return True
        return False

    def available_moves(self):
        return [i for i, v in enumerate(self.board) if v is None]

    def empty_squares(self):
        return any(v is None for v in self.board)

    def winner(self, pos, player):
        row_ind = pos // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all(spot == player for spot in row):
            return True

        col_ind = pos % 3
        col = [self.board[col_ind + i*3] for i in range(3)]
        if all(spot == player for spot in col):
            return True

        if pos % 2 == 0:
            diag1 = [self.board[i] for i in [0, 4, 8]]
            if all(spot == player for spot in diag1):
                return True
            diag2 = [self.board[i] for i in [2, 4, 6]]
            if all(spot == player for spot in diag2):
                return True

        return False

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join([s if s is not None else ' ' for s in row]) + ' |')

    def print_board_nums(self):
        nums = [str(i) for i in range(9)]
        for row in [nums[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')


# ---------- Players ----------

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def get_move(self, game):
        valid = False
        val = None
        while not valid:
            try:
                square = int(input(f"{self.letter}'s turn. Input move (0-8): "))
                if square not in game.available_moves():
                    raise ValueError
                valid = True
                val = square
            except ValueError:
                print("Invalid square. Try again.")
        return val


class MinimaxComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        self.opponent = 'O' if letter == 'X' else 'X'

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            return random.choice([0, 2, 4, 6, 8])

        _, move = self.minimax(game, self.letter)
        return move

    def minimax(self, state, player):
        max_player = self.letter
        other_player = self.opponent if player == self.letter else self.letter

        if state.current_winner == other_player:
            return (1 if other_player == max_player else -1, None)
        elif not state.empty_squares():
            return (0, None)

        best = (-math.inf, None) if player == max_player else (math.inf, None)

        for move in state.available_moves():
            state.make_move(move, player)
            score, _ = self.minimax(state, other_player)
            state.board[move] = None
            state.current_winner = None

            if player == max_player:
                if score > best[0]:
                    best = (score, move)
            else:
                if score < best[0]:
                    best = (score, move)

        return best


# ---------- Game loop ----------

def play_tic_tac_toe():
    print("\nTic Tac Toe — X is human, O is AI (Minimax).")
    game = TicTacToe()
    human = HumanPlayer('X')
    computer = MinimaxComputer('O')

    game.print_board_nums()
    letter = 'X'

    while game.empty_squares():
        if letter == 'X':
            move = human.get_move(game)
        else:
            print("Computer thinking...")
            move = computer.get_move(game)

        if game.make_move(move, letter):
            print(f"{letter} moved to {move}")
            game.print_board()

            if game.current_winner:
                print(f"{letter} wins!")
                return

            letter = 'O' if letter == 'X' else 'X'
        else:
            print("Invalid move.")

    print("It's a tie!")


if __name__ == "__main__":
    play_tic_tac_toe()
