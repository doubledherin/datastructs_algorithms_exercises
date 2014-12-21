def binarySearch(alist, item):
    start = 0
    stop = len(alist)-1
    found = False

    while start <= stop and not found:
        mid = (start+stop)//2
        if alist[mid] == item:
            found = True
        else:
            if item < alist[mid]:
                stop = mid-1
            else:
                start = mid+1
    return found

if __name__ == '__main__':
    print binarySearch([1,2,90,114,115], 6)
    print binarySearch([1,2,90,114,115], 114)