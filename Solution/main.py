from math import fabs
import sys

class Taxi:
    c =0
    r =0
    chosen =0
    pos = 0
    close = sys.maxint
    money =0
    rides=[]

    def sprawdz(self, orderM):
        for i in range(len(orderM.orders)):
            r2 = orderM.orders[i].A[0]
            c2 = orderM.orders[i].A[1]
            if (fabs(c2-self.c) + fabs(r2-self.r))<self.close:
                self.close = (fabs(c2-self.c) + fabs(r2-self.r))
                self.chosen = orderM.orders[i].id
                self.pos = i


    def go(self, orderM):
        self.c = orderM.orders[self.pos].B[1]
        self.r = orderM.orders[self.pos].B[0]
        c2 = orderM.orders[self.pos].A[1]
        r2 = orderM.orders[self.pos].A[0]
        self.money = (fabs(c2-self.c) + fabs(r2-self.r))
        self.rides.append(self.chosen)
        del orderM.orders[self.pos]



