def Reverce_str(str):
    rev_str=""

    for i in range(len(str)-1,-1,-1):
        rev_str += str[i]
    return rev_str

str = input("Enter string:\n")
result = Reverce_str(str)
print(result)