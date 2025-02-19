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
    c=0
    for i in range(2,n):
        if n%i==0:
            c=1
            continue
        else:
            prime_list.append(i)
a,b=1,2
prime_list=[]
fibonacci_list=[a,b]
n=5
fibonacci(n)
prime_numbers(n)
print(sorted(prime_list+fibonacci_list))