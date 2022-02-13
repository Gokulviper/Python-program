#tuple is immutable
#insertion order is maintained
#duplicate values are allowed\
#slicing are allowed in tuple

t=(10,20,30,30)
print(t)

# A important note you can give the single value in tuple t=(10) this can python identifieed
#as a t=(10,) you can declared like this

t=(10,)

l=[23,23,23,10,10,1]
tu=(l)
print(tu)
#tuple

ttt=(tu[::-1])


#aading two tuples
t1=(10,20,30)
t2=(3,50,70)
t3=t2+t1
print(t3)
print(t3*3)