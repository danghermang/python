def get(number,*strings):
    check = True
    current=strings[0]
    for element in strings[1:]:
        if current[len(current)-number:]!=element[:number]:
            check=False
            break
        current=element
    return check
print(get(2,'ana','naa'))