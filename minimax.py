import math

PLAYER = 'X'
OPPONENT = 'O'

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

def evaluate(board):
    # Checar linhas para ganhar
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == PLAYER:
                return 10
            elif board[row][0] == OPPONENT:
                return -10

    # Chegar colunas para ganhar
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == PLAYER:
                return 10
            elif board[0][col] == OPPONENT:
                return -10

    # Chegar diagonal para ganhar
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == PLAYER:
            return 10
        elif board[0][0] == OPPONENT:
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == PLAYER:
            return 10
        elif board[0][2] == OPPONENT:
            return -10

    # No ganhou
    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score
    if score == -10:
        return score
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '
        return best
    else:
        best = math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = OPPONENT
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = PLAYER
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

def main():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    while True:
        print_board(board)
        row, col = map(int, input("Entre com o seu movimento(linha coluna): ").split())
        if board[row][col] != ' ':
            print("Movimento inválido! Tente novamente.")
            continue
        board[row][col] = OPPONENT

        if evaluate(board) == -10:
            print_board(board)
            print("Você ganhou!")
            break

        if not is_moves_left(board):
            print_board(board)
            print("Velha!")
            break

        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = PLAYER

        if evaluate(board) == 10:
            print_board(board)
            print("Você perdeu!")
            break

        if not is_moves_left(board):
            print_board(board)
            print("Velha!")
            break

if __name__ == "__main__":
    main()