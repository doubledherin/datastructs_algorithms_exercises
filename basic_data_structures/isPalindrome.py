from deque import Deque 

def isPalindrome(s):

    d = Deque()

    for char in s:
        d.addFront(char)

    while d.size() > 1:
        item1 = d.removeFront()
        item2 = d.removeRear()
        if item1 != item2:
            return False

    return True


if __name__ == '__main__':
    print isPalindrome("radar")
    print isPalindrome("hannah")
    print isPalindrome("boat")