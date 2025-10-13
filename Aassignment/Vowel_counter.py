def vowel_counter():
    while True:
        text = input("Enter a sentence or word: ").strip()

        if not text:  # checks if the user entered nothing
            print("Input cannot be empty. Please try again.")
            continue

        vowels = "aeiouAEIOU"
        count = sum(1 for char in text if char in vowels)

        print(f"Total vowels in the given text: {count}")

        again = input("Do you want to continue? (yes/no): ").strip().lower()
        if again == "yes":
            continue
        elif again == "no":
            print("Kadrinchoe!")  
            break
        else:
            print("Ya Lasooo Invalid input ")
            break
vowel_counter()