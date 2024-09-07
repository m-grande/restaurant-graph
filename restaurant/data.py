from menu import Menu

restaurant_menu = Menu()

restaurant_menu.add_starter(
    "Bruschetta", 5.00, "Toasted bread with tomatoes and basil", "vegetarian"
)
restaurant_menu.add_starter(
    "Caprese Salad", 6.00, "Buffalo mozzarella with tomatoes and basil", "vegetarian"
)
restaurant_menu.add_starter("Crostini", 4.50, "Crostini with liver pâté", "spicy")

restaurant_menu.add_main_dish(
    "Margherita Pizza", 8.50, "Pizza with tomato, mozzarella, and basil", "vegetarian"
)
restaurant_menu.add_main_dish("Lasagna", 9.50, "Lasagna with meat sauce", "meat")
restaurant_menu.add_main_dish(
    "Mushroom Risotto", 9.00, "Risotto with porcini mushrooms", "vegetarian"
)

restaurant_menu.add_beverage("Water", 2.00, "Still water", "vegan")
restaurant_menu.add_beverage("Red Wine", 5.00, "Glass of red wine", "vegetarian")
restaurant_menu.add_beverage("Craft Beer", 4.00, "Craft beer", "vegan")

restaurant_menu.add_dessert(
    "Tiramisu", 4.50, "Coffee-flavored dessert with mascarpone", "vegetarian"
)
restaurant_menu.add_dessert("Panna Cotta", 4.00, "Cream dessert with berry sauce", "vegetarian")
restaurant_menu.add_dessert("Gelato", 3.50, "Artisanal ice cream", "vegetarian")

# Connetti i piatti
restaurant_menu.connect_dishes("Bruschetta", "Margherita Pizza")
restaurant_menu.connect_dishes("Caprese Salad", "Lasagna")
restaurant_menu.connect_dishes("Crostini", "Mushroom Risotto")

restaurant_menu.connect_dishes("Margherita Pizza", "Water")
restaurant_menu.connect_dishes("Lasagna", "Craft Beer")
restaurant_menu.connect_dishes("Mushroom Risotto", "Red Wine")

restaurant_menu.connect_dishes("Water", "Tiramisu")
restaurant_menu.connect_dishes("Craft Beer", "Panna Cotta")
restaurant_menu.connect_dishes("Red Wine", "Gelato")
