# Read list from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Create empty dictionary
occ = {}

# Count occurrences
for n in numbers:
    if n in occ:
        occ[n] += 1
    else:
        occ[n] = 1

# Print result
for key, value in occ.items():
    print(key, ":", value)