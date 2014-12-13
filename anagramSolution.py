def anagramSolution1(s1, s2):
    """
    Takes two strings and returns True if they are anagrams; False if not.
    
    Assumes strings are of equal length and contain lowercase ascii letters.
    """

    listy = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(listy) and stillOK:
        pos2 = 0
        found = False

        while pos2 < len(listy) and not found:
            if s1[pos1] == listy[pos2]:
                found = True
            else: pos2 = pos2 + 1

        if found:
            listy[pos2] = None

        else:

            stillOK = False
        pos1 += 1

    return stillOK