"""
'Best' way yo create Singleton in Python

Metaclass -> class that defines the behavior and rules
for creating other classes.
'Classes of classes.'

All classes in python implicitly inherit from 'type' built-on class,
which is a metaclass.

Allow us to customize class creation process.
"""


class SingletonMeta(type):
    # Dictionary stores single isntance of the class for
    # each subclass of the SingletonMEta metaclass
    _instances = {}

    def __call__(cls, *args, **kwargs):
        print("<call meta> calling...")
        if cls not in cls._instances:
            # Create the instance by calling the __call__
            # method of the parent's (super().__call__())
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# out actual Singleton class
class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass


# how to instantiate
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)
