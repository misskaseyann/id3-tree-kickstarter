from id3.DecisionTree import DecisionTree

if __name__ == "__main__":
    dt = DecisionTree()
    data, classes, features = dt.process_data("/Users/kaseystowell/Documents/workspace/id3tree/data/salarytraindata.csv")
    t = dt.grow_tree(data, classes, features)
    dt.print_tree(t, ' ')
    data, classes, features = dt.process_data("/Users/kaseystowell/Documents/workspace/id3tree/data/salarytestdata.csv")
    arr = dt.run_classifier(t, data)
    print("True classes...")
    print(classes)
    print("The data...")
    print(arr)
    true = 0
    false = 0
    for i in range(len(arr)):
        if classes[i] == arr[i]:
            true += 1
        else:
            false +=1
    print(true)
    print(false)