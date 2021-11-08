"""
Tic Tac Toe Player
"""
import copy
import math
import random

X = "X"
O = "O"
EMPTY = None
INF = float("inf")
NEG_INF = float("-inf")


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                count += 1
    if count % 2 == 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if player(board) == O:
        new_board[action[0]][action[1]] = O
    else:
        new_board[action[0]][action[1]] = X
    return new_board


def winner(board):
    for row in board:
        x_count = row.count(X)
        o_count = row.count(O)
        if x_count == 3:
            return X
        if o_count == 3:
            return O
    for i in range(3):
        column = [row[i] for row in board]
        if column.count(X) == 3:
            return X
        if column.count(O) == 3:
            return O
        if board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]
        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (len(actions(board)) == 0):
        return True
    if (winner(board) != None):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X):
        return 1
    if (winner(board) == O):
        return -1
    return 0


def Max_Value(board, highest_low, lowest_high):
    if terminal(board):
        return utility(board)
    v = NEG_INF
    for action in actions(board):
        v = max(v, Min_Value(result(board, action), highest_low, lowest_high))
        if v > lowest_high:
            break
    return v


def Min_Value(board, highest_low, lowest_high):
    if terminal(board):
        return utility(board)
    v = INF
    for action in actions(board):
        v = min(v, Max_Value(result(board, action), highest_low, lowest_high))
        if v < highest_low:
            break
    return v

# minimax function with alpha-beta prunning


def minimax(board):

    if terminal(board):
        return None
    c_player = player(board)
    actionlist = actions(board)
    highest_low, lowest_high = NEG_INF, INF
    if c_player == X:
        if len(actions(board)) == 9:
            corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
            random.shuffle(corners)
            return corners[0]
        for action in actionlist:
            value = Min_Value(
                result(board, (action[0], action[1])), highest_low, lowest_high)
            if value > highest_low:
                highest_low = value
                best_move = action
        return best_move

    if c_player == O:
        for action in actionlist:
            value = Max_Value(
                result(board, (action[0], action[1])), highest_low, lowest_high)
            if value < lowest_high:
                lowest_high = value
                best_move = action
        return best_move
