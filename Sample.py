"""
This is a sample demo of multi-threading with a daemon.
"""
__author__ = 'Xander Petty'
__contact__ = 'xander.petty@protonmail.com'
__version__ = '0.1'

from threading import Thread, Lock
from queue import Queue
from time import sleep

thread_lock = Lock() # This is so output doesn't get jumbled up by multiple threads trying to output at once.

def do_something(thread_number, input_number):
    with thread_lock:
        output = f'Thread: {str(thread_number)}: Here is a number: {str(input_number)}'
        print(output)

def daemon_task(thread_number):
    while True:
        next_in_line = q.get() # This grabs the next object from the queue
        do_something(thread_number, next_in_line) # Runs out above function
        sleep(1) # Just to slow down the tasks so we can watch the threads in action.
        q.task_done()

if __name__ == '__main__': # This says run the below code if it's ran from python Sample.py. But, if you import Sample.py it will skip.
    q = Queue()
    # Lets build some threads
    all_threads = []
    for t_num in range(3):
        t = Thread(target=daemon_task, args=[t_num])
        t.daemon = True 
        t.start()
        all_threads.append(all_threads)
    for num in range(20):
        q.put(num)
    q.join()