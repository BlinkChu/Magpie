import multiprocessing
import os

def func():
    print(f'Hello World from {os.getpid()}')

p1 = multiprocessing.Process(target=func)
p2 = multiprocessing.Process(target=func)


if __name__ == '__main__':
    p1.start()
    p2.start()