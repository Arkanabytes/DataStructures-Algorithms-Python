

def jumpingOnClouds(c):
    count = 0
    len1 = len(c)-1
    i = 0

    while(i < len1):
        if c[i] == 0 and i+2 <= len1 and c[i+2] == 0:
            count += 1
            i += 2
        else:
            count += 1
            i += 1

    return count

c = [1,0,0,0,1,0] # output: 3
# c = [0,1,0,0,0,1,0] # output: 3
# c = [0,0,1,0,0,1,0] # output: 4
print(jumpingOnClouds(c))