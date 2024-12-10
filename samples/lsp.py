"""
Liskov-substitution principle
"""

"""
Problem:
Objects of the superclass should be able to be replaces with objects
of a subclass without affecting the correctness of the program.
If Penguin is used where a Bird is expected, we might get unexpected
behavior due to overriden fly method.
"""


class Bird:
    def fly(self):
        print("I can fly")


class Penguin(Bird):
    def fly(self):
        print("I can't fly")


class Bird:
    def fly(self):
        pass


"""
Solution
"""


class FlyingBird(Bird):
    def fly(self):
        print("I can fly")


class NonFlyingBird(Bird):
    def fly(self):
        print("I can't fly")


class Penguin(NonFlyingBird):
    pass
