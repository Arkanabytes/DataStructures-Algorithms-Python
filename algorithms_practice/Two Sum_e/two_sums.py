def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    h = {}
    i = 0
    for num in nums:
        n = target - num
        if n not in h:
            h[num] = i
            i+=1
        else:
            return [h[n],i]
            

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums,target))
