import math
import re

from id3.Read import Read


class DecisionTree(object):
    def __init__(self):
        self.oracle = None
        self.attributes = None

    def process_data(self, fp):
        """
        Takes the filepath of the data text file and seperates
        the oracle and attributes from the data.

        :param fp: file path to the text file.
        """
        r = Read(fp)
        c = r.readin()
        self.oracle = self.split(c[0])
        self.attributes = [None] * (len(c)-1)
        for i in range(1, len(c)):
            self.attributes[i-1] = self.split(c[i])

    def split(self, c):
        """
        Splits the data into seperate pieces into an array.

        :param c: formatted string array of data.
        :return: array containing each of the following:
        0. Title of the category.
        1. Number of subsets in category.
        2. Array of subsets.
        3. Array of subset data.
        """
        arr = [None] * 4
        collection = re.split(':', c)
        arr[0] = collection[0]
        arr[1] = int(collection[1])
        arr[2] = list(collection[2])
        arr[3] = re.split(',', collection[3])
        return arr