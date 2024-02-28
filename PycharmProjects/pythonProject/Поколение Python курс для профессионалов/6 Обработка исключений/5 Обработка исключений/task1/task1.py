def low(letter):
    return letter.isalpha() and letter == letter.lower()


def up(letter):
    return letter.isalpha() and letter == letter.upper()


def dig(letter):
    return letter.isdigit()


def is_good_password(string):
    try:
        if not list(filter(low, string)):
            raise ValueError('False')
        if not list(filter(up, string)):
            raise ValueError('False')
        if not list(filter(dig, string)):
            raise ValueError('False')
        if len(string) < 9:
            raise ValueError('False')
        else:
            return True

    except ValueError:
        return False


print(is_good_password('qwertyтимур696969'))
