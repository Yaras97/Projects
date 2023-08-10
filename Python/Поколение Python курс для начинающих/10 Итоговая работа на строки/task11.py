s = input()
a = int(s.find('h'))
b = int(s.rfind('h'))
print(s[:a]+s[b:a:-1]+s[b:])
