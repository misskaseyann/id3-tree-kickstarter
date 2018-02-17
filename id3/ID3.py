import math
import numpy as np

class ID3(object):
    def __init__(self):
        #  Entropy of the system.
        self.esystem = None
        self.eattribute = None
        #  The oracle of the data.
        self.oracle = None

    def entropySys(self, s, k):
        """
        :param s: collection of data
        :param k: categories numpy array [all values][the categories]
        :return:
        """
        #  Cardinality of the collection.
        size = s.shape[0]
        poison = 0   #  true
        edible = 0   #  false
        #  Find how many T/F values there are.
        for answer in self.oracle:
            if answer == 'p':
                poison += 1
            if answer == 'e':
                edible += 1

        return -(poison/size) * math.log((poison/size), 2) - (edible/size) * math.log((edible/size), 2)