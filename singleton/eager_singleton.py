"""
Eager instantiation
"""


class SingletonMeta(type):
    # Dictionary stores single isntance of the class for
    # each subclass of the SingletonMEta metaclass
    _instances = {}

    # override: called during creation of sub-types
    def __init__(cls, name, bases, dct):
        super.__init__(name, bases, dct)
        # Eager loading of the class instance
        cls._instances[cls] = super.__call__()
        print('initializing <super>...')

    # return the singleton instance
    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]


# Out practical Singleton clss which is a singleton by the
# fact that it is derived from the SingletonMeta metaclass
class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        # Initialize your attributes here
        self.attributes = "I'm a Singleton"


# how to instantiate
s1 = Singleton()
s2 = Singleton()

print(s1.attributes)
print(s2.attributes)

print(s1 is s2)
