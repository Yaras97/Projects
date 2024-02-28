class PhoneNumber:
    def __init__(self, phone_number):
        if ' ' in phone_number:
            self.phone_number = ''.join(phone_number.split())
        else:
            self.phone_number = phone_number

    def __str__(self):
        return f'({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}'

    def __repr__(self):
        return f"PhoneNumber('{self.phone_number}')"


phone = PhoneNumber('918 396 3389')

print(str(phone))
print(repr(phone))


# import re
#
# class PhoneNumber:
#     pattern = r'(\d{3})\s?(\d{3})\s?(\d{4})'
#
#     def __init__(self, phone_number):
#         self.phone_number = phone_number
#
#     def __str__(self):
#         result = re.sub(PhoneNumber.pattern, r'(\1) \2-\3', self.phone_number)
#         return result
#
#     def __repr__(self):
#         return f"PhoneNumber('{self.phone_number.replace(' ','')}')"