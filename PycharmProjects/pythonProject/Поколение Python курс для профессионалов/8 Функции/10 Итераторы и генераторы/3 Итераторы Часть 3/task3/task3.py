def is_iterator(obj):
    try:
        if obj == iter(obj):
            return True
        else:
            return False
    except:
        return False

print(is_iterator([1, 2, 3, 4, 5]))