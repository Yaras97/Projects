n = input()
count = ""
for i in range(len(n)):
    if i % 3 != 0:
        count += n[i]
print(count)
