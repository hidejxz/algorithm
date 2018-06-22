def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first+last)//2
        if alist[midpoint] == item:
            found = True
        elif item < alist[midpoint]:
            last = midpoint - 1
        else: 
            first = midpoint + 1
    return found

def binary_search(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            return binary_search(alist[:midpoint], item)
        else: 
            return binary_search(alist[midpoint+1:], item)