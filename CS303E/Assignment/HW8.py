# File: HW8.py
# Author: Yingchen (Angela) Liu
# UT EID: yl42556
# Course: CS 303E
#
# Program containes a text-based role-playing game that allows user to create
# their hero and encounter events and battle with enemies

class Character:
    """
    Creates a character with inputed name and health level

    Attributes
    ----------
    name : str
        Name of the character
    health : int
        Health value of the character 
    """
    
    def __init__(self, name, health):
        """
        Initializes a Character object with its name and health value

        Parameters
        ----------
        name : str
            Inputted name to name the character being created
        health : int
            Health value of the character represented as int 
        """
        self.name = name
        self.health = health
        
    def take_damage(self, amount_damage):
        """
        Reduce the character's health value by the amount of damage it received 

        Parameter
        ---------
        amount_damage : int
            Amount of damage that character recevied
            
        Return
        ------
        health : int
            Adjusted Character object's health value 
        """
        self.health -= amount_damage
        return self.health

    def __str__(self):
        """
        Return string representation of attribute 'name' and 'health'

        Return
        ------
        str
            String representation of character's name and current health value 
        """
        return f"{self.name} (health={self.health})"
        
class Hero(Character):
    """
    Creates a Hero object as a subclass object of Character object

    Attributes
    ----------
    name : str
        Name of the new created Hero object 
    health : int
        Health values of the new created Hero object
    """
    
    def __init__(self, name, health):
        """
        Initializes a Hero object with provided name and health value

        Parameters
        ----------
        name : str
            Name of the hero character
        health : int
            Health value of the hero character 
        """
        Character.__init__(self, name, health)
        self.__inventory = []
        
    def restore_health(self, amount_restore):
        """
        Regain the hero character's health point with the amount that the
        founded exilier provided

        Parameter
        ---------
        amount_restore : int
            Amount of health point that exilier can restore

        Return
        ------
        health : int
            New health value after character restore health 
        """
        self.health += amount_restore
        return self.health

    def add_inventory(self, item):
        """
        Add items that character found to its inventory

        Parameter
        ---------
        item : str
            Found objects 
        """
        self.__inventory.append(item)

    def remove_inventory(self, item):
        """
        Remove found item from character's inventory

        Parameter
        ---------
        item : str
            Found objects 
        """
        self.__inventory.remove(item)

    def get_inventory(self):
        """
        Return inventory that recorded all found items
        """
        return self.__inventory 

class Enemy(Character):
    """
    Subclass of Character object along with amount of damage enemy can produce
    
    Attributes
    ----------
    name : str
        Name of the enemy
    health : int
        Health value of the enemy
    amount_damage : int
        Amount of damage that enemy produce 
    """
    
    def __init__(self, name, health, amount_damage):
        """
        Initializes Enemy object with the provided name, health, and amount of
        damage they produce

        Parameters
        ----------
        name : str
            Name of the created Enemy object
        health : int
            Health value of the created Enemy object
        amount_damage : int
            Amout of damage that Enemy object produce
        """
        Character.__init__(self, name, health)
        self.damage = amount_damage

def main():
    han = Hero("Han", 40)
    zombie = Enemy("Zombie", 20, 15)
    werewolf = Enemy("Werewolf", 15, 10)
    print(f"Start:\n{han}\n{zombie}\n{werewolf}")
    # battle 1
    han.take_damage(werewolf.damage)
    werewolf.take_damage(10)
    print(f"Battle 1:\n{han}\n{werewolf}")
    # battle 2
    han.take_damage(zombie.damage)
    zombie.take_damage(20)
    print(f"Battle 2:\n{han}\n{zombie}")
    # restore health
    han.restore_health(5)
    print(f"Restore Health:\n{han}")
    # find an item
    han.add_inventory("gold coin")
    han.add_inventory("candle")
    print(f"Inventory:\n{han.get_inventory()}")

if __name__ == "__main__":
    main()
    
