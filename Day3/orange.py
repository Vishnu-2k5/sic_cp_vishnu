no_of_oranges=int(input())
orange_stack=list(map(int,input().split()))
#print(orange_stack)
k=0
for i in range(no_of_oranges):
    if orange_stack[i]<orange_stack[no_of_oranges-1]:
        orange_stack[i],orange_stack[k]=orange_stack[k],orange_stack[i]
        k+=1
orange_stack[k],orange_stack[no_of_oranges-1]=orange_stack[no_of_oranges-1],orange_stack[k]
print(orange_stack)