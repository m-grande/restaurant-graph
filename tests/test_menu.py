import pytest
from restaurant.menu import Menu


def test_menu_creation():
    menu = Menu()
    assert menu.starters == [], "The starters list should be empty initially."
    assert menu.main_dishes == [], "The main dishes list should be empty initially."
    assert menu.beverages == [], "The beverages list should be empty initially."
    assert menu.desserts == [], "The desserts list should be empty initially."
    assert menu.menu == [], "The overall menu list should be empty initially."


def test_add_starter():
    menu = Menu()
    menu.add_starter("Bruschetta", 5.00, "Toasted bread with tomatoes", "vegetarian")
    assert len(menu.starters) == 1, "There should be 1 starter in the menu"
    assert menu.starters[0].name == "Bruschetta", "Expected name 'Bruschetta'"
    assert menu.starters[0].price == 5.00, "Expected price 5.00 for the starter"


def test_add_main_dish():
    menu = Menu()
    menu.add_main_dish("Lasagna", 9.50, "Lasagna with meat sauce", "non-vegetarian")
    assert len(menu.main_dishes) == 1, "There should be 1 main dish in the menu"
    assert menu.main_dishes[0].name == "Lasagna", "Expected name 'Lasagna'"
    assert menu.main_dishes[0].price == 9.50, "Expected price 9.50 for the main dish"


def test_add_beverage():
    menu = Menu()
    menu.add_beverage("Coca Cola", 3.00, "Refreshing soda", "vegan")
    assert len(menu.beverages) == 1, "There should be 1 beverage in the menu."
    assert menu.beverages[0].name == "Coca Cola", "The name of the beverage is incorrect."
    assert menu.beverages[0].price == 3.00, "The price of the beverage is incorrect."


def test_add_dessert():
    menu = Menu()
    menu.add_dessert("Tiramisu", 4.50, "Coffee-flavored dessert", "vegetarian")
    assert len(menu.desserts) == 1, "There should be 1 dessert in the menu."
    assert menu.desserts[0].name == "Tiramisu", "The name of the dessert is incorrect."
    assert menu.desserts[0].price == 4.50, "The price of the dessert is incorrect."


def test_find_dish_by_name():
    menu = Menu()
    menu.add_starter("Bruschetta", 5.00, "Toasted bread with tomatoes", "vegetarian")
    dish = menu.find_dish_by_name("Bruschetta")
    assert dish.name == "Bruschetta", "Expected to find 'Bruschetta' in the menu"


def test_find_dish_not_in_menu():
    menu = Menu()
    assert menu.find_dish_by_name("Pizza") is None, "Expected to not find 'Pizza' in the menu"


def test_connect_dishes():
    menu = Menu()
    menu.add_starter("Bruschetta", 5.00, "Toasted bread with tomatoes", "vegetarian")
    menu.add_main_dish("Margherita Pizza", 8.50, "Pizza with tomato and mozzarella", "vegetarian")
    menu.connect_dishes("Bruschetta", "Margherita Pizza")

    bruschetta = menu.find_dish_by_name("Bruschetta")
    margherita_pizza = menu.find_dish_by_name("Margherita Pizza")

    assert bruschetta.get_edges() == [
        margherita_pizza
    ], "Bruschetta should be connected to Margherita Pizza."
    assert margherita_pizza.get_reverse_edges() == [
        bruschetta
    ], "Margherita Pizza should be connected to Bruschetta."


def test_show_suggestions(capsys):
    menu = Menu()
    menu.add_starter("Bruschetta", 5.00, "Toasted bread with tomatoes", "vegetarian")
    menu.add_main_dish("Margherita Pizza", 8.50, "Pizza with tomato and mozzarella", "vegetarian")
    menu.connect_dishes("Bruschetta", "Margherita Pizza")

    menu.show_suggestions("Bruschetta")
    captured = capsys.readouterr()
    assert (
        "With Bruschetta our suggestions are: Margherita Pizza.\n" in captured.out
    ), "The output for suggestions is incorrect."


def test_show_suggestions_no_suggestions(capsys):
    menu = Menu()
    menu.add_starter("Bruschetta", 5.00, "Toasted bread with tomatoes", "vegetarian")

    menu.show_suggestions("Bruschetta")
    captured = capsys.readouterr()
    assert (
        "No suggestions for Bruschetta." in captured.out
    ), "The output for no suggestions is incorrect."


def test_show_menu(capsys):
    menu = Menu()
    menu.add_starter("Bruschetta", 5.00, "Toasted bread with tomatoes", "vegetarian")
    menu.add_main_dish("Margherita Pizza", 8.50, "Pizza with tomato and mozzarella", "vegetarian")
    menu.add_beverage("Coca Cola", 3.00, "Refreshing soda", "vegan")
    menu.add_dessert("Tiramisu", 4.50, "Coffee-flavored dessert", "vegetarian")

    # Call the show_menu function to capture the output
    menu.show_menu()

    # Capture printed output
    captured = capsys.readouterr()

    # Check that category titles are present in the output
    assert "Starter" in captured.out, "The Starter section is not displayed in the menu."
    assert "Main Dish" in captured.out, "The Main Dish section is not displayed in the menu."
    assert "Beverage" in captured.out, "The Beverage section is not displayed in the menu."
    assert "Dessert" in captured.out, "The Dessert section is not displayed in the menu."

    # Check that the names of the dishes are present in the output
    assert "Bruschetta" in captured.out, "Bruschetta is not displayed in the menu."
    assert "Margherita Pizza" in captured.out, "Margherita Pizza is not displayed in the menu."
    assert "Coca Cola" in captured.out, "Coca Cola is not displayed in the menu."
    assert "Tiramisu" in captured.out, "Tiramisu is not displayed in the menu."

    # Check that prices are correctly formatted
    assert "€5.00" in captured.out, "The price for Bruschetta is not displayed correctly."
    assert "€8.50" in captured.out, "The price for Margherita Pizza is not displayed correctly."
    assert "€3.00" in captured.out, "The price for Coca Cola is not displayed correctly."
    assert "€4.50" in captured.out, "The price for Tiramisu is not displayed correctly."

    # Check that there is a blank line to separate the categories
    assert (
        captured.out.count("\n") >= 5
    ), "There should be at least 5 newline characters for spacing."
