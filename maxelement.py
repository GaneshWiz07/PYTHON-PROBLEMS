def Max(List):
    max=0
    for num in List:
        if num>=max:
            max=num
    return max
List=[  int(x) for x in input("Enter the list elements:").split()]
print("Maximum element in the list is: ",max(List))
print("Maximum element in the list with user defined function: ",Max(List))