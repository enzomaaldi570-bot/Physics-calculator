import math 

a = float(input('force(N): '))
b = float(input('distance(M): '))
c = float(input('angle (º): '))

d = math.radians(c)
e = math.sin(d)

result = a * b * e
print('result', result)
