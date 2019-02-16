from random import randint

# Pygal used to produce scalable vector graphics files
# Analyze the results of rolling dice
# Can see chart types at http://www.pygal.org/

class Die():
    # Single die class

    # Die will be six if no arguments accepted
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    # returns random number 1-6
    def roll(self):
        return randint(1, self.num_sides)
