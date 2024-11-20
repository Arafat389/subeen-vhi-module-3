def selection_sort(nums):
    n = len(nums)
    for i in range (n-1):
        min_item = 100
        min_index = -1
        for j in range (i,n):
            if nums[j] < min_item:
                min_item = nums[j]
                nums[j] = j
        nums[min_index] = nums[i] 
        nums[i] = min_item

li = [2,1,4,3,7,5,8]
print("before shorting", li)
selection_sort(li)
print("after shorting ", li)               