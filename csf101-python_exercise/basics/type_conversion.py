age = 19
age_str = str(age)
message = "i am " +age_str + " years old"
print(message)
num_str = "69"
num_int = int(num_str)
print(num_int)
non_num_str = "kuzu"
try:
    non_num_int = int(non_num_str)
    print(non_num_int)
except ValueError as e:
    print(f"error: {e}")