import random

price = 10
weight = 20
flammability = 0.5

class Product():
    def __init__(self, name, price, weight,flammability, identifier):
        # these are attributes / nouns
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000,10000000)
    def Productinfo(self):
        print("Pro Info",self.name,self.price,self.identifier,self.flammability)  
    def stealability(self):
        self.price = (price / weight)
        print("stealability",self.price)
    def explode(self):
        self.blow = flammability * weight  
if __name__ == "__main__":
    # test for values
    prod = Product("Bananas", 10, 20, 0.5, random.randint(1000000,10000000))
    print(prod.price)
    prod.Productinfo()   
    print(prod.weight)
    prod.stealability()
    