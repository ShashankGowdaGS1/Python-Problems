def sec_BigInt(l):
    big = l[0]
    sec_big = -1
    for num in l:
        if num>big:
            sec_big = big
            big = num
        elif num>sec_big and num!=big:
            sec_big  = num
    #print(big)
    if sec_big==-1:
        return None
    return sec_big
    
l=[10,20,40,5,15]
res = sec_BigInt(l)
print(res)