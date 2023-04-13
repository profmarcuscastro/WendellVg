P1 = int(input())
C1 = int(input())
P2 = int(input())
C2 = int(input())

t1 = P1*C1
t2 = P2*C2

if t1>t2:
    print('-1')
elif t2>t1:
    print('1')
else:
    print('0')