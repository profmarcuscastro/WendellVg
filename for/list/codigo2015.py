n= int(input())
l = map(int,input().split())
l = list(l)
n=0
for i in range(len(l)-2):
    if l[i]==1:
        if l[i+1]==0 and l[i+2]==0:
            n+=1

print(n)