def binarySearchRecursive(alist, item):
    # base case
    if len(alist) == 0:
        return False
    else:
        mid = len(alist)//2
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                return binarySearchRecursive(alist[:mid], item)
            else:
                return binarySearchRecursive(alist[mid+1:], item)



if __name__ == '__main__':
    print binarySearchRecursive([1,2,90,114,115], 6)
    print binarySearchRecursive([1,2,90,114,115], 114)