text = input()
count = -2
vh = 0
for i in range(len(text)):
    if text[i] == "f":
        vh = i
        count += 1
    if count > -1:
        break
if count == -2:
    print("-2")
elif count == -1:
    print("-1")
else:
    print(vh)