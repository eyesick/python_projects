from abc import ABC

class computer(ABC):
    def comp_type(self, os):
        print("Computer runs off of ", os)

class pc(computer):
    def comp_cost(self, cost):
        print("The cost of my computer was: ", cost)

windows = pc()

windows.comp_type("mac")

windows.comp_cost("300")
