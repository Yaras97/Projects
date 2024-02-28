def is_good_password(string):
    class LengthError(Exception):
        pass

    class LetterError(Exception):
        pass

    class DigitError(Exception):
        pass

    def low(letter):
        return letter.isalpha() and letter == letter.lower()

    def up(letter):
        return letter.isalpha() and letter == letter.upper()

    def dig(letter):
        return letter.isdigit()
    try:
        if not list(filter(low, string)):
            raise LetterError('LetterError')
        if not list(filter(up, string)):
            raise LetterError('LetterError')
        if not list(filter(dig, string)):
            raise DigitError('DigitError')
        if len(string) < 9:
            raise LengthError('LengthError')
        else:
            print('Success!')
            return 'Success!'

    except LengthError as err:
        print(err)
        return err

    except LetterError as err:
        print(err)
        return err

    except DigitError as err:
        print(err)
        return err


while is_good_password(input()) != 'Success!':
    pass
