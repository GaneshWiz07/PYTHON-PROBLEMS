n=int(input("Enter a number: "))
flag=1
if n<=1:
    flag=0
else:
    for i in range(2,int(n**0.5)+1):
        if i==2:
            flag=1
        if n%i==0:
            flag=0
            break
    print(f"{n} is a prime number") if flag==1 else print(f"{n} is not a prime number")