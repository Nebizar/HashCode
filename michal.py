import fileinput
import copy

class Order:
    id = 0
    A=[]
    B=[]
    start = []
    end = []
    def __init__(self, inId, inA, inB, inStart, inEnd):
        A = copy.deepcopy(inA)
        B = copy.deepcopy(inB)
        start = copy.deepcopy(inStart)
        end = copy.deepcopy(inEnd)
        id = copy.deepcopy(inId)
    def printInfo(self):
        print(self.id, self.A, self.B, self.start, self.end)


class OrderManager:
    orders = []
    def loadFromFile(self, path):
        input = fileinput.input(path)
        i=0
        for line in input:
            Ax,Ay,Bx,By,start,end=line.split(" ")
            tempObject = Order(i,[Ax, Ay], [Bx, By], start, end)
            self.orders.append( tempObject )
            i += 1
    def printInfo(self):
        for order in self.orders:
            print(order.printInfo())


orderManager = OrderManager()
orderManager.loadFromFile("a_example.in")
orderManager.printInfo()


