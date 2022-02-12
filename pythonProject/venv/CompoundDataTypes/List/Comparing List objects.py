#comparing list object
a=[2,5,7,8,9,0]
b=[2,5,7,8,9,0]


print(a is b)#this is false because this check memeory address
print(a==b)#this is frue this comparre inside object
print(a<b)

#membership operrators -> in , not in
print(2 in a)#true
print(2 not in a)#false

#remove all values
a.clear();
print(a)