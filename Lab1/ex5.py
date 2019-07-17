string = input("gimme stringz\n")
special=[r"\r", r"\t", r"\n", r"\a", r"\b", r"\f", r"\v"]
has=True
for i in special:
    if string.find(i)>=0:
        print(has)
        break
if not has:
    print(has)