from math import fabs
import sys
import michal
import fileinput

time_limit = 0
on_time_bonus = 0


class Taxi:
    c = 0  # x
    r = 0  # y
    chosen = 0  # chosen passenger
    pos = 0  # position of current ride in array of passengers
    close = sys.maxint  # distance to closest destination
    money = 0  # points earned

    rides = []  # array of ride ids

    time = 0  # current time unit
    chosen = False #checks if taxi has chosen a passenger

    def check(self, orderM):  # selects the closest passenger
        for i in range(len(orderM.orders)):
            p = orderM.orders[i]  # passenger being checked
            r2 = p.A[0]  # x ride start
            c2 = p.A[1]  # y ride start
            distance = (fabs(c2 - self.c) + fabs(r2 - self.r))
            ride_length = (fabs(c2 - p.B[1]) + fabs(r2 - p.B[0]))
            if (distance < self.close) and max(self.time + distance, p.start) + ride_length < time_limit:
            #if the ride is closer to the taxi than the previous one and the ride won't exceed the time limit
                self.close = (fabs(c2 - self.c) + fabs(r2 - self.r))
                self.chosen = p.id
                self.pos = i
                self.chosen = True

    def go(self, orderM):  # go to chosen passenger and ride
        p = orderM.orders[self.pos]
        self.c = p.B[1]
        self.r = p.B[0]
        c2 = p.A[1]
        r2 = p.A[0]
        distance = (fabs(c2 - self.c) + fabs(r2 - self.r))
        ride_length = (fabs(c2 - p.B[1]) + fabs(r2 - p.B[0]))

        self.money = (fabs(c2 - self.c) + fabs(r2 - self.r))
        self.time = max(self.time + distance, p.start) + ride_length
        if self.time <= p.end:
            self.money += on_time_bonus

        self.rides.append(self.chosen)
        del orderM.orders[self.pos]
        self.chosen = False


def taxi_loop(taxis):
    taxi_rides_done = True #checks if any taxi has taken a passenger
    while taxi_rides_done:
        taxi_rides_done = False
        for taxi in taxis:
            taxi.check
            if taxi.chosen:
                taxi.go
                taxi_rides_done = True



def write_answer(array, filename):

    with open(filename) as file:
        for taxi in array:
            file.write(len(taxi.rides) + ' ' + ' '.join(taxi.rides))


def main():
    taxis = []
    orderManager = michal.OrderManager()
    orderManager.loadFromFile("a_example.in")
    orderManager.printInfo()

    input = fileinput.input("a_example.in")
    tablica = input[0].split(" ")
    tablica = tablica[0:-1]
    #print(tablica)
    orderManager = michal.OrderManager()
    orderManager.loadFromFile("a_example.in")
    time_limit = tablica[5]
    on_time_bonus = tablica[4]
    #orderManager.printInfo()
    for i in range (tablica[2]):
        taxi = Taxi()
        taxis.append(taxi)

    taxi_loop(taxis)

    write_answer(taxis, "output.txt")

if __name__ == '__main__':
    main()
