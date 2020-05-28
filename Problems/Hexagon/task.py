import math


class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        answer = (3 * math.sqrt(3) * self.side_length ** 2) / 2
        return "%.3f" % answer


    # create get_area here