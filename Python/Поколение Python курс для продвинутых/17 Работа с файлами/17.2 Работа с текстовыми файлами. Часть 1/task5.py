file = open("nums.txt", encoding='utf-8')
a = list(map(str.strip, file.readlines()))
a = list(filter(lambda x: x != "" and x != " ", a))
print(sum(list(map(int, a))))
file.close()
