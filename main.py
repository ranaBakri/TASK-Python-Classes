from operator import truediv


class Wallet:
    def __init__(self, money):
        self.money=money
        

    def credit(self,amount):
        credit=0
        credit+=amount
        print(f"thank for crdit the {amount} your balance amount now is{credit}")

    def debit(self,amount):
        debit=0
        debit=abs(debit-amount)
        print(f"thank you for your operation your current amount is {debit}")

wallet = Wallet(6)
wallet = Wallet(0)  # This should default money inside the wallet to 0
print(wallet)

wallet.debit(20)
wallet.credit(5)


class Person:
    def __init__(self, name,location,wallet):
        self.name=name
        self.location=location
        self.wallet=Wallet(100)
    
    def move_to_point(self,point):
        
        self.location =self.location + point
        print(f"the new location for you now is{self.location}")

    


person = Person("Moh", 5, 50)
person.move_to_point(2)

class Vendor(Person):
    def __init__(self, name,location,wallet,range,price):
        super().__init__(name,location,wallet)
        self.range = 5
        self.price = 1

    def sellTo(self,customer, number_of_icecreams):
        super() .move_to_point(customer)
        coast=int(self.price*number_of_icecreams)
        Vendor.wallet=int(abs((wallet.money-(coast))))
        print(f"we sold around {number_of_icecreams} and it coast {coast}   the amount in the vendor wallet now {Vendor.wallet}")

vendor = Vendor("Abdallah",2,10,5,1)

vendor.sellTo(7,3)

class Customer(Person):
    def __init__(self, name,location,wallet):
        super().__init__(name,location,wallet)

    def is_in_range(self,vendor):
        range =abs(vendor-self.location)
        if range<=vendor:
            return True
        else:
            return False


    def have_enough_money(vendor,number_of_icecreams):
        if vendor >= number_of_icecreams:
            return True
        else:
            return False

    def request_icecream(vendor, number_of_icecreams):
       if  is_in_range(vendor) and have_enough_money(vendor, number_of_icecreams):
           print("give the custmer ice-cream")
       else:
            print("sorry we can't deliver the service")

    

customer = Customer("Abdallah", 3,6)
# /print(customer.is_in_range(2))
print(customer.have_enough_money(2,3))
  
 