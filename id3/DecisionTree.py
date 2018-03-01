import numpy as np


class DecisionTree(object):
    """
    Create a decision tree based on the ID3 algorithm.
    """
    def __init__(self):
        """
        Constructor
        """

    def process_data(self, fp):
        """
        Take in the data and evaluate where it goes.

        :param fp: file path to the data.
        :return: data, classes of the data, the features of the data.
        """
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

    def grow_tree(self, data, classes, features, max_depth=1, depth=0):
        """
        Grow the deicison tree with further subtrees and leafs until
        you hit the max depth of recursion.

        :param data: actual data to be calculated.
        :param classes: classes of the data.
        :param features: features of the data.
        :param max_depth: the maximum recursion depth in case tree takes too long to form.
        :param level: the current level of recursion the tree is at.
        :return: decision tree with nodes and/or leafs.
        """
        numdata = len(data)
        numfeatures = len(data[0])
        #  Get the classes from the data.
        newclasses = []
        print("classes")
        print(classes)
        for this_class in classes:
            if newclasses.count(this_class) == 0:
                newclasses.append(this_class)
        print("new classes")
        print(newclasses)
        #  Compute the total entropy of the system.
        freq = np.zeros(len(newclasses))
        total_entropy = 0
        total_gini = 0
        i = 0
        threshold = False
        for this_class in newclasses:
            freq[i] = classes.count(this_class)
            total_entropy += self.entropy(freq[i]/numdata)
            total_gini += (freq[i]/numdata) ** 2
            freqval = freq[i]/numdata
            if freqval > 0.75:
                threshold = True
            i += 1
        total_gini = 1 - total_gini
        max = classes[np.argmax(freq)]
        #  Check if we are at a max depth of our tree, if we should cut it off, or if we continue recursively building subtrees.
        if numdata == 0 or numfeatures == 0 or (max_depth >= 0 and depth > max_depth) or len(freq) == 1 or (depth > 0 and threshold == True):
            return max
        elif classes.count(classes[0]) == numdata:
            return classes[0]
        else:
            #  What attribute has the largest gain?
            gain = np.zeros(numfeatures)
            gini_gain = np.zeros(numfeatures)
            featureset = range(numfeatures)
            for feature in featureset:
                fgain, fgini_gain = self.gain(data, classes, feature)
                gain[feature] = total_entropy - fgain
                gini_gain[feature] = total_gini - fgini_gain
            #  Nodes of our tree.
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
                #  Recursively call down the tree.
                subtree = self.grow_tree(newdata, newclasses, newfeatures, max_depth, depth+1)
                #  Add subtree to the tree we are growing!
                tree[features[maxfeature]][val] = subtree
            print("DONE")
            #  Return our tree or subtree.
            return tree

    def entropy(self, p):
        """
        Calculate the entropy.

        :param p: cardinality of category.
        :return: entropy value.
        """
        return -p * np.log2(p)

    def gain(self, data, classes, feature):
        """
        Calculate the gain.

        :param data: data being caluclated.
        :param classes: classes of the data.
        :param feature: features of the data.
        :return: gain of the data and the gini gain.
        """
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

    def classifier(self, tree, data):
        """
        Run through the completed tree with given data.

        :param tree: decision tree (dict).
        :param data: data to run through the tree.
        :return: recursive call or the tree.
        """
        if type(tree) == type("string"):
            return tree
        else:
            a = list(tree.keys())[0]
            for i in range(len(self.features)):
                if self.features[i] == a:
                    break
            try:
                t = tree[a][data[i]]
                return self.classifier(t, data)
            except:
                return None

    def run_classifier(self, tree, data):
        """
        Run the classifier and print the results.

        :param tree: the decision tree (dict).
        :param data: data to be ran through the tree.
        :return: results of what the tree classified for each peice of data.
        """
        results = []
        for i in range(len(data)):
            results.append(self.classifier(tree, data[i]))
        return results

    def print_tree(self, tree, name):
        """
        Print the tree out for a visual representation.

        :param tree: A dictionary containing the tree.
        :param name: Name of the node.
        """
        if type(tree) == dict:
            print(name, list(tree.keys())[0])
            for item in list(tree.values())[0].keys():
                print(name, item)
                self.print_tree(list(tree.values())[0][item], name + "\t")
        else:
            print(name, "\t->\t", tree)