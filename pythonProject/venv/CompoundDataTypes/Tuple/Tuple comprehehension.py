#tuple comprehension
#it can be change to the generator
t=(i**i for i in range(1,9))
print(type(t))
print(t)

for i in t:
    print(i,end=" ")
