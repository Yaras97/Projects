s = input().split()
print(f"Общее количество артиклей: {s.count('a') + s.count('an') + s.count('the') + s.count('A') + s.count('An') + s.count('The')}")