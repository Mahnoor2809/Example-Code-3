import csv 
# with open('data.csv') as fdr:
#     students = csv.reader(fdr)
#     for student in students:
#         print(student)

single_student = ['Inam', 'AI', '1530-1830' ]
students = [
     ['Inam', 'AI', '1530-1830' ],
     ['Inam', 'AI', '1530-1830' ],
     ['Inam', 'AI', '1530-1830' ],
     ['Inam', 'AI', '1530-1830' ],
     ['Inam', 'AI', '1530-1830' ],
     ['Inam', 'AI', '1530-1830' ],
     ['Inam', 'AI', '1530-1830' ],
     ['Inam', 'AI', '1530-1830' ],
     ['Inam', 'AI', '1530-1830' ],
]
print(single_student)
with open('data.csv','w', newline='') as fdes:
    writer = csv.writer(fdes, delimiter=',')
    #writer.writerow(single_student)
    for student in students:
     writer.writerow(student)