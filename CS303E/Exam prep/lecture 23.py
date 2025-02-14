class Automobile:
    
    def __init__(self, make, mileage, price):
        self.__make = make
        self.__mileage = mileage
        self.__price = price
        
    def get_make(self):
        return self.__make
    
    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

class Car(Automobile): # making it the subclass 

    def __init__(self, make, mileage, price, num_doors):
        Automobile.__init__(self, make, mileage, price)  
        self.__num_doors = num_doors
        
class Truck(Automobile):

    def __init__(self, make, mileage, price, bed_length):
        Automobile.__init__(self, make, mileage, price)
        self.__bed_legnth = bed_length

    def get_bed_length(self):
        return self.bed_legnth 
        
def main():
    auto = Automobile('Kia',35000, 2)
    caf = Car('Subaru', 80000, 4, 6)

    print('Auto\'s info:')
    print(auto.get_make())
    print(car.get_make()) 
    
main() 
