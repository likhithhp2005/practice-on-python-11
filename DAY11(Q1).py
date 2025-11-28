keys = input("Enter keys separated by space: ").split()
values = input("Enter values separated by space: ").split()

d = {}

for i in range(len(keys)):
    d[keys[i]] = values[i]

print("Dictionary:", d)