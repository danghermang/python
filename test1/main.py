import os
def problema2():
    suma=0
    for i in range(10):
        suma+=i
    return suma
def problema3(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
def problema4(m):
    lista=[]
    for i in range(m):
        if problema3(i):
            lista.append(i)
    return lista
def problema5(my_list):
    result=[]
    for element in my_list:
        if isinstance(element,int):
            result.append(element)
    return sorted(result,reverse=True)

def problema6(folder,fisier):
    f=open(fisier,"w")
    for element in os.listdir(folder):
        if os.path.isfile(os.path.join(folder,element)) and element.startswith('A'):
            f.write(os.path.join(folder,element))
    f.close()

def problema7(director,depth):
    lista = []
    if depth==0:
        count=0
        for element in os.listdir(director):
            if os.path.isfile(os.path.join(director, element)):
                count+=1
            if count==3:
                lista.append(director)
                return lista
    else:
        count = 0
        for element in os.listdir(director):
            if os.path.isfile(os.path.join(director, element)):
                count+=1
            elif os.path.isdir(os.path.join(director, element)):
                lista.extend(problema7(os.path.join(director, element), depth-1))
            if count==3:
                lista.append(director)
    return lista

print(problema7("D:/Facultate/an 3 sem 1/Python",1))
if __name__ == "__main__":
    print("Cel mai simplu test")