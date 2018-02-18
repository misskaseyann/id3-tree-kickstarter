import numpy as np
import re

from id3.Read import Read


class DecisionTree(object):
    def __init__(self):
        """Constructor"""

    def process_data(self, fp):
        file = open(fp, 'r+', encoding='utf-8')
        data = []
        d = []
        for line in file.readlines():
            d.append(line.strip())
        for d1 in d:
            data.append(d1.split(","))
        file.close()

        features = data[0]
        #  get rid of the oracle feature
        features = features[:-1]
        data = data[1:]
        classes = []
        for d in range(len(data)):
            classes.append(data[d][-1])
            data[d] = data[d][:-1]
        return data, classes, features

    def grow_tree(self, data, classes, features):
        numdata = len(data)
        print(data)
        print("numdata")
        print(numdata)
        numfeatures = len(data[0])

        #  Get all possible classes.
        all_classes = []
        for this_class in classes:
            if all_classes.count(this_class) == 0:
                all_classes.append(this_class)

        freq = np.zeros(len(all_classes))

        total_entropy = 0
        # total_gini = 0
        i = 0

        for this_class in all_classes:
            freq[i] = classes.count(this_class)
            total_entropy += self.entropy(freq[i]/numdata)
            # total_gini += (freq[i]/numdata) ** 2
            i += 1

        total_gini = 1 - total_gini
        node = classes[np.argmax(freq)]
        if numdata == 0 or numfeatures == 0:
            return node
        elif classes.count(classes[0]) == numdata:
            return classes[0]
        else:
            gain = np.zeros(numfeatures)
            # gini_gain = np.zeros(numfeatures)
            set = range(numfeatures)
            for subset in set:
                g = self.gain()
                # TODO

    def entropy(self, p):
        return -p * np.log2(p)