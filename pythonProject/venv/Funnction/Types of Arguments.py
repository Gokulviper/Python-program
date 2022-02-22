#1 position arguments
def add(no1,name):
    print(no1,'is your name',name)

add(10,'gokul')
#input type won't changed


#2 keyword argument

def add1(no,name):
    print(no, 'is your name', name)

add1(name='gokyl',no=23)
#you can change the order thats not a issue





#3 default arguments

def dicount(rate,dis=10):
    print('your discount is',rate-dis)


dicount(100,20)
dicount(100)
#you can give the value that are executed you cannot give the default will be executed





#4 variable length arguments
#similar to method overloading in java

def totalMarks(*n):
    total=0
    for i in n:
        total+=i;
    print(total)

totalMarks(13,31,13,13)
totalMarks(23)
totalMarks()
totalMarks(213,23)


