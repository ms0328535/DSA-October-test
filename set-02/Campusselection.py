
n = int(input())
arr = list(map(int, input().split()))

count = 0
candidate = None

for num in arr:
    if count == 0:
        candidate = num

    if num == candidate:
        count += 1
    else:
        count -= 1

print(candidate)

# Explanation

# We maintain two variables:
# - candidate – stores the possible winning candidate.
# - count – stores the voting count.
# Number	Candidate	Count
# 3	3	1
# 2	3	0
# 3	3	1
# 3	3	2
# 1	3	1
# 3	3	2
# 2	3	1
# 3	3	2
# 3	3	3

# Final candidate = 3.