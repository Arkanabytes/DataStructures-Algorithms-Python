
# working on....
def findlongestSubarraySum(arr,s):

    i = 0
    j = 1
    sum = arr[i]+arr[j]
    result = []
    max_len = 0

    while j < len(arr)-1:
        if sum < s:
            j += 1
            sum += arr[j]
        if sum > s:
            sum -= arr[i]
            i += 1
        if sum == s:
            if j - i + 1 > max_len:
                max_len = j - i + 1
                result = [i+1,j+1]
            j += 1
    return result

# arr = [1,2,3,7,5]
# s = 12

arr = [1,2,3,4,5,0,0,0,6,7,8,9,10]
s = 15
print(findlongestSubarraySum(arr,s))