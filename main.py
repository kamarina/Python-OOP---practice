from item import Item
from phone import Phone

item1 = Phone("iPhone12", 1000, 3)

item1.apply_increment(0.2)
print(item1.price)

