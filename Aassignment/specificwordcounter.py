import urllib.request  #Imports the urllib library wwhich allows Python to fetch text content from a URL
def specific_word_counter():
    specific_words = ["is", "are", "has", "have"] # List of specific words to count

    while True:
        source = input("Do you want to use a (F)ile or (U)RL? ").strip().upper() #strip() removes any spaces and upper() converts input to uppercase
        text = "" #initializes an empty string to store the text contentt

        if source == "F": #Handles the local file option
            file_path = input("Enter the path of the text file: ").strip() #file path on my laptop is "C:\\Users\\sonam\\OneDrive\\Documents\\webpage.txt"
            try:
                with open(file_path, "r", encoding="utf-8") as file: #opens the file and encoding='utf-8' makes sure that it can read most of the texts in a text file
                    text = file.read()  # Read all text from the file
            except FileNotFoundError:
                print("File not found! Try again.")
                continue  
            except Exception as e:
                print(f"Error: {e}")
                continue  # Restart loop for other file errors

        elif source == "U": #this handles the url option
            url = input("Enter the URL of the webpage: ").strip()#the url is https://gist.github.com/konrados/a1289ade329ac6f4598ebf5ee3dbcb3c
            try:
                response = urllib.request.urlopen(url) # this code fetches the contents to read from the webpage
                text = response.read().decode("utf-8")  # Convert bytes from thr webpage/url to a string
            except Exception as e:
                print(f"Failed to fetch URL: {e}") #Catches errors like invalid URL no internet or fetch failure
                continue  # Restart loop if URL fails

        else:
            print("Invalid choice! Enter 'F' for file or 'U' for URL.")
            continue  # Restart loop if user input is invalid

        words_in_text = text.lower().split()  # Convert text to lowercase and split the texts into a list of words
        counts = {word: words_in_text.count(word) for word in specific_words}  # Count each specific word in the given text file or url

        print("Word counts for specific words:")
        for word, count in counts.items():  # Loopss through the dictionary to print each word and its countt
            print(f"{word}: {count}")

        again = input("Do you want to analyze another source? (yes/no): ").strip().lower()
        if again == "yes":
            continue
        elif again == "no":
            print("Kadrinchoe!")  
            break  
        else:
            print("Invalid inputt exiting program")
            break

specific_word_counter()