import string
Sentence=set(input("Enter a sentence: ").lower().strip())
Alphabets=set(string.ascii_lowercase)
if Alphabets.issubset(Sentence):
    print("It is a Pangram sentence")
else:
    print("It is not a Pangram sentence")
