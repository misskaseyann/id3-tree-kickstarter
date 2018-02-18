import os
import re


class Read(object):
    """
    Helper class that reads in data.
    """
    def __init__(self, fp):
        """
        Initialize the Read class.

        :param fp: filepath to be read.
        """
        self.fp = fp

    def readin(self):
        """
        Reads a text file in and splits it by each new line.

        :return: array of split text data.
        """
        if os.path.isfile(self.fp):
            file = open(self.fp, 'r+', encoding='utf-8')
            data = []
            d = []
            for line in file.readlines():
                d.append(line.strip())
            for d1 in d:
                data.append(d1.split(","))
            file.close()

            # raw = file.read()
            # data = re.split('\n', raw)
            # return data
        else:
            print("Improper file path.")

    def setpath(self, fp):
        """
        :param fp: filepath to set current filepath to.
        """
        self.fp = fp
