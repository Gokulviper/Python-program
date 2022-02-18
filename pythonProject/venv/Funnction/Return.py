#you can return many return statements in single function

def cal(no1,no2):
    add=no2+no1
    sub=no2-no1
    mul=no2*no1
    return add,sub,mul

print(cal(10,10))
ans=cal(2,2)
print(type(ans))

#type is tuple
#packing and unpacking is tuple