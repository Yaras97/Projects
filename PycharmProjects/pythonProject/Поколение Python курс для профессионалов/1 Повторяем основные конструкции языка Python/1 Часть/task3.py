def is_valid(string):
    return string.isdigit() and 4 <= len(string) <= 6



# def is_valid(string):
#     f = ' ' not in string
#     f2 = 4 <= len(string) <= 6
#     f3 = string.isdigit()
#
#     return all([f, f2, f3])


# from string import digits
#
# def is_valid(string):
#     if len(string) in [4, 5, 6]:
#         for c in string:
#             if c not in digits:
#                 return False
#         else:
#             return True
#     else:
#         return False