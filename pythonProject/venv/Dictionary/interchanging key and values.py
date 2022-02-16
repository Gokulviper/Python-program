#interchanging keys and values
employees={'kathiravn':234,'gokul':45,'harish':453,'gokila':235}
emp={}
for i,j in employees.items():
   emp[j]=i
print(emp)

print(emp.get(234))


