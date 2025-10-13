"""
============================================================
               DOCUMENTATION: PYTHON DATA TYPES
============================================================

Topic: Booleans, Numbers, Strings, and Type Conversion
Language: Python
Author: Sonam Lindel
------------------------------------------------------------

Main Concepts Applied
---------------------
1. Clarity and Readability:
   All examples are written in simple, understandable syntax with meaningful variable names.
   The focus is on demonstrating each concept clearly and logically.

2. Precision:
   Each data type is used according to its purpose — numeric operations for numbers,
   logical conditions for booleans, and text manipulation for strings.
   Type conversion examples show how to correctly transform one type into another.

3. Practical Understanding:
   The examples are designed to show real use cases such as arithmetic operations,
   conditional logic, string formatting, and type casting.

------------------------------------------------------------
"""

# ============================================================
# 1. BOOLEANS
# ============================================================

# Booleans represent truth values: True or False.
# They are commonly used in conditions, comparisons, and control statements.

is_logged_in = True
has_permission = False

# Boolean results from comparisons:
a = 10
b = 5
print(a > b)   # True
print(a == b)  # False

# Values that are considered False:
# 0, 0.0, "", [], (), {}, None
# All other values evaluate to True when converted to boolean.

"""
Reflection on Booleans
----------------------
I learned that booleans are the foundation of decision-making in programming.
They allow the program to branch into different paths depending on True or False conditions.
Understanding how non-boolean values (like 0 or empty strings) behave in boolean contexts
helps in writing cleaner and more predictable conditional statements.
"""


# ============================================================
# 2. NUMBERS
# ============================================================

# Python supports:
# - int: whole numbers
# - float: numbers with decimals
# - complex: numbers with real and imaginary parts

x = 10       # int
y = 3.5      # float
z = 2 + 4j   # complex

# Basic arithmetic operations
print(x + y)   # 13.5
print(x - y)   # 6.5
print(x * y)   # 35.0
print(x / 3)   # 3.333...
print(x // 3)  # 3 (floor division)
print(x % 3)   # 1 (modulus)
print(x ** 2)  # 100 (power)

"""
Reflection on Numbers
---------------------
Working with numbers in Python reinforced my understanding of data types and precision.
Unlike some languages, Python automatically distinguishes between integers and floats.
Learning how different operators behave (especially floor division and modulus)
taught me how to perform accurate calculations for real-world applications like
temperature conversions, averages, and mathematical modeling.
"""


# ============================================================
# 3. STRINGS
# ============================================================

# Strings are sequences of characters inside quotes.
# They are used for storing and manipulating text.

name = "Sonam"
greeting = "Hello"
message = """This is
a multi-line
string."""

# Concatenation and formatting
full_message = greeting + " " + name
print(full_message)

# Indexing and slicing
print(name[0])     # S
print(name[1:4])   # ona

# String methods
print(name.upper())       # SONAM
print(name.lower())       # sonam
print(name.replace("S", "T"))  # Tonam
print(len(name))          # 5

# Formatted strings
age = 19
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))

"""
Reflection on Strings
---------------------
Through this section, I learned how versatile strings are in Python.
They are not only for storing text but also for formatting output and displaying information clearly.
Using indexing and slicing helped me understand how strings are stored as character sequences.
Methods like .upper(), .lower(), and .replace() showed me how powerful built-in string manipulation can be.
"""


# ============================================================
# 4. TYPE CONVERSION
# ============================================================

# Type conversion allows changing a variable from one type to another.
# Common functions: int(), float(), str(), bool()

a = 10
b = 3.5
c = "25"

# Examples of conversions
print(int(b))     # 3 (float → int)
print(float(a))   # 10.0 (int → float)
print(int(c))     # 25 (string → int)
print(str(a))     # "10" (int → string)
print(bool(0))    # False
print(bool(100))  # True

# Checking types
print(type(a))    # <class 'int'>
print(type(b))    # <class 'float'>
print(type(c))    # <class 'str'>

"""
Reflection on Type Conversion
-----------------------------
I learned that type conversion (casting) ensures compatibility between different data types.
For example, converting numbers to strings allows concatenation, while converting strings to numbers enables arithmetic.
Using the type() function to verify conversions improved my understanding of how Python handles data dynamically.
It also highlighted the importance of being explicit about conversions to avoid logical or runtime errors.
"""


# ============================================================
# FINAL REFLECTION AND SUMMARY
# ============================================================

"""
Summary
-------
This exercise gave me a strong foundation in Python’s basic data types:
booleans, numbers, strings, and type conversions. I realized that understanding
data types is essential before moving to advanced topics like loops and functions.

Booleans helped me think logically, numbers strengthened my mathematical reasoning,
strings improved my understanding of text manipulation, and type conversion
taught me how to manage data safely and flexibly.

Each of these concepts contributes to writing efficient, bug-free, and well-structured Python programs.
By practicing them, I’ve built confidence in handling and transforming data effectively in any Python project.
"""
