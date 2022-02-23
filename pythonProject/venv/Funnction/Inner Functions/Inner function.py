#nested functions

def outer():
    print(" i am from outer ")
    def inner():
        print("i am from inner")
    inner()
outer()