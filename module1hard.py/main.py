# Задание "Средний балл"
students = ['Johny','Bilbo','Steve', 'Khendrik', 'Aaron']
grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students_sort = sorted(students)
dict_ = {'Aaron':53354, 'Bilbo':2223, 'Johny':4552, 'Khendrik':443, 'Steve':55545}

Aaron = (5,3,3,5,4)
l_A = len(Aaron)    # - "len" - индекс последнего элемента списка Aaron
s_A = sum(Aaron)    # - "sum" - сумма всех чисел списка  Aaron

Bilbo = (2,2,2,3)
l_B = len(Bilbo)
s_B = sum(Bilbo)

Johny = (4,5,5,2)
l_J = len(Johny)
s_J = sum(Johny)

Khendrik = (4,4,3)
l_K = len(Khendrik)
s_K = sum(Khendrik)

Steve = (5,5,5,4,5)
l_S = len(Steve)
s_S = sum(Steve)

dict_.update({'Aaron': s_A/l_A,  # - "s_B/l_B" - рачет среднего значения оценки
              'Bilbo': s_B/l_B,
              'Johny': s_J/l_J,
              'Khendrik': s_K/l_K,
              'Steve':s_S/l_S })
print(dict_)
