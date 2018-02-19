from id3.DecisionTree import DecisionTree

if __name__ == "__main__":
    dt = DecisionTree()
    data, classes, features = dt.process_data("/Users/kaseystowell/Documents/workspace/id3tree/data/party")
    t = dt.grow_tree(data, classes, features)
    dt.printTree(t, ' ')