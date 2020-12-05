...

housing = ['House', 'Apartment', 'Studio', 'Motel']
#             0          1           2         3
#            -4         -3          -2        -1

print('House: 40.000$')
print('Apartment: 9.000$')
print('Studio: 17.500$')
print('Motel: 3.500$')

print('Жилье которое стоит дороже 34,000$:')
print('1.', housing[-4])

print('Жилье которое стоит дешевле 4.000$:')
print('1.', housing[1])
print('2.', housing[-1])

print('Оптимальным жильем является:')
print(housing[-2])

print('Худшем жильем является:')
print(housing[3])


