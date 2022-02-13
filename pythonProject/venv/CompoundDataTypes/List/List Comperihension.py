#how to create list easily
ll=[i*i for i in range(1,16)]
print(ll)

#adding list in another list
ll2=[val for val in ll if val%2==0 ]
print(ll2)