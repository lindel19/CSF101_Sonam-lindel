def average_and_range_finder():
    while True:
        try:
            num = int(input("How many numbers do you want to enter? : "))
            if num <= 0: #this code Checks if the user entered zero or a negative number
                print("Please enter a positive number.")
                continue # it will make the program to Go back to start if invalid input
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        numbers = []  # empty list to store the inputs

        for i in range(num): #loop to get the numbers from the user
            try:
                value = float(input(f"Enter number {i + 1}: ")) #this code will ask the user to input the numbers one by one
                numbers.append(value) #.append() method to add each number to the list
            except ValueError:
                print("Invalid number! Please enter a numeric value.")
                break # this will male the user exit the loop if invalid input 

        if len(numbers) != num: #this code checks if the number of valid inputs matches the expected count if not it will go back to start
            continue

        avg = sum(numbers) / len(numbers) #Calculates the average by dividing the total sum by how many numbers there are using sum() and len() functions
        rng = max(numbers) - min(numbers) #Calculates the range by subtracting the smallest number from the largest number using max() and min() functions

        print(f"Average: {round(avg, 2)}, Range: {round(rng, 2)}") #displays the average and the range rounding both to 2 deciamls if there is

        again = input("Do you want to continue? (yes/no): ").strip().lower()
        if again == "yes":
            continue
        elif again == "no":
            print("Kadrinchoe!")  # just Kadrinchoe :)
            break
        else:
            print("Invalid input laaaaaaa.")
            break

average_and_range_finder()