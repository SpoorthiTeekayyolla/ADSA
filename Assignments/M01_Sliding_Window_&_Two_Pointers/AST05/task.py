# task.py

from typing import List

def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n

    # Store product of all elements to the left
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    # Multiply with product of all elements to the right
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(productExceptSelf(arr))