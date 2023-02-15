v = 0
n = 0

while n<6:
    n = n+1
    a = float(input())

    if a>0:
        v = v+1
    s = a
    if s<0:
        x = a+a
        x = float(x/2)

print(f'{v} valores positivos')
print(x)



