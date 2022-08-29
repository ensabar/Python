#from multiprocessing import Process, Value, Array, Lock
#import time
#
#def add_100(numbers, lock):
#    
#    for i in range(100):
#        time.sleep(0.01)
#        for i in range(len(numbers)):
#            with lock:
#                numbers[i] += 1
#
#        
#
#if __name__ == "__main__":
#
#    lock = Lock()
#    #shared_number = Value('i', 0)
#    shared_array = Array('d', [0.0, 100.0, 200.0])
#
#    print('array at beginning', shared_array[:])
#    #print('number at beginning', shared_array[:])
#
#
#    p1 = Process(target=add_100, args=(shared_array, lock))
#    p2 = Process(target=add_100, args=(shared_array, lock))
#
#    p1.start()
#    p2.start()
#
#    p1.join()
#    p2.join()
#
#    print('number at end', shared_array[:])
#    #print('number at end', shared_number.value)

########################################################
# Using Queue
#from multiprocessing import Process, Value, Array, Lock, Queue
#import queue
#import time
#
#def square(numbers, queue):
#    for i in numbers:
#        queue.put(i*i)
#        
#def make_negative(numbers, queue):
#      for i in numbers:
#        queue.put(-1*i)
#
#
#
#if __name__ == "__main__":
#    numbers = range(1, 6)
#
#    q = Queue()
#
#    p1 = Process(target=square, args=(numbers, q))
#    p2 = Process(target=make_negative, args=(numbers, q))
#    
#    p1.start()
#    p2.start()
#
#    p1.join()
#    p2.join()
#
#    while not q.empty():
#        print(q.get())

########################################################
# Multiprocessing pool
# map, apply, join, close
from multiprocessing import Pool


def cube(number):
    return number * number * number
    


if __name__ == "__main__":

    numbers = range(1, 10)
    pool = Pool()

    result = pool.map(cube,numbers)
    
    pool.close()
    pool.join()

    print(result)


