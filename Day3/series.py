def fibonacci(n):
    global a
    global b
    global fibonacci_list
    for i in range(n):
        next_term=a+b
        fibonacci_list.append(next_term)
        a=b
        b=next_term
def prime_numbers(n):
    global prime_list
    i=0
    k=2
    while i<n:
        c=1
        for j in range(2,k):
            if k%j==0:
                c=0
        if c:
            prime_list.append(k)
            i+=1
        k+=1
a,b=1,2
prime_list=[]
fibonacci_list=[a,b]
n=13
fibonacci(n)
prime_numbers(n)
combined_list=sorted(prime_list+fibonacci_list)
print(combined_list)
print(combined_list[n-1])