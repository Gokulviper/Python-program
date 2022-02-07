#adding 2 strings one by one

s1='gokul'
s2='rajanarajn'
ans='';
templen=0
length=0
current='';
if len(s1)<len(s2):
    length=len(s1)
    current=s2
    templen=len(s2)
else:
    length=len(s2)
    current=s1
    templen = len(s1)
i=0
for i in range(0,length):
    ans=ans+s1[i]+s2[i]
for i in range(0,templen):
    ans=ans+current[i]
print(ans)


























