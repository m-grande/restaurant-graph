from node import Node
from tabulate import tabulate


class Menu:
    def __init__(self):
        self.starters = []
        self.main_dishes = []
        self.beverages = []
        self.desserts = []
        self.menu = []

    def add_starter(self, name, price, description, category):
        starter = Node(name, price, description, category)
        self.starters.append(starter)
        self.menu.append(starter)

    def add_main_dish(self, name, price, description, category):
        main_dish = Node(name, price, description, category)
        self.main_dishes.append(main_dish)
        self.menu.append(main_dish)

    def add_beverage(self, name, price, description, category):
        beverage = Node(name, price, description, category)
        self.beverages.append(beverage)
        self.menu.append(beverage)

    def add_dessert(self, name, price, description, category):
        dessert = Node(name, price, description, category)
        self.desserts.append(dessert)
        self.menu.append(dessert)

    def show_menu(self):
        """Mostra il menu in una tabella unica con una colonna per tipo di piatto, nome, prezzo e descrizione."""
        print("\n======= MENU =======\n")

        menu_data = []

        menu_data.extend(self._format_category(self.starters, "Starter"))
        menu_data.append(["", "", "", ""])

        menu_data.extend(self._format_category(self.main_dishes, "Main Dish"))
        menu_data.append(["", "", "", ""])

        menu_data.extend(self._format_category(self.beverages, "Beverage"))
        menu_data.append(["", "", "", ""])

        menu_data.extend(self._format_category(self.desserts, "Dessert"))

        print(
            tabulate(
                menu_data,
                headers=["Type", "Name", "Price (€)", "Description"],
                tablefmt="fancy_grid",
            )
        )

    def _format_category(self, category, category_name):
        formatted_category = []
        for dish in category:
            formatted_category.append(
                [category_name, dish.name, f"€{dish.price:.2f}", dish.description[:40]]
            )
        return formatted_category

    def find_dish_by_name(self, name):
        for dish in self.menu:
            if dish.name == name:
                return dish
        return None

    def connect_dishes(self, name1, name2):
        dish1 = self.find_dish_by_name(name1)
        dish2 = self.find_dish_by_name(name2)
        if dish1 and dish2:
            dish1.add_edge(dish2)
        else:
            print(f"Error: one of the dishes could not be found  '{name1}' or '{name2}'.")

    def show_suggestions(self, name):
        dish = self.find_dish_by_name(name)
        if dish:
            suggestions = dish.get_edges()
            reverse_suggestions = dish.get_reverse_edges()

            all_suggestions = set(suggestions + reverse_suggestions)

            if all_suggestions:
                suggestion_names = [suggestion.name for suggestion in all_suggestions]
                print(f"With {dish.name} our suggestions are: {', '.join(suggestion_names)}.\n")
            else:
                print(f"No suggestions for {dish.name}.")
        else:
            print(f"'{name}' not found in the menu.")
