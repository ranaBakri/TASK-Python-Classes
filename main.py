from operator import truediv

#mony = 0 means the defaoult value = 0
class Wallet:
    def __init__(self, money):
        self.money=money
        

    def credit(self,amount):
        self.money+=amount
        print(f"thank for crdit the {amount} your balance amount now is{self.money}")

    def debit(self,amount):
       self.money-=amount
       print(f"thank you for your operation your current amount is {self.money}")

wallet = Wallet(6)
wallet = Wallet(0)  # This should default money inside the wallet to 0
print(wallet)

wallet.debit(20)
wallet.credit(5)


class Person:
    def __init__(self, name,location,wallet):
        self.name=name
        self.location=location
        self.wallet=Wallet(wallet)

    # def__str__(self):
    #     return f"this person is{self.name} and it has {self.location}and they have {self.wallet} money"
   
    def move_to_point(self,point):
        
        self.location = point
        print(f"the new location for you now is{self.location}")

    


person = Person("Moh", 5, 50)
person.move_to_point(2)

class Vendor(Person):
    range = 5 # because it takes fix values
    price = 1
    def __init__(self, name,location,wallet):
        super().__init__(name,location,wallet)
        

    def sellTo(self,customer, number_of_icecreams):
        coast = number_of_icecreams*self.price
        self.move_to_point(customer.location)
        customer.wallet.debit(coast)
        self.wallet.credit(coast)
        print(f"we sold around {number_of_icecreams} and it coast {coast}   the amount in the vendor wallet now {self.wallet}")




class Customer(Person):
    def __init__(self, name,location,money):
        super().__init__(name,location,money)

    def is_in_range(self,vendor):
        range =abs(vendor.location -self.location)
        print(f"this vendor {vendor.name}  is withen {self.name} range")
        if range<=vendor.range:
            return True
        else:
            return False


    def have_enough_money(self,vendor,number_of_icecreams):
        coast = vendor.price*number_of_icecreams
        if self.wallet.money >= coast:
            return True
        else:
            return False

    def request_icecream(self,vendor, number_of_icecreams):
       if self.is_in_range(vendor) and self.have_enough_money(vendor, number_of_icecreams):
        vendor.sellTo( customer, number_of_icecreams)
        print("give the custmer ice-cream")
       else:
        print("sorry we can't deliver the service")

    

vendor = Vendor("Abdallah",2,10)
customer = Customer("Abdallah", 3,6)
# /print(customer.is_in_range(2))
# print(customer.have_enough_money(vendor,3))
customer.request_icecream(vendor,5)
  
 