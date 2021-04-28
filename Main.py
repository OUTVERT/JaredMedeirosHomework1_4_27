from ShoppingBag import *

def main():

    # Define items
    items = [("Pants", 75, "Massachusetts", "clothing"),
             ("Car Bill", 400, "Maine", "everything else"),
             ("Steak", 20, "New Hampshire", "food")]

    bag = ShoppingBag(items)
    bag.calculate_total()

if __name__ == '__main__':
    main()