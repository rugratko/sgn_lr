print('Task 6')
x = int(input('Input x:'))
y = int(input('Input y:'))
if ((x**2)*y) > (x*(y**2)):
    a = ((x**2)*y)
else:
    a = (x*(y**2))
    
if (x-y) > (x+2*y):
    b = (x+2*y)
else:
    b = (x-y)
    
print('Ответ:', a**2 + b**2)