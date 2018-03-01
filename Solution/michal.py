import fileinput
import copy

class Order:
    id = 0
    A=[]
    B=[]
    start = 0
    end = 0
    def __init__(self, inId, inA, inB, inStart, inEnd):
        self.A = inA
        self.B = inB
        self.start = inStart
        self.end = inEnd
        self.id = inId
    def printInfo(self):
        print(self.id, self.A, self.B, self.start, self.end)


class OrderManager:
    orders = []
    def loadFromFile(self, path):
        input = fileinput.input(path)
        i=0
        for line in input:
            Ax,Ay,Bx,By,start,end=line.split(" ")
            order = Order(i, [Ax, Ay], [Bx, By], start, end)
            self.orders.append( order )
            i += 1
    def printInfo(self):
        for order in self.orders:
            print(order.printInfo())


orderManager = OrderManager()
orderManager.loadFromFile("a_example.in")
orderManager.printInfo()


