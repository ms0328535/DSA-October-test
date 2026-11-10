
n = int(input())
arr = list(map(int, input().split()))

largest = None
second = None

for num in arr:
    if largest is None or num > largest:
        second = largest
        largest = num

    elif num != largest and (second is None or num > second):
        second = num

if second is None:
    print("None")
else:
    print(second)


# Explanation

# We maintain two variables:
# - largest – stores the highest number.
# - second – stores the second-highest distinct number.
# Number	Largest	Second
# 31	31	None
# 28	31	28
# 35	35	31
# 35	35	31
# 29	35	31
# -4	35	31
# 35	35	31
# 28	35	31
# 30	35	31

# Final result:
# - Largest = 35
# - Second largest = 31