def hash_function(obj):
    return hash(obj) % 100
data = [2077, 3.14, 'bee', 'geek', (1, 2, 3), -3, -3.0]
for obj in data:
    print(hash_function(obj))