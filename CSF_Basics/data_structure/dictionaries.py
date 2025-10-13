name = "lindel"
age = 19
height = 172
is_student = True
person_info = {
    "name": name,
    "age": age,
    height: height,
    "is_student": is_student
}
print(person_info)
person_info["favorite_color"]= "black"
print(person_info)
try:
    print(person_info['weight'])
except KeyError as e:
    print(f"KeyError: {e}")    