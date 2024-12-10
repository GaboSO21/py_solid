"""
Interface Separation Principle (ISP)
"""

# Wrong implementation
# Interface Has multiple functionalities
# Each class should implement all methods even though they are not relevant
# to their functionality.
# Violates ISP, states that clients should not be forced to depend
# on interfaces they do not use

# Large interfaces with unrelated methods makes code harder to maintain,
# understand and extend


class IMultiFunctionDevice:
    def print(self):
        pass

    def scan(self):
        pass

    def copy(self):
        pass

    def fax(self):
        pass


class Printer(IMultiFunctionDevice):
    def print(self):
        print("Printing...")


class Scanner(IMultiFunctionDevice):
    def scan(self):
        print("Scanning...")


class Copier(IMultiFunctionDevice):
    def copy(self):
        print("Copying...")


"""
Solution
"""


class IPrinter:
    def print(self):
        pass


class IScanner:
    def scan(self):
        pass


class ICopier:
    def copy(self):
        pass


class IFax:
    def fax(self):
        pass


class Printer(IPrinter):
    def print(self):
        print("Printing....")

# Etc..
