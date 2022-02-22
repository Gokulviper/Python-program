price=1#global varible

def hike():
    global price #getting global vraiable
    print(price)
hike()

def hikee():
    price=1243 #local variable
    print(price)
hikee()

