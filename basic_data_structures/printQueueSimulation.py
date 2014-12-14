from queue import Queue 
import random

class Printer:

    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def countdown(self):
        if self.currentTask:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def isBusy(self):
        return self.currentTask != None

    def startNextTask(self, newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() * (60 / self.pagerate)

class Task:

    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def getTimeWaited(self, currentTime):
        return currentTime - self.timestamp


def simulation(seconds, ppm):

    printer = Printer(ppm)
    q = Queue()
    waittimes = []

    for currentSecond in range(seconds):

        if newPrintTask():
            task = Task(currentSecond)
            q.enqueue(task)

        if (not printer.isBusy()) and (not q.isEmpty()):
            nextTask = q.dequeue()
            waittimes.append(nextTask.getTimeWaited(currentSecond))

            printer.startNextTask(nextTask)


        printer.countdown()

    averageWait = sum(waittimes)/len(waittimes)

    print "Average wait of %6.2f seconds; %3d tasks remaining." \
            % (averageWait, q.size())
    return



def newPrintTask():
    """
    Print tasks are generated on average every 180 seconds. This simulates that.
    """
    num = random.randrange(181)
    if num == 180:
        return True
    else:
        return False


if __name__ == '__main__':
    for i in range(100):
        simulation(3600, 10)
