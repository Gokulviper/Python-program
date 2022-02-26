class Student:
    #documentation string = what type main concept of the class
    '''
this class is about student
    '''
    name='gokul'
    age=26
    def marks():
        inputt=input("enter you mark")
        print(inputt," this your mark")
print(Student.__doc__)
help(Student)
Student.marks()