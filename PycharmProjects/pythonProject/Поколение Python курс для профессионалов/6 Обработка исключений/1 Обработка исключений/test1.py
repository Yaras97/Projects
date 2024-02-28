string = 'asdfhhdggiuo'
vowels = 'aeiouy'
swapped_string = ''

for char in string:
    if char in vowels:
        char = char.upper()
        swapped_string += char

print(swapped_string)