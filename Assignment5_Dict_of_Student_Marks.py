students_details = {'Alice':85, 'Carol': 90, 'Silvia': 70}

student_name = str(input("Please Enter a Student Name: ")).capitalize()

if student_name in students_details:
    print(f"{student_name}'s marks: {students_details[student_name]}")
else:
    print('Student Not Found.')
