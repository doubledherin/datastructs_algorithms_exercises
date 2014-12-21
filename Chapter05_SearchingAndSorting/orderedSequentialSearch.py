def orderedSequentialSearch(alist, item):
    pos = 0 
    found = False
    tooFar = False

    while pos < len(alist) and not found and not tooFar:
        if alist[pos] == item:
            found = True
        elif alist[pos] > item:
            tooFar = True
        else:
            pos += 1
    return found

if __name__ == '__main__':
    print orderedSequentialSearch([1,2,90,114,115], 6)
    print orderedSequentialSearch([1,2,90,114,115], 114)

