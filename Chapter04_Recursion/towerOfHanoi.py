def moveTower(height, fromPole, toPole, withPole):

    if height >= 1:
        
        moveTower(height-1, fromPole, withPole, toPole)
        
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)

def moveDisk(fromPole, toPole):
    print "Moving disk from %s to %s\n" % (fromPole, toPole)


if __name__ == '__main__':
    print moveTower(10, "Pole A", "Pole C", "Pole B")
