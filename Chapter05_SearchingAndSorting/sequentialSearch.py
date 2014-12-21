def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found

if __name__ == '__main__':
    print sequentialSearch([1,2,90,114,115], 6)
    print sequentialSearch([1,2,90,114,115], 114)