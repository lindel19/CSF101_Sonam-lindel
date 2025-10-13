#Write a function that checks if a file exists.
import os
def file_exists(filename):
    return os.path.isfile(filename)
print(f"sample.txt exists: {file_exists('sample.txt')}")
print(f"nonexsistent.txt exists: {file_exists('nonexistent.txt')}")
#Write a function that renames a file.
import os 
"""def rename_file(old_name, new_name):
    os.rename(old_name, new_name)
rename_file ('sample.txt', 'renamed_sample.txt')
print("File renamed successfully.")
print(f"'renamed_sample.txt' exists:{file_exists('renamed_sample.txt')}")"""
#Write a function that deletes a file.
import os
def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} has been deleted.")
    else:
        print(f"{filename} does not exist.")
delete_file('binary_sample.bin')
#Write a function that creates a new directory.
import os
def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"directory '{directory_name}' created successfully")
    else:
        print(f"directory '{directory_name}' already exists.")
create_directory('new_folder')
#Write a function that lists all files in a directory.
import os
def list_files(directory):
    files= os.listdir(directory)
    for file in files:
        print(file)
print("Files in current directory:")
list_files('.')
#Write a function that copies a file from one location to another.
import shutil
def copy_file(source, destination):
    shutil.copy(source, destination)
    print(f"File copied from {source} to {destination}.")
copy_file('renamed_sample.txt', 'new_folder/copied_sample.txt')
#Write a function that reads a CSV file and prints its contents.
import csv
def read_csv_file(filename):
    with open(filename, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(','.join(row))
#creating a sample csv file
with open('sample.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Name', 'Age', 'City'])
    csv_writer.writerow(['Lindel', '19', 'Thimphu'])
    csv_writer.writerow(['Karma', '20', 'Paro'])
print("contents of sample.csv:")
read_csv_file('sample.csv')