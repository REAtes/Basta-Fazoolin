# 19. Since we’ve been so successful building out a branded chain of restaurants, we’ve decided to diversify. We’re going to create a restaurant that sells arepas! First let’s define a Business class.
class Business:
  # 20.Give Business a constructor. A Business needs a name and a list of franchises.
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises


# 12.Basta Fazoolin’ with my Heart has seen tremendous success with the family market, which is fantastic because when you’re at Basta Fazoolin’ with my Heart with family, that’s great! We’ve decided to create more than one restaurant to offer our fantastic menus, services, and ambience around the country.First, let’s create a Franchise class.
class Franchise:

# 13. Give the Franchise class a constructor. Take in an address, and assign it to self.address. Also take in a list of menus and assign it to self.menus.
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

# 15. Give our Franchises a string representation so that we’ll be able to tell them apart. If we print out a Franchise it should tell us the address of the restaurant.
  def __repr__(self):
    return self.address

# 16. Let’s tell our customers what they can order! Give Franchise an .available_menus() method that takes in a time parameter and returns a list of the Menu objects that are available at that time.
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
      else: 
        print("We are closed")
    return available_menus

# 1. At Basta Fazoolin’ with my Heart our motto is simple: when you’re here with family, that’s great! We have four different menus: brunch, early-bird, dinner, and kids.
class Menu:
  # 2. Give Menu a constructor with the five parameters self, name, items, start_time, and end_time.
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.item = items
    self.start_time = start_time
    self.end_time = end_time
  
  # 7. Give our Menu class a string representation method that will tell you the name of the menu. Also, indicate in this representation when the menu is available.
  def __repr__(self):
    return "{name} menu available from {start_time} to {end_time}".format(name=self.name, start_time=self.start_time, end_time=self.end_time)

# 9. Give Menu a method .calculate_bill() that has two parameters: self, and purchased_items, a list of the names of purchased items. 
# Have calculate_bill return the total price of a purchase consisting of all the items in purchased_items.
  def calculate_bill(self, purchased_items):
    total_price = 0
    for purchased_item in purchased_items:
      item_price = self.item[purchased_item]
      total_price += item_price
    return total_price

brunch = Menu("Brunch", {"pancakes": 7.50, "waffles": 9.00, "burger": 11.00, "home fries": 4.50, "coffee": 1.50, "espresso": 3.00, "tea": 1.00, "mimosa": 10.50, "orange juice": 3.50}, 11, 16)
early_bird = Menu("Early Bird", {"salumeria plate": 8.00, "selad and breadsticks (serves 2, no refills)": 14.00, "mushroom ravioli (vegan)": 13.50, "coffee": 1.50, "espresso": 3.00}, 15, 18)
dinner = Menu("Dinner", {"crostini with eggplant caponata": 13.00, "caesar salad": 16.00, "pizza with quattro formaggi": 11.00, "duck ragu": 19.50, "mushroom ravioli (vegan)": 13.50, "coffee": 1.50, "espresso": 3.00}, 17, 23)
kids = Menu("Kids", {"chicken nuggers": 6.50, "fusilli with wild mushrooms": 12.00, "apple juice": 3.00}, 11, 21)

# 8. Try out our string representation. If you call print(brunch) it should print out something like the following:
print(brunch)

# 10.Test out Menu.calculate_bill(). We have a breakfast order for one order of pancakes, one order of home fries, and one coffee. Pass that into brunch.calculate_bill() and print out the price.
print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))

# 11. What about an early-bird purchase? Our last guests ordered the salumeria plate and the vegan mushroom ravioli. Calculate the bill with .calculate_bill().
print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

# 14. Let’s create our first two franchises! Our flagship store is located at "1232 West End Road" and our new installment is located at "12 East Mulberry Street". Pass in all four menus along with these addresses to define flagship_store and new_installment.
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids] )
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

# 15.
print(flagship_store)

# 17
print(flagship_store.available_menus(12))

# 21. Let’s create our first Business. The name is "Basta Fazoolin' with my Heart" and the two franchises are flagship_store and new_installment.
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# 22. Before we create our new business, we’ll need a Franchise and before our Franchise we’ll need a menu. The items for our Take a’ Arepa available from 10am until 8pm are the following:
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take a’ Arepa", arepas_items, 10, 20)

# 23. Next let’s create our first Take a’ Arepa franchise! Our new restaurant is located at "189 Fitzgerald Avenue". Save the Franchise object to a variable called arepas_place.
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# 24. Now let’s make our new Business! The business is called "Take a' Arepa"!
arepas = Business("Take a' Arepa", [arepas_place])






