def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
n=int(input(("Enter a number: ")))
print(f"Factorial of {n} is: ",fact(n))
x=1
for i in range(1,n+1):
    x=x*i
print(f"Factorial of {n} without function is: ",x)
