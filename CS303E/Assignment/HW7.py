# File: HW7.py 
# Author: Yingchen(Angela) Liu
# UT EID: yl42556
# Course: CS 303E
#
# This program contains two classes. ShoppingCart designated to keep track of
# items a student customer is purchasing. ItemToPurchase contained information
# associated with each item and better assist for calculating the total amount
# of prices and quantity. 

class ItemToPurchase:
    """
    Creates an object to track selected item's price and quantity 

    Attributes
    ----------
    name : str
        Name of the item
    price : float
        Price of the item
    quantity : int
        Amount of the item that the student is purchasing
    """
    
    def __init__(self, name, price, quantity):
        """
        Initializes a ItemToPurchase object with item'name, price, and quantity

        Parameters
        ----------
        name: str
            Item's name
        price : float
            Monetary amount of the item 
        quantity: int
            Amount of the item that the student is purchasing
        """
        self.name = name
        self.price = float(price)
        self.__quantity = int(quantity)
        
    def get_quantity(self):
        """
        Returns the quantity of selcted item(s)

        Return
        ------
        self.__quantity : int
            Amount of the item that the student is purchasing 
        """
        return self.__quantity
    
    def set_quantity(self, quantity):
        """
        Resetting the quantity of item student is purchasing
        """
        self.__quantity = quantity 
    
    def __str__(self):
        """
        Returns a string representation of the ItemToPurchase object

        Returns
        -------
        str
            String display of the item with its price and quantity
        """
        total_price = self.price * self.__quantity
        return f"{self.name}: {self.__quantity} @ ${self.price:.2f} = " + \
               f"${total_price:.2f}"
    
class ShoppingCart:
    """
    A listing of items that student customer is purchasing 

    Attributes
    ----------
    customer_ID : int
        Student's ID number
    cart_items : list
        List of items that student customer is acquring 
    """
    
    def __init__(self, customer_ID):
        """
        Initializeings a ShoppingCart object with item(s) student is purchasing 

        Attributes
        ----------
        customer_ID: str
            Student's ID number
        cart_items : list
            A list of items that indvidual student is acquring 
        """
        self.customer_ID = customer_ID
        self.cart_items = list()
        
    def add_item(self, item):
        """
        Adding item to the shopping list

        Parameter
        ---------
        item : ItemToPurchase object 
            An ItemToPurchase object representing what customer is purchasing 
        """
        self.cart_items.append(item)
        
    def remove_item(self, item):
        """
        Removing specific item from shopping list

        Parameter
        ---------
        item : ItemToPurchase object
            An ItemToPurchase object of what customer wants to remove
        """
        self.cart_items.remove(item) 

    def change_quantity(self, item_name, new_quantity):
        """
        Change specific item's quanity in student's shopping cart

        Parameters
        ----------
        item_name : str
            Name of the item 
        new_quantity : int
            New amount of item customer is purchasing 
        """
        for item in self.cart_items:
            if item_name == item.name:
                item.set_quantity(new_quantity)

    def print_cart(self):
        """
        Printing out all items in the student's shopping cart 
        """
        print(f"Shopping Cart for Customer: {self.customer_ID}")
        total = 0 
        for i in self.cart_items:
            print(i)
            total += i.get_quantity() * i.price
        print(f"TOTAL: ${total:.2f}")
        
def main():
    potato_chips = ItemToPurchase("Potato Chips", 3.49, 1)
    potato_chips.set_quantity(2) 
    soda = ItemToPurchase("Soda", 1.50, 1)
    #print(f"{potato_chips}\n{soda}")
    
    shopping_cart = ShoppingCart(987654)
    shopping_cart.add_item(potato_chips)
    shopping_cart.add_item(soda)
    shopping_cart.print_cart()
    print()
    shopping_cart.remove_item(potato_chips)
    shopping_cart.print_cart()
    print()
    shopping_cart.change_quantity("Soda", 3)
    shopping_cart.print_cart()

if __name__ == "__main__":
    main() 
        
    
