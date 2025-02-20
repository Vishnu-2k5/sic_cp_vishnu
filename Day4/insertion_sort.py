arr=[int(element) for element in input().split()]
print(arr)
qsarr=[]
qsarr.append(arr[0])
for i in arr[1:]:
    j=0
    while j<len(qsarr) and i>qsarr[j]:
        j+=1
    qsarr.insert(j,i)
print(qsarr)
