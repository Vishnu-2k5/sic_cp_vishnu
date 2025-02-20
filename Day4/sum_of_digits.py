import sys
number=(sys.argv[1])
print(number)
print("Sum of odd placed even digits = ",sum([int(number[i]) for i in range(0,len(sys.argv[1]),2) if int(number[i])%2==0]))
print("Sum of odd placed odd digits = ",sum([int(number[i]) for i in range(0,len(sys.argv[1]),2) if int(number[i])%2==1]))
print("Sum of even placed odd digits = ",sum([int(number[i]) for i in range(1,len(sys.argv[1]),2) if int(number[i])%2==1]))
print("Sum of even placed even digits = ",sum([int(number[i]) for i in range(1,len(sys.argv[1]),2) if int(number[i])%2==0]))