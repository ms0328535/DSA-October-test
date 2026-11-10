
n = int(input())
arr = list(map(int, input().split()))

total = sum(arr)
left_sum = 0

for i in range(n):
    right_sum = total - left_sum - arr[i]

    if left_sum == right_sum:
        print(i)
        break

    left_sum += arr[i]

else:
    print(-1)


# Explanation

# First calculate the total sum:
# \[
# 3+(-2)+5+4+1+5=16
# \]

# Formula:
# \[
# RightSum=Total-LeftSum-CurrentElement
# \]

# Index	Element	Left sum	Right sum	Balanced?
# 0	3	0	13	No
# 1	-2	3	15	No
# 2	5	1	10	No
# 3	4	6	6	Yes

# At index 3:
# - Left side: 3 + (-2) + 5 = 6
# - Right side: 1 + 5 = 6