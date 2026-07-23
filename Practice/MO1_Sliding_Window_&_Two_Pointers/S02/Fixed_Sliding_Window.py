from typing import List
def findMaxAverage(nums: List[int], k: int) -> float:
    max_sum = float("-inf")
    n = len(nums)
    for i in range(n-k+1):
        sub_sum = 0 
        for j in range(i, k+i):
            sub_sum += nums[j]
        max_sum = max(max_sum,sub_sum)
    return max_sum/k 
nums = [1,12,-5,-6,50,3]   
k = 4 
print(findMaxAverage(nums,k))


def findMaxAverage_Optimal(nums: List[int],k: int)
