def add(n,total):
    if(n==0):
        print(total)
        return
    add(n-1,total*n)
#add(5,1)

def adddigits(n,total):
    if(n==0):
        print(total)
        return
    adddigits(n//10,total+n%10)
adddigits(53,0)

