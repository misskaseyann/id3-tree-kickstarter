import numpy as np


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

        self.features = data[0]
        #  get rid of the oracle feature
        self.features = self.features[:-1]
        data = data[1:]
        classes = []
        for d in range(len(data)):
            classes.append(data[d][-1])
            data[d] = data[d][:-1]
        return data, classes, self.features

    def grow_tree(self, data, classes, features, maxlevel=-1, level=0):
        numdata = len(data)
        numfeatures = len(data[0])

        #  Get all possible classes.
        newclasses = []
        print("classes")
        print(classes)
        for this_class in classes:
            if newclasses.count(this_class) == 0:
                newclasses.append(this_class)
        print("new classes")
        print(newclasses)

        freq = np.zeros(len(newclasses))

        total_entropy = 0
        total_gini = 0
        i = 0
        for this_class in newclasses:
            freq[i] = classes.count(this_class)
            total_entropy += self.entropy(freq[i]/numdata)
            total_gini += (freq[i]/numdata) ** 2
            i += 1

        total_gini = 1 - total_gini
        max = classes[np.argmax(freq)]

        if numdata == 0 or numfeatures == 0 or (maxlevel >= 0 and level > maxlevel):
            #  No more attributes to test.
            return max
        elif classes.count(classes[0]) == numdata:
            #  All examples left are the same class.
            return classes[0]
        else:
            #  Find the attribute that maximizes gain.
            gain = np.zeros(numfeatures)
            gini_gain = np.zeros(numfeatures)
            featureset = range(numfeatures)

            for feature in featureset:
                fgain, fgini_gain = self.gain(data, classes, feature)
                gain[feature] = total_entropy - fgain
                gini_gain[feature] = total_gini - fgini_gain

            # node
            maxfeature = np.argmax(gain)
            tree = {features[maxfeature]: {}}
            print("tree")
            print(tree)

            vals = []
            for element in data:
                if element[feature] not in vals:
                    vals.append(element[maxfeature])

            for val in vals:
                #  Find the data with each feature.
                newdata = []
                newclasses = []
                i = 0
                newfeatures = None
                for element in data:
                    if element[maxfeature] == val:
                        if maxfeature == 0:
                            newelement = element[1:]
                            newfeatures = features[1:]
                        elif maxfeature == numfeatures:
                            newelement = element[:-1]
                            newfeatures = features[:-1]
                        else:
                            newelement = element[:maxfeature]
                            newelement.extend(element[maxfeature + 1:])
                            newfeatures = features[:maxfeature]
                            newfeatures.extend(features[maxfeature + 1:])
                        newdata.append(newelement)
                        newclasses.append(classes[i])
                    i += 1
                #  recursively call down the tree.
                subtree = self.grow_tree(newdata, newclasses, newfeatures, maxlevel, level+1)
                #  add subtree to the tree
                tree[features[maxfeature]][val] = subtree
            print("DONE")
            return tree

    def entropy(self, p):
        return -p * np.log2(p)

    def gain(self, data, classes, feature):
        gain = 0
        gini_gain = 0
        numdata = len(data)

        #  All the values the feature can take.
        vals = []
        for element in data:
            if element[feature] not in vals:
                vals.append(element[feature])

        #  Initialize everything for calculation.
        numfeatures = np.zeros(len(vals))
        entropy = np.zeros(len(vals))
        gini = np.zeros(len(vals))
        vi = 0
        #  Find where the values are.
        for val in vals:
            di = 0
            new_classes = []
            for element in data:
                if element[feature] == val:
                    numfeatures[vi] += 1
                    new_classes.append(classes[di])
                di += 1

            classvals = []
            for this_class in new_classes:
                if classvals.count(this_class) == 0:
                    classvals.append(this_class)

            numclasses = np.zeros(len(classvals))
            ci = 0
            for classval in classvals:
                for this_class in new_classes:
                    if this_class == classval:
                        numclasses[ci] += 1
                ci += 1

            for ci in range(len(classvals)):
                entropy[vi] += self.entropy((numclasses[ci])/np.sum(numclasses))
                gini[vi] += (numclasses[ci]/np.sum(numclasses)) ** 2

            gain = gain + numfeatures[vi] / numdata * entropy[vi]
            gini_gain = gini_gain + numfeatures[vi] / numdata * gini[vi]
            vi += 1
        return gain, 1 - gini_gain

    def printTree(self, tree, name):
        if type(tree) == dict:
            print(name, list(tree.keys())[0])
            for item in list(tree.values())[0].keys():
                print(name, item)
                self.printTree(list(tree.values())[0][item], name + "\t")
        else:
            print(name, "\t->\t", tree)