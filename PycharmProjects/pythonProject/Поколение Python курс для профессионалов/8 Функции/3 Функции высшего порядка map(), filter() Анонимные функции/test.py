objects = [0, [False], '0', False, True, [], 'bee']
true_objects = filter(None, objects)
print(*true_objects)