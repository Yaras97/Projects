def is_fraction(string):
    try:
        if '/' in string:
            num1, num2 = string.split('/')
            float(num1)/float(num2)
            return True
        else:
            return False
    except Exception:
        return False

print(is_fraction('1000/00004123'))
print(is_fraction('1000/0000'))
print(is_fraction('1000/00000008000'))