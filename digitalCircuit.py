class LogicGate:

    def __init__(self,n):
        self.label = n
        self.output = None

    def __str__(self):
        return str(self.label)

    def getLabel(self):
        return str(self.label)

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):

        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):

        if self.pinA == None:
            return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))

class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        if self.pinB == None:
            self.pinA = source
        else:
            raise RuntimeError("Error: At least 1 pin must be empty.")

class OrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a==1 or b==1:
            return 1

        else:
            return 0

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        if self.pinB == None:
            self.pinA = source
        else:
            raise RuntimeError("Error: At least 1 pin must be empty.")

class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n)
      

    def performGateLogic(self):

        a = self.getPin()
        
        if a==1:
            return 0
        else:
            return 1

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: At least 1 pin must be empty.")

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate






if __name__ == "__main__":
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    c3 = Connector(g3,g4)
    print g4.getOutput()
