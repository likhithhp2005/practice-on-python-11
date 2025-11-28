d = {'a': 10, 'b': 25, 'c': 5, 'd': 30}

max_key = max(d, key=d.get)

print("Key with maximum value:", max_key)
print("Value:", d[max_key])