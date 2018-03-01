from math import fabs
import sys
import michal
import fileinput

class Taxi:
    c =0 #x
    r =0 #y
    chosen =0 #chosen passenger
    pos = 0 #position of current ride in array of passengers
    close = sys.maxint #distance to closest destination
    money =0 #points earned
    rides=[] #array of ride ids

    def check(self, orderM): #selects the closest passenger
        for i in range(len(orderM.orders)):
            r2 = orderM.orders[i].A[0] #x ride start
            c2 = orderM.orders[i].A[1] #y ride start
            if (fabs(c2-self.c) + fabs(r2-self.r)) < self.close:
                self.close = (fabs(c2-self.c) + fabs(r2-self.r))
                self.chosen = orderM.orders[i].id
                self.pos = i

    def go(self, orderM): #go to chosen passenger and ride
        self.c = orderM.orders[self.pos].B[1]
        self.r = orderM.orders[self.pos].B[0]
        c2 = orderM.orders[self.pos].A[1]
        r2 = orderM.orders[self.pos].A[0]
        self.money = (fabs(c2-self.c) + fabs(r2-self.r))
        self.rides.append(self.chosen)
        del orderM.orders[self.pos]


def write_answer(array, filename):
    with open(filename) as file:
        for taxi in array:
            file.write(len(taxi.rides) + ' ' + ' '.join(taxi.rides))

def main():
    taxis = []
    input = fileinput.input("a_example.in")
    tablica = input[0].split(" ")
    tablica = tablica[0:-1]
    #print(tablica)
    orderManager = michal.OrderManager()
    orderManager.loadFromFile("a_example.in")
    #orderManager.printInfo()
    for i in range (tablica[2]):
        taxi = Taxi()
        taxis.append(taxi)

    #do_stuff

    write_answer(taxis, "output.txt")

if __name__ == '__main__':
    main()