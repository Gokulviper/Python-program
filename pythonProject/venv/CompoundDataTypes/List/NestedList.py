l=[[1,3,5],
   [34,5,2],
   [3,7,9]]

#for i in l:
#   for j in i:
#       print(j,end=' ')
#    print()


#print(l[0][0])
#diagonal
#transpose
k=0
sum=0;
for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        #if(j==k):
            #sum+=l[i][j]
            print(l[j][i],end=' ')

    print()
  #  k+=1
#print(sum)