def numPrint(n):
    if(n==0):
        print(n)
        return

    numPrint(n-1)
    print(n)
numPrint(8)



