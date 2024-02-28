import pickle

with open('data.pk1', 'wb') as pickle_file:
    data = ['a', 'b', 3, 4, 'f', 'g', 7, 8]
    pickle.dump(data, pickle_file)


def pickle_summ(filename, sum_count):
    with open(filename, 'rb') as file:
        pk_file = pickle.load(file)
        sum_dict = 0
        list_cnt = []
        for num in pk_file:
            if type(pk_file) is list:
                if type(num) is int:
                    list_cnt.append(num)

            elif type(pk_file) is list:
                if type(num) is int:
                    sum_dict += num
        sum_list = min(list_cnt) * max(list_cnt)
        if sum_count == sum_dict or sum_count == sum_list:

            print('Контрольные суммы совпадают')
        else:
            print('Контрольные суммы не совпадают')


pickle_summ('data.pk1', 3023)
