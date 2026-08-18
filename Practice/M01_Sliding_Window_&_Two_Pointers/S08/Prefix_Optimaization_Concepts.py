nums = [1,2,3,4]
res = [0] * (len(nums))
for i in range(len(nums)):
    curr_sum = 0 
    for j in range(0,i+1):
        curr_sum += nums[j]
    res[i] = curr_sum 
print(res) 


#optimal solution
nums = [1,2,3,4]
for i in range(1,len(nums)):
    nums[i] = nums[i-1] + nums[i]
print(nums)


1732 

n = len(gain)
alt = [0] * (n+1)  this is what 
for i in range(1,n+1):
    alt[i] = alt[i-1] + gain[i-1]
print(max(alt))

#Optimal Solution
curr_alt =  0
max_alt = 0 
for g in gain:
    curr_alt += g 
    max_alt = max(curr_alt, max_alt)
return max_alt