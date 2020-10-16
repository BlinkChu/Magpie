# Your Code Below
import numpy as np
import time


def check_win(A, i, j):
    """return true if someone win after taking A[i][j]
    """
    # check horizontal
    if (A[:, j] == A[i, j]).all():
        return True
    # check vertical
    if (A[i, :] == A[i, j]).all():
        return True
    # check diagonal
    if i == j and (A.diagonal() == A[i, j]).all():
        return True
    # check reverse diagonal
    if i + j == 2 and (np.fliplr(A).diagonal() == A[i, j]).all():
        return True
    return False


def take_place(A, player):
    """take a place for player

    return the winner after taking the place
    None if no one wins
    """
    opposite = 1 if player == 2 else 2
    win_position = None
    opp_win_position = None

    # search for possible places
    zero_id = np.argwhere(A == 0)
    for i, j in zero_id:
        # search for a place to take that will win the game
        A[i, j] = player
        if check_win(A, i, j):
            win_position = (i, j)
            break

        # search for a place the other side can take that will win the game.
        A[i, j] = opposite
        if check_win(A, i, j):
            opp_win_position = (i, j)
        A[i, j] = 0

    if win_position:
        A[win_position] = player
        return player
    elif opp_win_position:
        A[opp_win_position] = player
    else:
        # take place randomly
        i, j = zero_id[np.random.randint(zero_id.shape[0])]
        A[i, j] = player

    return None


def tic_tac_toe_AI():
    """smart version of tic-tac-toe game

    return the winner, None if draw
    """
    A = np.zeros((3, 3), dtype=int)

    for i in range(9):
        player = [1, 2][i % 2]

        winner = take_place(A, player)
        if winner:
            return winner

    return None


def simulate():
    """simulate tic_tac_toe_AI for 1 seconds
    """
    win_stat = [0, 0, 0]  # [num_draw, num_1_win, num_2_win]
    n_sim = 0  # total number of simulations

    start_time = time.time()
    while (time.time() - start_time < 1):
        winner = tic_tac_toe_AI()
        if (winner):
            win_stat[winner] += 1
        else:
            win_stat[0] += 1
        n_sim += 1
    end_time = time.time()

    print(f"Probability of 1 wins: {win_stat[1] / n_sim:.2f}")
    print(f"Probability of 2 wins: {win_stat[2] / n_sim:.2f}")
    print(f"Probability of draw: {win_stat[0] / n_sim:.2f}")
    print(f"Games completed: {n_sim}")
    print(f"Simulation time: {end_time - start_time:.2f}")


simulate()