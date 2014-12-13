from queue import Queue 

def hotPotato(namelist, num):
    """
    Simulates a game of hot potato (like musical chairs). 'num' is the number of enqueues before a name is removed before the list. Proceeds until there is only one name left (which is returned).
    """

    q = Queue()

    for name in namelist:
        q.enqueue(name)

    while q.size() > 1:

        for i in range(num):
            person = q.dequeue()
            q.enqueue(q.dequeue())

    winner = q.dequeue()

    return winner



if __name__ == '__main__':
    namelist = ["Wendy", "Benoit", "Jessica", "Linda", "Tammy", "Penelope"]
    num = 5
    print hotPotato(namelist, num)