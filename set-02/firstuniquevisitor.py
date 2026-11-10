
n = int(input())
arr = list(map(int, input().split()))

count = {}

for num in arr:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

found = False

for num in arr:
    if count[num] == 1:
        print(num)
        found = True
        break

if not found:
    print(-1)

# explanation

# Step 1: Count the frequency of each visitor ID.
# Visitor ID	Frequency
# 17	3
# 23	2
# 8	2
# 42	2
# 5	1

# Step 2: Check the original array from left to right.
# - 17 → repeated
# - 23 → repeated
# - 17 → repeated
# - 8 → repeated
# - 23 → repeated
# - 42 → repeated
# - 8 → repeated
# - 5 → appears only once!
# Therefore, the first unique visitor is 5.