'''
74,240,378
'''

def searchMatrix(matrix : List[List[int]], target: int) -> bool:
    arr = []
    for row in matrix:
        arr += row 
    n = len(arr)
    l,r = 0,n-1 
    while l <= r:
        mid = (l+r)//2 
        if target == arr[mid]:
            return True 
        elif target < arr[mid]:
            r += mid - 1
        else:
            l = mid + 1 
    return False 
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix,target))