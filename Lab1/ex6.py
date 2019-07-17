string = input("gimme stringz\n")
string2=''
string2+=string[0].lower()
for char in string[1:]:
    if char.isupper():
        string2+="_"+char.lower()
    else:
        string2+=char
print(string2)