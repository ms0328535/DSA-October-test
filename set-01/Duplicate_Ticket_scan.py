
n = int(input())
arr = list(map(int, input().split()))

seen = set()

for i in range(n):
    if arr[i] in seen:
        print(arr[i])
        break
    else:
        seen.add(arr[i])
else:
    print(-1)


# Explanation
# Index	Ticket ID	Status
# 0	4021	First occurrence
# 1	3377	First occurrence
# 2	5120	First occurrence
# 3	3377	Repeated!

# At index 3, ticket ID 3377 has already appeared at index 1.

# Therefore, we stop scanning.