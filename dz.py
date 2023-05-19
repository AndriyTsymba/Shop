class Clothing:
    def __init__(self, material, name, price, size):
        self.material = material
        self.name = name
        self.price = price
        self.size = size
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.inventory = []
    def add_item(self, item):
        self.inventory.append(item)
    def remove_item(self, item):
        self.inventory.remove(item)
    def get_items(self):
        return self.inventory
    def search_items(self, keyword):
        return [item for item in self.inventory if keyword.lower() in item.name.lower()]
class Customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.cart = []
    def add_to_cart(self, item):
        if item.price <= self.budget:
            self.cart.append(item)
            self.budget -= item.price
            print(f"{item.name} added to the cart.")
        else:
            print(f"Not enough budget to add {item.name} to the cart.")

    def remove_from_cart(self, item):
        if item in self.cart:
            self.cart.remove(item)
            self.budget += item.price
            print(f"{item.name} removed from the cart.")
        else:
            print(f"{item.name} is not in the cart.")

    def view_cart(self):
        if self.cart:
            print("Items in the cart:")
            for item in self.cart:
                print(f"- {item.name}: ${item.price}")
        else:
            print("The cart is empty.")

    def checkout(self):
        total_cost = sum(item.price for item in self.cart)
        if total_cost <= self.budget:
            self.budget -= total_cost
            print(f"Purchase successful. Total cost: ${total_cost}")
            self.cart = []
        else:
            print("Insufficient budget to complete the purchase.")
store = Store("LOUSI VUTTION", "Chechatik 1001")
item1 = Clothing("Cotton", "T-Shirt", 200, "M")
item2 = Clothing("Denim", "Jeans", 120, "L")
item3 = Clothing("Wool", "Sweater", 250, "S")
store.add_item(item1)
store.add_item(item2)
store.add_item(item3)
customer = Customer("Kostiy", 1000)
keyword = "t-shirt,"
search_results = store.search_items(keyword)
if search_results:
    customer.add_to_cart(search_results[0])
else:
    print(f"No items found with the keyword '{keyword}'.")
customer.view_cart()
customer.remove_from_cart(item1)
customer.view_cart()
customer.checkout()
