from ShoppingBag import *

def main():

    # Define items in order by paper so Mass, NH, Then Maine
    items = [("Clothing", 75, "Massachusetts", "clothing"),
             ("Everything Else", 400, "New Hampshire", "everything else"),
             ("Food", 20, "Maine", "Wic Eligible foods")]

    bag = ShoppingBag(items)
    bag.calculate_total()

if __name__ == '__main__':
    main()