def mean(*args):
    if len(args) < 1:
        return 0.0
    else:
        lst = [i for i in args if type(i) == int or type(i) == float]
        if len(lst) == 0:
            return 0.0
        return sum(lst)/len(lst)