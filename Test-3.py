import math
x1 = int(input('Введіть значення x точки A = ')) #A
y1 = int(input('Введіть значення y точки A = '))

x2 = int(input('Введіть значення x точки B = ')) #B
y2 = int(input('Введіть значення y точки B = '))

x3 = int(input('Введіть значення x точки C = ')) #C
y3 = int(input('Введіть значення y точки C = '))

AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
BC = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
AC = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)

p = (AB+BC+AC)

print(p)