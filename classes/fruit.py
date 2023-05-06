class Fruit:
    category="Fruit"
    def __init__(self,name,quantity,price):
        self.name=name
        self.quantity=quantity
        self.price = price
    def get_by_name(self):
        return f"This is {self.name}"
    def find_by_quantity(self):
        return f"The {self.name} color is  {self.weight}"
    def find_by_price(self):
        
        return f" the price is{self.price}"
      