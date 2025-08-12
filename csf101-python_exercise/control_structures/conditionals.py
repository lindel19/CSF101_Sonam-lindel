number = 10
if number > 0:
    print("The number is positive.")
else:
    print("The number is non-positive.")
number = 0
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

score = 95
if score >=90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"The grade is: {grade}")
number = 19 
results = "even" if number % 2 == 0 else "odd"
print(f"the number is {results}.")
num1 = 10
num2 = 20
operator ="+"
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2 if num2 !=0 else "error: divison by zero"
else:
    result = "Invalid operator"
print(f"results: {result}")

   