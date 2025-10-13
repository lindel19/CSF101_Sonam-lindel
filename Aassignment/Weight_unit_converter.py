def weight_converter():
    while True: #creates a infinite loop in which it lets the user perform multiple conversions until they choose to exit
        try:     #Begins a block that checks for possible input errors (like typing a word instead of a number)
            weight = float(input("Enter the weight to convert: "))
        except ValueError:    # If the input is not a valid number it catches the error and prompts the user again
            print("Invalid input! Please enter a numeric value.")
            continue  # Go back to start if invalid input
        
        choice = input("Convert to (P) pounds or (K) kilograms? : ").strip().upper() #we use strip() to remove any spaces and upper() to convert the input to uppercase reason being the program to accept both lowercase and uppercase inputs

        # Kilograms → Pounds
        if choice == "P":
            converted = round(weight * 2.20462, 2)#we use round() to keep the answer to 2 decimal places 
            print(f"{weight} kilograms = {converted} pounds")

        # Pounds → Kilograms
        elif choice == "K":
            converted = round(weight / 2.20462, 2)
            print(f"{weight} pounds = {converted} kilograms")
        else:
            print("Invalid option! Enter 'P' for pounds or 'K' for kilograms.")

        # Ask if the user wants to continue or exit
        again = input("Do you want to continue? (yes/no): ").strip().lower()
        if again == "yes":
            continue  # repeat
        elif again == "no":
            print("Kadrinchoe!")  # just Kadrinchoe :)
            break
        else:
            print("Invalid input, bye.")
            break
# call the function to run the converter
weight_converter()