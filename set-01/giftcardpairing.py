n = int(input())
price = list(map(int, input().split()))
T = int(input())

seen = {}

for i in range(n):
    complement = T - price[i]

    if complement in seen:
        print(seen[complement], i)
        break

    seen[price[i]] = i

# explanation

# We need to find two prices whose sum is 235.
# Index	Price	Required price (235 - price)	Result
# 0	120	115	Not found
# 1	45	190	Not found
# 2	80	155	Not found
# 3	200	35	Not found
# 4	35	200	Found at index 3