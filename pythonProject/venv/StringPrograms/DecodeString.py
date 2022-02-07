s1='temp23'
#output=AAAAA
temp=''
num=1;
count=1
for i in s1:
    if i.isalpha():
        temp+=i;
    elif i.isdigit():
        if count>1:
            num=num*10+int(i)

            continue
        num=int(i)
        count += 1
print(temp*num)