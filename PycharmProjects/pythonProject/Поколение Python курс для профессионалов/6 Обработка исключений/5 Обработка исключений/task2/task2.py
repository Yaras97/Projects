class LengthError(Exception):
    pass


class LetterError(Exception):
    pass


class DigitError(Exception):
    pass


def is_good_password(string):
    def low(letter):
        return letter.isalpha() and letter == letter.lower()

    def up(letter):
        return letter.isalpha() and letter == letter.upper()

    def dig(letter):
        return letter.isdigit()

    try:
        if not list(filter(low, string)):
            raise LetterError('False')
        if not list(filter(up, string)):
            raise LetterError('False')
        if not list(filter(dig, string)):
            raise DigitError('False')
        if len(string) < 9:
            raise LengthError('False')
        else:
            return True
    except LengthError as err:
        return err
    except LetterError as err:
        return err
    except DigitError as err:
        return err




print(is_good_password('sjkdfsjkdfhjksdfhjkSDFSDAFSADFSADfsdajf'))
