import threading

# shared variable
counter = 0

# creating a mutual exclusion lock
lock = threading.Lock()

# function to increase the counter
def increase():
    global counter
    for _ in range(3):  # only 3 times for simplicity (optional: range(100000))
        # acquire the lock
        with lock:
            print(f"{threading.current_thread().name} acquired lock") # lock acquired
            temp = counter # read current value
            counter = temp + 1 # increment value
            print(f"{threading.current_thread().name} updated counter to {counter}") # new value set

# create two threads
t1 = threading.Thread(target=increase)
t2 = threading.Thread(target=increase)

# start the threads
t1.start()
t2.start()

# wait for both threads to finish
t1.join()
t2.join()

# print final counter value
print("Counter value:", counter)