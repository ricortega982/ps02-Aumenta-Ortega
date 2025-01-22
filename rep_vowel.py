sentence = "Python is fun and python is easy to learn"
vowels = ("aeiou")
letter = ""

for x in sentence:
    if x.lower() in vowels:
        letter += x.upper()
    else:
        letter += x
print(letter)