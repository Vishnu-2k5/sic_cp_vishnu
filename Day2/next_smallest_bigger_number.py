n=input("Enter a number:")
num=list(n)
l=[]
for i in range(0,len(num)):
    for j in range(0,len(num)-1):
        num[j],num[j+1]=num[j+1],num[j]
        s=""
        for i in num:
            s+=i
        if int(s)>=int(n):
            l.append(s)
l=sorted(l)
if n!=l[-1]:
    print(l[1])
else:
    print("Not Possible")