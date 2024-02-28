def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return string[0] == string[-1] and is_palindrome(string[1:-1])


print(is_palindrome('radar'))
print(is_palindrome('level'))
print(is_palindrome('python'))