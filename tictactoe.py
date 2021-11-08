"""
Tic Tac Toe Player
"""
import copy
import math

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

    if ((board[0][0] == X and board[0][1] == X and board[0][2] == X) or
        (board[1][0] == X and board[1][1] == X and board[1][2] == X) or
        (board[2][0] == X and board[2][1] == X and board[2][2] == X) or
        (board[0][0] == X and board[1][0] == X and board[2][0] == X) or
        (board[0][1] == X and board[1][1] == X and board[2][1] == X) or
        (board[0][2] == X and board[1][2] == X and board[2][2] == X) or
        (board[0][0] == X and board[1][1] == X and board[2][2] == X) or
            (board[0][2] == X and board[1][1] == X and board[2][0] == X)):
        return X

    if ((board[0][0] == O and board[0][1] == O and board[0][2] == O) or
        (board[1][0] == O and board[1][1] == O and board[1][2] == O) or
        (board[2][0] == O and board[2][1] == O and board[2][2] == O) or
        (board[0][0] == O and board[1][0] == O and board[2][0] == O) or
        (board[0][1] == O and board[1][1] == O and board[2][1] == O) or
        (board[0][2] == O and board[1][2] == O and board[2][2] == O) or
        (board[0][0] == O and board[1][1] == O and board[2][2] == O) or
            (board[0][2] == O and board[1][1] == O and board[2][0] == O)):
        return O
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


def Max_Value(board):
    if terminal(board):
        return utility(board)
    v = NEG_INF
    for action in actions(board):
        v = max(v, Min_Value(result(board, action)))
    return v


def Min_Value(board):
    if terminal(board):
        return utility(board)
    v = INF
    for action in actions(board):
        v = min(v, Max_Value(result(board, action)))
    return v


def minimax(board):

    if terminal(board):
        return None
    currentplayer = player(board)
    actionlist = actions(board)
    action_value, highest_low, lowest_high = 0, NEG_INF, INF
    if currentplayer == X:
        for action in actionlist:
            action_value = Min_Value(result(board, (action[0], action[1])))
            if action_value > highest_low:
                highest_low = action_value
                best_move = action
        return best_move

    if currentplayer == O:
        for action in actionlist:
            current = Max_Value(result(board, (action[0], action[1])))
            if action_value < lowest_high:
                lowest_high = action_value
                best_move = action
        return best_move
