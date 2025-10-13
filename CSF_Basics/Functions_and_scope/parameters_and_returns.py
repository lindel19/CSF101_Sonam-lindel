def greet_with_default(name="damchey"):
    print(f"hello, {name}")
greet_with_default()
greet_with_default("lindel")

def calculate_rectangle_area(width,length):
    return width * length
area= calculate_rectangle_area(5, 4)
print(f"the area of the rectangle is: {area}")

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="lindel", age=19 , city="thimphu")
def min_max(numbers):
    return min(numbers), max(numbers)
results= min_max([5,2, 9, 1, 6])
print(f"min; {results[0]}, max: {results[1]}")
def safe_divide(a,b):
     if b==0:
        return "cannot divide by zero"
     return a / b
print(safe_divide(10, 2))   
print(safe_divide(10, 0))