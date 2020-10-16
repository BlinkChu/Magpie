
import numpy as np
import random
import time
import numba as nb

def game():
    chess = [0 for i in range(9)]
    initial = [i for i in range(9)]
    win = False
    turn = 1
    result = ''
    # print(np.reshape(chess,[3,3]))
    while not win:
        for i in initial:
            chess_tmp = chess.copy()
            chess_tmp[i] = 1
            if win_con(chess_tmp):
                chess[i] = 1
                win = win_con(chess_tmp)
                # print(f'After turn {turn}')
                turn += 1
                # print(np.reshape(chess,[3,3]))
                break
        if win:
            break
        else:
            defeat = False
            for i in initial:
                chess_tmp = chess.copy()
                chess_tmp[i] = 2
                if win_con(chess_tmp):
                    chess[i] = 1
                    # print(f'After turn {turn}')
                    turn += 1
                    # print(np.reshape(chess,[3,3]))
                    initial.remove(i)
                    defeat = True
                    break
            if len(initial) == 0:
                result = 'draw'
                win = True
                # print(result)
                break
            if not defeat:
                tmp = random.choice(initial)
                chess[tmp] = 1
                initial.remove(tmp)
                # print(f'After turn {turn}')
                turn += 1
                # print(np.reshape(chess,[3,3]))
                win = win_con(chess)
            if len(initial) == 0:
                result = 'draw'
                win = True
                # print(result)
                break

        # =========================================  =========================================
        for i in initial:
            chess_tmp = chess.copy()
            chess_tmp[i] = 2
            if win_con(chess_tmp):
                chess[i] = 2
                win = win_con(chess_tmp)
                # print(f'After turn {turn}')
                turn += 1
                # print(np.reshape(chess,[3,3]))
                break
        if win:
            break
        else:
            defeat = False
            for i in initial:
                chess_tmp = chess.copy()
                chess_tmp[i] = 1
                if win_con(chess_tmp):
                    chess[i] = 2
                    # print(f'After turn {turn}')
                    turn += 1
                    # print(np.reshape(chess,[3,3]))
                    initial.remove(i)
                    defeat = True
                    break
            if len(initial) == 0:
                result = 'draw'
                win = True
                # print(result)
                break
            if not defeat:
                tmp = random.choice(initial)
                chess[tmp] = 2
                initial.remove(tmp)
                # print(f'After turn {turn}')
                turn += 1
                # print(np.reshape(chess,[3,3]))
                win = win_con(chess)
            if len(initial) == 0:
                result = 'draw'
                win = True
                # print(result)
                break

    return winner(chess)
        # tmp = random.choice(initial)
        # chess[tmp] = 2
        # initial.remove(tmp)
        # print(f'After turn {turn}')
        # turn += 1
        # print(np.reshape(chess, [3, 3]))
        # win = win_con(chess)
        # if win:
        #     break

def win_con(a):
    # a = array.flatten()
    con = ((a[0] == 1 and a[1] == 1 and a[2] == 1) or(a[3] == 1 and a[4] == 1 and a[5] == 1) or
    (a[6] == 1 and a[7] == 1 and a[8] == 1) or
    (a[0] == 1 and a[3] == 1 and a[6] == 1) or
    (a[1] == 1 and a[4] == 1 and a[7] == 1) or
    (a[2] == 1 and a[5] == 1 and a[8] == 1) or
    (a[0] == 1 and a[4] == 1 and a[8] == 1) or
    (a[2] == 1 and a[4] == 1 and a[6] == 1) or
    (a[0] == 2 and a[1] == 2 and a[2] == 2) or
    (a[3] == 2 and a[4] == 2 and a[5] == 2) or
    (a[6] == 2 and a[7] == 2 and a[8] == 2) or
    (a[0] == 2 and a[3] == 2 and a[6] == 2) or
    (a[1] == 2 and a[4] == 2 and a[7] == 2) or
    (a[2] == 2 and a[5] == 2 and a[8] == 2) or
    (a[0] == 2 and a[4] == 2 and a[8] == 2) or
    (a[2] == 2 and a[4] == 2 and a[6] == 2))
    return con

def winner(a):
    con_1 = ((a[0] == 1 and a[1] == 1 and a[2] == 1) or(a[3] == 1 and a[4] == 1 and a[5] == 1) or
    (a[6] == 1 and a[7] == 1 and a[8] == 1) or
    (a[0] == 1 and a[3] == 1 and a[6] == 1) or
    (a[1] == 1 and a[4] == 1 and a[7] == 1) or
    (a[2] == 1 and a[5] == 1 and a[8] == 1) or
    (a[0] == 1 and a[4] == 1 and a[8] == 1) or
    (a[2] == 1 and a[4] == 1 and a[6] == 1))

    con_2 = ((a[0] == 2 and a[1] == 2 and a[2] == 2) or
    (a[3] == 2 and a[4] == 2 and a[5] == 2) or
    (a[6] == 2 and a[7] == 2 and a[8] == 2) or
    (a[0] == 2 and a[3] == 2 and a[6] == 2) or
    (a[1] == 2 and a[4] == 2 and a[7] == 2) or
    (a[2] == 2 and a[5] == 2 and a[8] == 2) or
    (a[0] == 2 and a[4] == 2 and a[8] == 2) or
    (a[2] == 2 and a[4] == 2 and a[6] == 2))

    if con_1:
        return 1
    elif con_2:
        return 2
    else:
        return 3

if __name__ == '__main__':
    # winners = game()
    # if winners == 1:
    #     print('1 wins')
    # elif winners == 2:
    #     print('2 wins')
    result = []
    count = 50000
    start_time = time.time()
    for i in range(count):
        winners = game()
        result.append(winners)
    end_time = time.time()
    count_1 = result.count(1)
    count_2 = result.count(2)
    draw_result = result.count(3)

    print(f'Probability of 1 wins: {count_1 / count}')
    print(f'Probability of 2 wins: {count_2 / count}')
    print(f'Probability of draw: {draw_result / count}')
    print(f'Games completed: {count}')
    print(f'Simulation time: {end_time - start_time}')