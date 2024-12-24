import threading


class SingletonMeta(type):

    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super(
                    SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SequenceGenerator(metaclass=SingletonMeta):

    def __init__(self):
        self._number = 0

    def getNextNumber(self):
        self._number += 1
        return self._number


seq_one = SequenceGenerator()
seq_two = SequenceGenerator()
print(seq_one.getNextNumber())
print(seq_two.getNextNumber())
print(seq_one == seq_two)
