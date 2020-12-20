x = float(input('Введіть значення X = '))
b = 2*(x)**2-x-3

if(b == 0):
    y=1
else:
    if(b > 0):
        y=2
    else:
        if(b < 0):
            y=0

print('y = {0}'.format(y))

