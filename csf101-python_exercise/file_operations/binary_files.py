#Write a function that creates a binary file containing some bytes.
def create_binary_file(filename):
    data = bytes([0,1,2,3,4,5])
    with open(filename, 'wb') as file:
        file.write(data)
create_binary_file('binary_sample.bin')
print("binary file created successfully.")
#Write a function that reads and prints the contents of the binary file as bytes.
def read_binary_file(filename):
    with open (filename, 'rb') as file:
        content= file.read()
        print("binary file content:", content)
read_binary_file('binary_sample.bin')
#Write a function that appends bytes to an existing binary file.
def append_to_binary_file(filename, data):
    with open(filename, 'ab') as file:
        file.write(data)
append_to_binary_file('binary_ample.bin', bytes([6,7,8,9]))
print("bytes appended to binary")
read_binary_file('binary_sample.bin')
