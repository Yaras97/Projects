import pickle


def filter_dump(filename, objects, typename):
    with open(filename, 'wb') as file:
        new_list = []
        for item in objects:
            if type(item) is typename:
                new_list.append(item)
        pickle.dump(new_list, file)


filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)