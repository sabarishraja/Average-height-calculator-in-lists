student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total = 0
for sum in student_heights:
    total+=sum
no_of_students = 0
for average in student_heights:
    no_of_students+=1
average_1 = total / no_of_students
print(str(round(average_1)))
    