class MyClass:
    def __del__(self):
        print('Bye')

def func():
    print('Hi')
    obj = MyClass()
    return obj

obj = func()