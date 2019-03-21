import time
from threading import Thread
import logging
import numpy as np

logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def my_func(name):

    while True:
        sec = np.random.randint(1, 4)

        logging.info("Sleeping {sec} sec from thread {name}.".format(sec=sec, name=name))
        time.sleep(sec)
        logging.info("Finished sleeping from thread {name}.".format(name=name))


t1 = Thread(target=my_func, args=("t1",))
t2 = Thread(target=my_func, args=("t2",))
t3 = Thread(target=my_func, args=("t3",))
t4 = Thread(target=my_func, args=("t4",))
t5 = Thread(target=my_func, args=("t5",))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
