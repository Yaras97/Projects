import pickle
import sys

with open('func.pk1', 'wb') as pickle_file:
    def func(*args):
        return ' '.join(args)
    pickle.dump(func, pickle_file)

with open('func.pk1', 'rb') as file:
    open_f = pickle.load(file)
    inp_words = [i for i in sys.stdin]
    print(open_f(*inp_words))
