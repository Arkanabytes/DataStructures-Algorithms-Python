

def sockMerchant(n, ar):
    dic = {}

    for i in ar:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    sum_socks = 0
    for i in dic:
        sum_socks += (dic[i]//2)
    
    return sum_socks


n = 9
ar = [10,20,20,10,10,30,50,10,20]
print(sockMerchant(n,ar))