class CustomContextManager:
    def __enter__(self):
        print('Вход в контекстный менеджер...')
        return 'Python generation!'
    def __exit__(self, exc_type, exc_value, traceback):
        print('Выход из контекстного менеджера...')
        print(exc_type, exc_value, traceback, sep='\n')


with CustomContextManager() as manager:
    print('hello')
    print(manager)