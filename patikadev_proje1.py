def flatten(A):
    F=[]
    for i in A:
        if type(i) == list:
            for x in i:
                if type(x) == list:
                    for y in x:
                        if type(y) == list:
                            for z in y:
                                F.append(z)
                        else:
                            F.append(y)
                else:
                    F.append(x)
        else:
            F.append(i)
    return F



A=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(A))