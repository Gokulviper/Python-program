l=[1,5,6,9,7]
#all posible double digit odd number combination

for i in l:
    for j in l:
        currrentNum=i*10+j
        if currrentNum%2!=0:
            print(currrentNum)
