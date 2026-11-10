
n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    index = abs(arr[i]) - 1

    if arr[index] > 0:
        arr[index] = -arr[index]

missing = []

for i in range(n):
    if arr[i] > 0:
        missing.append(i + 1)

if len(missing) == 0:
    print("None")
else:
    print(*missing)

# Explanation

# Initially:
# Index:  0  1  2  3  4  5  6  7
# Array:  4  3  2  7  8  2  3  1


# We use each number to mark its corresponding index as negative.

# For example:
# - Number 4 → index 3 → mark as negative.
# - Number 3 → index 2 → mark as negative.
# - Number 2 → index 1 → mark as negative.
# - Number 7 → index 6 → mark as negative.
# - Number 8 → index 7 → mark as negative.
# - Repeated numbers are skipped if their positions are already negative.
# After marking:
# Index:  0   1   2   3   4  5   6   7
# Array: -4  -3  -2  -7   8  2  -3  -1


# Now check for positive values.
# - Index 4 contains positive 8 → missing roll number = 5.
# - Index 5 contains positive 2 → missing roll number = 6.