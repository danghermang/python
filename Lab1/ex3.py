import re
string=input("gimme the string\n")
lista=re.findall(r"[A-Za-z]+", string)
print(len(lista))