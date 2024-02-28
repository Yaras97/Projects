def greeting(language):
    def greeting_ru():
        print('Привет!')

    def greeting_fr():
        print('Bonjour!')

    if language == 'ru':
        return greeting_ru
    if language == 'fr':
        return greeting_fr


func = greeting('fr')
func()
