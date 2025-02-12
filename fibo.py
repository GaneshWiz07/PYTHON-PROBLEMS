n=int(input("Enter the value of n: "))
a,b=0,1
print(f"Fibonacci Series of {n} is:")
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
