import threading
import time
import random

# define a semaphore with capacity of 3
semaphore = threading.Semaphore(3)

# function executed by each thread
def access_resource(id):
    print(f"Thread-{id} is waiting to access resource...") # waiting to acquire
    with semaphore: # acquire semaphore
        print(f"Thread-{id} entered") # entering critical section
        time.sleep(random.uniform(1, 3))  # simulate time of using resource
        # time.sleep(1)
        print(f"Thread {id} is leaving") # exiting critical section

# create and start threads
threads = []
for i in range(6):
    t = threading.Thread(target=access_resource, args=(i,))
    t.start()
    threads.append(t)

# wait for all threads to finish
for t in threads:
    t.join()