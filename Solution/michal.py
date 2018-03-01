import fileinput

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
    premia = 0
    firstInfoRow = []
    def loadFromFile(self, path):
        input = fileinput.input(path)
        i=0
        for line in input:
            if i==0:
                self.firstInfoRow = line.split(" ")
                self.firstInfoRow[-1] = self.firstInfoRow[-1][0:-1]
                for a in range( len(self.firstInfoRow) ):
                    self.firstInfoRow[a] = int(self.firstInfoRow[a])
            else:
                Ax,Ay,Bx,By,start,end=line.split(" ")
                order = Order(i-1, [int(Ax), int(Ay)], [int(Bx), int(By)], int(start), int(end))
                self.orders.append( order )
            i += 1

    def printInfo(self):
        print("Nagłówek: ", self.firstInfoRow)
        for order in self.orders:
            order.printInfo()

"""orderManager = OrderManager()
orderManager.loadFromFile("a_example.in")
orderManager.printInfo()

"""
orderManager = OrderManager()
orderManager.loadFromFile("a_example.in")
orderManager.printInfo()
