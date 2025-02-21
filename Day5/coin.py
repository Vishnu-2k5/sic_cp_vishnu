amt=int(input("Enter the amount:"))
denomination_list=list(map(int,input("Enter the denominations:").split()))
denomination_list.sort(reverse=True)
for i in denomination_list:
    no_of_coins=amt//i
    print(f"Number of {i}'s required are {no_of_coins}")
    amt%=i