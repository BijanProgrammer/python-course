x = 23


def do_something():
    global x
    
    x = 42
    print("inside:", x)


print("before:", x)
do_something()
print("after:", x)
