String=input("Enter a String: ")
vowels=['A','a','E','e','I','i','O','o','U','u']
count=0
for letter in String:
    if letter in vowels:
        count+=1
print(f"Count of Vowels in the String \"{String}\" is:",count)