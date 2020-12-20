a = float(input('Число а = '))
b = float(input('Число b = '))
c = float(input('Число c = '))

if (a>=b):
    min1 = b
else:
    min1 = a

if (b>=c):
    min2 = c
else:
    min2 = b

d = min1 + min2**2

print(d)