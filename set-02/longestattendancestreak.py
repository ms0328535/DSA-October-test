
n, T = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
longest = 0

for i in range(n):
    if arr[i] >= T:
        count += 1

        if count > longest:
            longest = count
    else:
        count = 0

print(longest)

# explanation

# Threshold T = 30.

# A good day means attendance is greater than or equal to 30.
# Day	Attendance	Good day?	Current streak
# 1	28	No	0
# 2	35	Yes	1
# 3	40	Yes	2
# 4	31	Yes	3
# 5	30	Yes	4
# 6	12	No	0
# 7	33	Yes	1
# 8	36	Yes	2
# 9	29	No	0
# 10	41	Yes	1

# The longest consecutive good-day streak is 4.