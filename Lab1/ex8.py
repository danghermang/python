def get(sir,valoare):
    lista=list()
    i=0
    while i<len(sir):
        if i=='-':
            lista.append(-int(sir[i+1]))
            i+=1
        else:
            lista.append(int(sir[i]))
        i+=6
    return lista
-