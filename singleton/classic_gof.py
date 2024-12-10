"""
Classic generic way of creating a Singleton
in Python.
"""


class ClassicSingleton:
    # class-level variable to store single class instance
    _instance = None

    def __init__(self):
        print("<init> called...")
        raise RuntimeError("Call get_instance() instead.")

    @classmethod
    def get_instance(cls):
        print("<get_instance> called...")
        # NOTE: lazy instantiation
        if not cls._instance:
            # create new instance of the class
            cls._instance = cls.__new__(cls)
        # return the single intance of the class, either
        # newly created one or existing one
        return cls._instance


# will raise error
# s0 = ClassicSingleton()

# instantiation sample:
s1 = ClassicSingleton.get_instance()
s2 = ClassicSingleton.get_instance()
print(s1 is s2)
print(s1)
print(s2)
