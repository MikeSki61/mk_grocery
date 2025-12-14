class CoffeeOrder:

    total_orders = 0

    def __init__(self):
        self.orders = []
        CoffeeOrder.total_orders +=1
    
    def add_order(self, drink):
        self.orders.append(drink)
        print(f"{drink} added to your order.")

    def cancel_order(self, drink):
        if drink in self.orders:
            self.orders.remove(drink)
            print(f"{drink} removed from your order.")
        else:
            print(f"{drink} not found in your order.")

    def show_order(self):
        print("Your order: ", ", ".join(self.orders))

    def clear_orders(self):
        """Clears the entire order list."""
        self.orders = []
        print("Your order has been cleared.")


    @classmethod

    def get_total_orders(cls):
        return cls.total_orders

    def add_orders(self, drink):
        self.order.append(drink)

    def cancel_order(self, drink):
        if drink in self.orders:
            self.orders.remove(drink)
            print(f"{drink} has been removed")
        else:
         print(f"{drink} was not found in you order")

    def show_order(self):
        """Displays all drinks in the order."""
        print("Your Order:" , ", ".join(self.orders))

    @staticmethod
    def is_valid_drink(drink):
        """Checks if a drink name is valid."""
        return isinstance(drink, str) and bool(drink.strip())


my_order = CoffeeOrder()
my_order.add_order("Latte")
my_order.add_order("Espresso")
my_order.show_order()
my_order.cancel_order("Latte")
my_order.show_order()

print(CoffeeOrder.is_valid_drink("Capuccino"))
print(CoffeeOrder.is_valid_drink(""))

#Getters, Setters and Decorators




 






