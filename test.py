def once(inputs):
    lens = len(inputs)
    i = 0
    cand = []
    while i<lens:
        cand.append(inputs[i:i+3])
        i+=3
    s = 0
    print(cand)
    for c in cand:
        try:
            k = c[1]-c[0]
        except:
            k=0
        s+=k
    print(s)
    return s

def inout(inputs):
    lens = len(inputs)
    i = 0
    m = 0
    while i<lens and (lens-i)>3:
        s = once(inputs[i:])
        if m<s:
            m=s
        i+=1
    return m
    
inout([3,4,5,1,3])
