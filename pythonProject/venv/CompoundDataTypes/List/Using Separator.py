#convart list to String
input='sun mon Tues wed satur fri Thus'
day='day'
list=[]
words=input.split()


for i in words:
   if( i.startswith('T')):
       #or
      # if(i[0]=='T'):

    list.append(i+day)

output=' '.join(list)
print(output)