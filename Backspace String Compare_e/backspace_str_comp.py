def backspaceCompare(S, T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """
    s_res = []
    t_res = []
    

    for i in S:
        if (i == '#' and len(s_res) > 0) : 
            s_res.pop()

        if (i != '#'):
            s_res.append(i)


    for j in T:
        if j == '#' and len(t_res) > 0:
            t_res.pop()

        if (j != '#'):
            t_res.append(j)
            
    if s_res == t_res:
        return True
    else:
        return False


S = "a#c"
T = "b"
print(backspaceCompare(S,T))