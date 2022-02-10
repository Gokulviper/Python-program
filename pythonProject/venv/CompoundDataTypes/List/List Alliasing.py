#FOR both list same memory will be shared in list alliasing]
l1=[3,65,2]
l2=[2,6,8]
l2=l1[:]
print(l2)
#diifernt memory addres for list cloning

l2=l1
print(l2)
