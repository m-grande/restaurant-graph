import pytest
from restaurant.order import Order


class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price


def test_add_item():
    order = Order()
    dish = Dish("Margherita Pizza", 8.50)
    order.add_item(dish, 2)
    assert len(order.items) == 1, "There should be 1 item in the order"
    assert order.items[0][0].name == "Margherita Pizza", "Dish name is incorrect"
    assert order.items[0][1] == 2, "Quantity is incorrect"


def test_remove_item():
    order = Order()
    dish1 = Dish("Margherita Pizza", 8.50)
    dish2 = Dish("Tiramisu", 4.50)
    order.add_item(dish1, 2)
    order.add_item(dish2, 1)
    order.remove_item("Margherita Pizza")
    assert len(order.items) == 1, "There should be 1 item in the order after removing"
    assert order.items[0][0].name == "Tiramisu", "Remaining dish should be Tiramisu"


def test_calculate_total():
    order = Order()
    dish1 = Dish("Pizza", 8.50)
    dish2 = Dish("Tiramisu", 4.50)
    order.add_item(dish1, 2)
    order.add_item(dish2, 1)
    assert order.calculate_total() == 21.50, "Expected total of 21.50 for the order"


def test_generate_receipt(capsys):
    order = Order()
    dish1 = Dish("Margherita Pizza", 8.50)
    dish2 = Dish("Tiramisu", 4.50)

    order.add_item(dish1, 2)
    order.add_item(dish2, 1)

    # Call generate_receipt and capture the output
    order.generate_receipt()
    captured = capsys.readouterr()

    # Step-by-step detailed assertions
    assert "======= YOUR RECEIPT =======" in captured.out, "Receipt header is missing or incorrect"
    assert "Quantity" in captured.out, "'Quantity' column header is missing"
    assert "Dish Name" in captured.out, "'Dish Name' column header is missing"
    assert "Unit Price" in captured.out, "'Unit Price' column header is missing"
    assert "Total Price" in captured.out, "'Total Price' column header is missing"

    # Check the individual rows
    assert "2" in captured.out, "Quantity of Margherita Pizza is missing or incorrect"
    assert (
        "Margherita Pizza" in captured.out
    ), "Dish name 'Margherita Pizza' is missing or incorrect"
    assert "€8.50" in captured.out, "Unit price for Margherita Pizza is missing or incorrect"
    assert "€17.00" in captured.out, "Total price for Margherita Pizza is missing or incorrect"

    assert "1" in captured.out, "Quantity of Tiramisu is missing or incorrect"
    assert "Tiramisu" in captured.out, "Dish name 'Tiramisu' is missing or incorrect"
    assert "€4.50" in captured.out, "Unit price for Tiramisu is missing or incorrect"
    assert "€4.50" in captured.out, "Total price for Tiramisu is missing or incorrect"

    # Check the final total
    assert "Total to pay: €21.50" in captured.out, "The final total is missing or incorrect"
