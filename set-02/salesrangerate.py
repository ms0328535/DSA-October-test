
n, q = map(int, input().split())

sales = list(map(int, input().split()))

# Create prefix sum array
prefix = [0] * n

prefix[0] = sales[0]

for i in range(1, n):
    prefix[i] = prefix[i - 1] + sales[i]

# Process queries
for _ in range(q):
    l, r = map(int, input().split())

    if l == 0:
        result = prefix[r]
    else:
        result = prefix[r] - prefix[l - 1]

    print(result)

# explanation

# Step 1: Calculate the prefix sum array.

# Original sales:
# Index:   0  1  2  3  4  5  6  7
# Sales:   5  3  8  2  7  1  9  4


# Prefix sum:
# Index:   0  1  2  3  4  5  6  7
# Prefix:  5  8 16 18 25 26 35 39


# Step 2: Answer each query.

# Formula:
# - If l == 0: Answer = prefix[r]
# - Otherwise: Answer = prefix[r] - prefix[l-1]
# Query	Calculation	Answer
# 0 2	16	16
# 3 5	26 − 16	10
# 1 7	39 − 5	34
# 4 4	25 − 18	7

# How does the formula work?