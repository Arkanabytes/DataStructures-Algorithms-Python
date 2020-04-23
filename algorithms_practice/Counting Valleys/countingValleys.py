

def countingValleys(n, s):
    step = 0
    prev = 0
    num_valley = 0
    for i in s:
        if i == 'U':
            prev = step
            step += 1
        if i == 'D':
            prev = step
            step -= 1
        if prev == -1 and step == 0:
            num_valley += 1
    return num_valley

    
n = 8
s ="DDUUDDUDUUUD"
print(countingValleys(n,s))