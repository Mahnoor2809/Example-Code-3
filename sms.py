students = []
for i in range(2):
    student = {}
    student['Name'] = input('Please enter student name: ')
    student['Father Name'] = input('Please enter father name: ')
    student['Cell number'] = input('Please enter Cell Number: ')
    students.append(student)
    print('Currently Enrolled Students: ', len(students))

    #DELETE FUNCTION:
#1
# for student in students:
#         #print('student')
#         #print(student)
#         if student['Name'].lower() == 'inam':
#           del student["Name"]
#           del student["Father Name"]
#           del student["Cell number"]
#2
# for idx in range(len(students)):
#     if students[idx]['Name'].lower() == 'inam':
#         del students[idx]
# print(students)
#3
# for student in students:
#          #print('student')
#          #print(student)
#         if student['Name'].lower() == 'inam':
#             students.remove(student)
# print(students)
