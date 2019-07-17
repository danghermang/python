def cmmdc(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a

def more_numberz(*args):
    result=args[0]
    for element in args[1:]:
        result=cmmdc(result,element)
    return result

print(more_numberz(32,24,8))
