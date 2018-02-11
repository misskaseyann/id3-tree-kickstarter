import math
import numpy as np

class ID3(object):
    def __init__(self, data):
        self.data = data
        self.es = None

    def entropy(self, s, k):
        """

        :param s: collection of data
        :param k: categories numpy array [all values][the categories]
        :return:
        """
        #  Cardinality of the collection.
        sc = s.shape[0]
        
        #  Find how many T/F values there are.
        for answer in oracle:
            if answer == 1:
                true += 1
            if answer == 0:
                false += 1

        self.es = -(true/size) * math.log((true/size), 2) - (false/size) * math.log((false/size), 2)