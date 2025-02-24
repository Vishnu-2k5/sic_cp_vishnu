t=int(input("Enter the number of test cases:"))
result=[]
for i in range(t):
    n=int(input("Enter the number of boys and girls:"))
    b=list(map(int,input(f"Enter the height of {n} boys:").split()))
    g=list(map(int,input(f"Enter the height of {n} girls:").split()))
    students=sorted(b+g)
    res=True
    for i in range(0,len(students),2):
        if (students[i] in b and students[i+1] in g ):
            continue
        else:
            res=False
    print(students)
    if  not res:
        for i in range(0,len(students),2):
            if (students[i] in g and students[i+1] in b ):
                res=True
            else:
                res=False
    if res:
        result.append("Yes")
    else:
        result.append("No")

for i in result:
    print(i)