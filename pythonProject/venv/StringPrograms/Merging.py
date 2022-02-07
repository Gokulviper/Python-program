#input :A5B6C7
#otput: ABC567

s='A5B6C7'
alpha=''
numeric=''
ans=''
for i in s:
    if i.isalpha():
        alpha+=i
    else:
        numeric+=i

ans=alpha+numeric
print(ans)