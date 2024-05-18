grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades_x = 0
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(students)
students_x = 0
for i in grades:
    print(students_list[students_x],  ((sum(grades[grades_x]) / len(grades[grades_x]))))
    grades_x = grades_x + 1
    students_x = students_x + 1