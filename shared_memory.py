from multiprocessing import Process, Value, Lock

# function to increase the counter
def add_to_counter(counter, lock, id):
    for _ in range(2):  # only 2 times for clarity (optional: range(100000))
        with lock: # acquire the lock
            print(f"Process-{id} acquired lock") # lock acquired
            temp = counter.value # read current value
            counter.value = temp + 1 # increment value
            # counter.value += 1
            print(f"Process-{id} set counter to {counter.value}") # new value set

if __name__ == '__main__':
    # define shared memory variable
    counter = Value('i', 0) # integer shared memory
    lock = Lock() # create a lock

    # create two processes
    p1 = Process(target=add_to_counter, args=(counter, lock, 1))
    p2 = Process(target=add_to_counter, args=(counter, lock, 2))

    # start the processes
    p1.start()
    p2.start()

    # wait for both to finish
    p1.join()
    p2.join()

    # print final counter value
    print("Final counter:", counter.value)