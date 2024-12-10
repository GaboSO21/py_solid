"""
Handling thread safety using a Lock for Singletons
"""
from threading import Lock


class Counter:
    """
    Thread safe counter
    """

    def __init__(self):
        self.count = 0
        self.lock = Lock

    def increment(self):
        self.lock.acquire()
        self.count += 1
        self.lock.release()

# Thread safe singleton sample


class ThreadSafeSingleton:
    # class-level variable. Store single class instance
    _instance = None
    # class-level lock to ensure thread safety
    _lock = Lock()
    # __new__ method override. Thread-safe implementation

    def __new__(cls):
        # acquire the lock to ensure thread safety
        with cls._lock:
            if not cls._instance:
                # create the single instance of the class
                cls._instance = super().__new__(cls)
            # return the single instance of the class
        return cls._instance


# Instantiate
s1 = ThreadSafeSingleton()
