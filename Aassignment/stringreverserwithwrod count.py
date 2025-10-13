def string_reverser():
    while True:
        text = input("Enter a sentence to reverse: ").strip()

        if not text:
            print("Input cannot be empty. Please try again.")
            continue

        reversed_text = text[::-1]  # [::-1] means start from the end and move backone step at a time and collect all characters
        words = text.split()  # splits the text into words and it will automatically ignores extra spaces
        word_count = len(words)  # counts how many words are in the list

        print(f"Reversed string: {reversed_text}")
        print(f"Word count: {word_count}")

        again = input("Do you want to continue? (yes/no): ").strip().lower()
        if again == "yes":
            continue
        elif again == "no":
            print("Kadrinchoe!")  # polite farewell :)
            break
        else:
            print("Invalid input yasiiiii bhaiiii")
            break

string_reverser()