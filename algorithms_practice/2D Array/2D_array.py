

def hourglassSum(arr):
    num = 6
    min_value = -10000
    max_hr = min_value

    for i in range(num):
        for j in range(num):
            if j+3 <= 6 and i+3 <= 6:
                max_hr = max(calc_hoursum(arr,i,j), max_hr)

    return max_hr


def calc_hoursum(arr,row,col):
    sum = 0
    
    for i in range(row, row+3):
        for j in range(col, col+3):
                sum += arr[i][j]
    sum = sum - arr[row+1][col] - arr[row+1][col+2]

    return sum

# arr = [[1, 1, 1, 0, 0, 0],
#        [0, 1, 0, 0, 0, 0],
#        [1, 1, 1, 0, 0, 0],
#        [0, 0, 2, 4, 4, 0],
#        [0, 0, 0, 2, 0, 0],
#        [0, 0, 1, 2, 4, 0]]

#test:
# -1 -1 0 -9 -2 -2
# -2 -1 -6 -8 -2 -5
# -1 -1 -1 -2 -3 -4
# -1 -9 -2 -4 -4 -5
# -7 -3 -3 -2 -9 -9
# -1 -3 -1 -2 -4 -5

# 0 -4 -6 0 -7 -6
# -1 -2 -6 -8 -3 -1
# -8 -4 -2 -8 -8 -6
# -3 -1 -2 -5 -7 -4
# -3 -5 -3 -6 -6 -6
# -3 -6 0 -8 -6 -7

arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
print(hourglassSum(arr))
