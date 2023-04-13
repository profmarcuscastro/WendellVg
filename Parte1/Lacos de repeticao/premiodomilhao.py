n = int(input())
total=0
d=0
while n>0:
    d+=1
    n = n -1
    a = int(input())
    total+= a
    if total>=1000000:
        break

print(d)