def frequency_CharInStr(str):
    count = {}

    for ch in str:
        if ch in count:
            count[ch] +=1
        else:
            count[ch] = 1
    return count

str = "banana"
res = frequency_CharInStr(str)
print(res)
