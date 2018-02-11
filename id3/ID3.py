import math

class ID3(object):
    def __init__(self, data):
        self.data = data
        self.es = None

    def system_entropy(self, oracle):
        true = 0
        false = 0
        size = len(oracle)

        #  Find how many T/F values there are.
        for answer in oracle:
            if answer == 1:
                true += 1
            if answer == 0:
                false += 1

        self.es = -(true/size) * math.log((true/size), 2) - (false/size) * math.log((false/size), 2)