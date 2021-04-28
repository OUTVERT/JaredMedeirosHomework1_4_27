class ShoppingBag:
    def __init__(self, items):
        self.items = items
        self.taxes = {
            "Massachusetts": 6.25,  # 6.25%
            "New Hampshire": 0,  # 0%
            "Maine": 5.5  # 5.5%
        }

    def __calculate_subtotal(self, item): # private method to calculate submethod of one item
        name = item[0]
        price = item[1]
        state = item[2]
        item_type = item[3]

        if state in self.taxes:
            return price*(1 + self.taxes[state]/100.0)
        else:
            return price

    def calculate_total(self):
        total = 0
        # Loop through items
        for item in self.items:
            name = item[0]
            price = item[1]
            state = item[2]
            item_type = item[3]
            print("Scanning item:", name)
            print("price: {0:.1f}".format(price))
            print("type: ", item_type)
            print("item after tax: {0:.1f}".format(self.__calculate_subtotal(item)))
            total += self.__calculate_subtotal(item)

        print("your checkout price including tax: {:.2f}".format(total))
