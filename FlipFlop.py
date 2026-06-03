def palind(r): 
    e = len(r) -1
    s = 0
    while(s<e): 
        if(r[e]!=r[s]): 
            return False
        s+=1
        e-=1
    return True
r = (7, 9, 4, 8, 5, 3)

if (palind(r)): 
    print("The tuple is a flop")
else: 
    print("The tuple is not a flop")