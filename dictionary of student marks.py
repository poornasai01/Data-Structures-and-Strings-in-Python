dictionary = {
    'Poornasai': 98,
    'Tarak': 95,
    'Maheshbabu': 91,
    'Ram': 35,
    'Raviteja': 55,
    'Nag': 75,
    'Chaitanya': 64,
    'Akhil': 22,
    'Venky': 72,
    'Nani': 88,
}

student_name = input("Enter the student's name: ")
marks = dictionary.get(student_name)
if student_name in dictionary:
    print("{}'s marks: {}".format(student_name, marks))
else:
    print("Student not found")