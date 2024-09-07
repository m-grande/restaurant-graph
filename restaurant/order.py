from tabulate import tabulate


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, dish, quantity=1):
        self.items.append((dish, quantity))

    def remove_item(self, dish_name):
        self.items = [item for item in self.items if item[0].name != dish_name]

    def calculate_total(self):
        total = 0
        for dish, quantity in self.items:
            total += dish.price * quantity
        return total

    def generate_receipt(self):
        receipt_data = []
        for dish, quantity in self.items:
            total_price = dish.price * quantity
            receipt_data.append([quantity, dish.name, f"€{dish.price:.2f}", f"€{total_price:.2f}"])

        print("\n======= YOUR RECEIPT =======\n")
        print(
            tabulate(
                receipt_data,
                headers=["Quantity", "Dish Name", "Unit Price", "Total Price"],
                tablefmt="fancy_grid",
            )
        )

        total = self.calculate_total()
        print(f"\nTotal to pay: €{total:.2f}")
