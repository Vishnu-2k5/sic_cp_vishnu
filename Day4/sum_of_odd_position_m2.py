def simplification(number):
    sum_of_odd_positions=0
    dig=number%10
    if dig%2==0:
        sum_of_odd_positions+=dig
    number//=10
    return sum_of_odd_positions
number=int(input("Enter a number:"))
print(sum([simplification(number) for i in range(0,len(str(number))) if i%2!=0]))

        
#print(sum_of_odd_positions)