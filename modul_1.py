grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_2 = list(students) # преобразую множество в список
students_2.sort() # сортирую список по алфавиту
sred_bal={students_2[0]:sum(grades[0])/len(grades[0]), students_2[1]:sum(grades[1])/len(grades[1]),
          students_2[2]:sum(grades[2])/len(grades[2]), students_2[3]:sum(grades[3])/len(grades[3]),
          students_2[4]:sum(grades[4])/len(grades[4])} # создаю словарь имя/средний балл
print(sred_bal) # вывод на экран словаря