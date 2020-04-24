

def repeatedString(s, n):
    lengh = len(s)
    extraCharm = n % lengh
    num_a = 0
    num_a_extra = 0
    result = 0

    for j,i in enumerate(s):
        if i == "a":
            num_a += 1
        if i == "a" and j < extraCharm:
            num_a_extra +=1
    result = ((n // lengh ) * num_a) + num_a_extra
    return result


s = "aba"
n = 10
print(repeatedString(s,n))
