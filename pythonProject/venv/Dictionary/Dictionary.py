#key and value pair
#no duplicate keys
#values are duplicate
#no insertion order maintained
#objects are mutable
#no indexing and no slicing

#creation dictionary
d={}
print(type(d))
d[12]='gokh'
d[56]='56'
d[98]='dfhgf'
#heterogenous valus allowed
d[22]=34

print(d)

f={12:'34',244:'fgf',235:234}
print(f)

#get value
print(d[12]) #you give the non contain key python through keyError
print(d.get(12))
print(d.get(34543))#you give the non contain key python not through keyError
print(d.pop(12))#get and remove key value error




#you can always change values using key
d[22]='arun'

print(d)

#remove key and value pair
del d[22]
print(d)

#removing all elements in set
#d.clear()

print(len(d))




