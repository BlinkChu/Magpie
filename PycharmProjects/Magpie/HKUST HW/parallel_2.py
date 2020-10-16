import time
import multiprocessing

t1 = time.time()

def func(t):
    time.sleep(t)
    print(f'slept {t} second..')

if __name__ == '__main__':
    processes = []

    for i in range(10):
        p = multiprocessing.Process(target=func, args=(i/10,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f'finished in {time.time()-t1} second(s)')