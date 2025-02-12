n=int(input("Enter a number:"))
sum=0
while n>0:
    sum=sum+(n%10)
    n=n//10
print(f"Sum of n digits : ",sum)