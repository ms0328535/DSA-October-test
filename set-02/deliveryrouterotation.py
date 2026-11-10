
n, k = map(int, input().split())

arr = list(map(int, input().split()))

k = k % n

def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

reverse(arr, 0, n - 1)

reverse(arr, 0, k - 1)

reverse(arr, k, n - 1)

print(*arr)

# explanation

# Step 1: Reverse the entire array.
# 7 6 5 4 3 2 1


# Step 2: Reverse the first k elements.

# Reverse the first 3 elements:
# 5 6 7 4 3 2 1


# Step 3: Reverse the remaining elements.

# Reverse the elements from index 3 to index 6:
# 5 6 7 1 2 3 4


# Final answer
# 5 6 7 1 2 3 4


# Why do we use k = k % n?
# Suppose:
# - n = 7
# - k = 10
# Rotating 7 positions gives the original array. Therefore, rotating 10 positions is equivalent to rotating 3 positions.