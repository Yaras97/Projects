from contextlib import contextmanager
@contextmanager
def custom_context_manager():
    try:
        print('Вход в контекстный менеджер...')
        yield 'Python generation!'
    except IndexError as error:
        print(f'Тип возбужденного исключения: {type(error)}')
        print(f'Текст исключения: {error}')
    except:
        raise # если исключение не планируется подавлять, оно должно быть возбуждено повторно
    finally:
        print('Выход из контекстного менеджера...')

with custom_context_manager() as manager:
    print(manager)
    # print(manager['fddf'])
    print(manager[100]) # обращаемся по несуществующему индексу
