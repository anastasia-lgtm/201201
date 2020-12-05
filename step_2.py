...

group_28 = ['Анастасия','Ирина','Екатерина',"Полина"]
#               0        1        2           ?
#                                            -1

# print(group_28[2])
print(group_28[len(group_28) -1])  # not ok
print(group_28[-1])  # ok

group_28.append('Влад')
print(group_28)

group_28.insert(2, 'Георгий')
print(group_28)

last_student = group_28.pop()
print(last_student)
print(group_28)

