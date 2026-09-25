fibodict={0:0,1:1}
def fibonnaci(a: int) -> int:
    if not isinstance(a, int) or a<0:
        raise ValueError("fibonnaci, the function that calculate the value of fibonnaci of an integer, expect a positive integer")
    if a in fibodict:
        return fibodict[a]
    else:
        newresult= fibonnaci(a-2)+fibonnaci(a-1)
        fibodict[a]= newresult
        return newresult

