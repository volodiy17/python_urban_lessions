grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# students = list(students)
# students.sort()
# grades = [sum(grade) / len(grade) for grade in grades]
# results = dict(zip(students, [sum(grade) / len(grade) for grade in grades]))
# print(results)

print(dict(zip(sorted(list(students)), [sum(grade) / len(grade) for grade in grades])))