# Read list from user
lst = list(map(int, input("Enter numbers separated by space: ").split()))

freq = {}

for n in lst:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1

print("Frequency of elements:")
for k, v in freq.items():
    print(k, ":", v)