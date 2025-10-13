def perfect_number_sum(start, end):
    def sum_is_perfect(n):
        if n < 2:  #we use if n<2 since any number less than 2 cannot be perfect
            return False
        divisors_total = sum([i for i in range(1, n) if n % i == 0])# i used n % i ==0 to check if i is a divisor of n
        return divisors_total == n

    total = sum([n for n in range(start, end + 1) if sum_is_perfect(n)]) #this code i used to go through every number from start to end and uses is_perfect if it is then it is added tothe toatl
    return total

while True:  #using while to create a loop for the user to continue or exit
    try:  #i am using try and except to catch errors if the user enters string or empty space instead of integers
        start = int(input("Enter first number: "))
        end = int(input("Enter second number: "))
        result = perfect_number_sum(start, end)  #we call the function here and send start and end as arguments and store the result in result variable
        print(f"Sum of all perfect numbers between {start} and {end}: {result}")

    except ValueError:#we use this to catch errors if the user enters string or empty space instead of integers
        print("Invalid input, no empty space or string, please enter integers only.")
        continue
        
    again = input("Do you want to continue? (yes/no): ")
    if again == "yes":
       continue #this statement will allow the user to start over 
    elif again == "no":
      print("kadrinchoe!")
      break
    else:
      print("Invalid input, exiting the program marayy.")
      break
       
