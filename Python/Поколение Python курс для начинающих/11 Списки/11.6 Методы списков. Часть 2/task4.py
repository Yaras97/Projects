n = int(input()[1:])

for i in range(n):
	line = input().split('#')
	line = line[0].rstrip()
	print(line)