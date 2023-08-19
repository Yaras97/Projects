n = input()
m = ""
for i in range(len(n)):
    if n[i] == "G":
        m += "C"
    if n[i] == "C":
        m += "G"
    if n[i] == "T":
        m += "A"
    if n[i] == "A":
        m += "U"
print(m)