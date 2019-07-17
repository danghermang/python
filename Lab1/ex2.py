vocale="aeiou"
string=input("Gimme the string:\n")
total=0
for char in vocale:
    total+=string.lower().count(char)
print(total)
