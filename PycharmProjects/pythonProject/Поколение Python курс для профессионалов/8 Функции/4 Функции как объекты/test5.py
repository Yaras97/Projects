def ru_greeting(name):
    print('Привет,', name)


def en_greeting(name):
    print('Hello,', name)


greeting = {'ru': ru_greeting,
            'en': en_greeting}
greeting['ru']('Тимур')
