number=input("Enter a number:")
"""for i in number[::2]:
    if int(i)%2==0:
        sum_of_odd_positions+=int(i)
print(sum_of_odd_positions)"""

print(sum([int(i) for i in number[::2] if int(i)%2==0]))