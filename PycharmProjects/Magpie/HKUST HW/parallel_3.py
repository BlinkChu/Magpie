from threading import Thread
import time

balance = 100

def increase():
    global balance

    local_copy = balance
    local_copy += 1
    time.sleep(0.1)

    balance - local_copy