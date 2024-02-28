data = input()
if isinstance(eval(data), list):
    print(eval(data)[-1])
if isinstance(eval(data), tuple):
    print(eval(data)[0])
if isinstance(eval(data), set):
    print(len(eval(data)))