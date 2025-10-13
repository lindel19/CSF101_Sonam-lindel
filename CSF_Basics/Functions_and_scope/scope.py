x = 10
def print_x():
    x = 20
    print(f"local x: {x}")
print_x()
print(f"global x: {x}")

count = 0 
def increment():
    global count
    count+= 1 
    print(f"count: {count}")
increment()
increment()
print(f"final count: {count}")

def outer():
    x = 5
    def inner():
        nonlocal x
        x = "inner"
        print(f"inner x: {x}")
    inner()
    print(f"outer x: {x}")
outer()
