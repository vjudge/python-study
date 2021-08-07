import threading
import time
from threading import current_thread


def my_sum(arg1, arg2):
    print(current_thread().getName(), 'start')
    print(arg1, arg2)
    time.sleep(2)
    print(current_thread().getName(), 'end')


for i in range(1, 6, 1):
    th1 = threading.Thread(target=my_sum, args=(i, i+5))
    th1.start()












