def greet(a, *args):
    args = (a,) + args
    j = [i + ' ' + 'and' for i in args]
    j = ' '.join(j).rstrip('and').rstrip()
    h = 'Hello, ' + j + '!'
    return h