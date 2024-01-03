# class Foo:
#     def __init__(self):
#         self.second = threading.Semaphore(0)
#         self.third = threading.Semaphore(0)

        


#     def first(self, printFirst: 'Callable[[], None]') -> None:
        
#         printFirst()
#         self.second.release()


#     def second(self, printSecond: 'Callable[[], None]') -> None:
        
#         self.second.acquire()
#         printSecond()
#         self.third.release()
import threading

class Foo:
    def __init__(self):
        self.first_lock = threading.Lock()
        self.second_lock = threading.Lock()
        self.first_lock.acquire()
        self.second_lock.acquire()  # Start with the second lock locked

    def first(self, printFirst):
        # Print 'first'
        printFirst()
        # Release the first lock to allow the execution of 'second'
        self.first_lock.release()

    def second(self, printSecond):
        # Wait for the first lock to be released
        self.first_lock.acquire()
        # Print 'second'
        printSecond()
        # Release the second lock to allow the execution of 'third'
        self.second_lock.release()

    def third(self, printThird):
        # Wait for the second lock to be released
        self.second_lock.acquire()
        # Print 'third'
        printThird()

#     def third(self, printThird: 'Callable[[], None]') -> None:
        
#         self.third.acquire()
#         printThird()