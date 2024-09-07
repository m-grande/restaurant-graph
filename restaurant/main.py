from data import restaurant_menu
from fuzzywuzzy import process
from order import Order


def restaurant_description():
    print("===============================")
    print("WELCOME TO OUR RESTAURANT")
    print("===============================")
    print(
        "Our restaurant offers a unique dining experience, blending traditional Italian cuisine\n"
        "with modern culinary techniques. Our menu features a range of exquisite dishes, including\n"
        "freshly made pastas, wood-fired pizzas, and artisanal desserts, all crafted from the finest\n"
        "locally sourced ingredients."
    )
    print("\n")
    print(
        "Whether you're a fan of rich, meaty lasagnas or prefer light, vegetarian risottos,\n"
        "we have something for everyone. Our selection of fine wines and craft beers complements\n"
        "the food perfectly, ensuring an unforgettable dining experience.\n"
    )
    print("Enjoy the flavors of Italy in a warm and welcoming atmosphere!\n")


def ask_yes_no(question):
    answer = ""
    while answer not in ["y", "n"]:
        answer = input(f"{question}\nPlease type 'y' or 'n': ").lower()
        if answer in ["y", "n"]:
            return answer
        else:
            print("Invalid input")


def check_out_menu():
    print("\nCheck out our menu!")
    while True:
        if input("Press Enter to continue...") == "":
            break

    restaurant_menu.show_menu()


def closest_match(dish_name):
    # List of all names of dishes on the menu
    dish_names = [dish.name for dish in restaurant_menu.menu]

    # Use fuzzy matching to find similar dishes
    closest_match = process.extractOne(dish_name, dish_names, score_cutoff=80)

    if closest_match:
        if ask_yes_no(f"\nDid you mean {closest_match[0]}?") == "y":
            return restaurant_menu.find_dish_by_name(closest_match[0])

    return None


def ask_for_dish_suggestions():
    if ask_yes_no("\nWould you like any suggestions regarding a dish?") == "y":
        while True:
            restaurant_menu.show_menu()

            while True:
                dish_name = input("\nEnter the name of the dish: ")

                # Find the dish on the menu
                dish = restaurant_menu.find_dish_by_name(dish_name)

                if dish:
                    category_desc = get_category_description(dish.category)

                    print(
                        f"\nThe {dish.name} is {category_desc} and is described as: {dish.description}.\n"
                    )

                    restaurant_menu.show_suggestions(dish.name)
                    break

                else:
                    # Use fuzzy matching to find a similar dish
                    dish = closest_match(dish_name)

                    if dish:
                        category_desc = get_category_description(dish.category)
                        print(
                            f"\nThe {dish.name} is {category_desc} and is described as: {dish.description}."
                        )

                        restaurant_menu.show_suggestions(dish.name)
                        break

                    else:
                        print(f"The dish '{dish_name}' is not on the menu. Please try again.")

            if ask_yes_no("\nWould you like any other suggestions regarding a dish?") == "n":
                break

    else:
        print("Alright, no suggestions at the moment!")


def get_category_description(category):
    category_descriptions = {
        "vegetarian": "a vegetarian dish",
        "vegan": "a vegan dish",
        "spicy": "a spicy dish",
        "meat": "a meat-based dish",
        "seafood": "a seafood dish",
    }

    return category_descriptions.get(category, "a dish")


def ask_quantity_and_add_to_order(order, selected_dish):
    while True:
        try:
            quantity = int(
                input(f"How many portions of {selected_dish.name} would you like to order? ")
            )
            if quantity > 0:
                order.add_item(selected_dish, quantity)
                break
            else:
                print("Please enter a quantity greater than 0.")
        except ValueError:
            print("Please enter a valid number.")


def create_order():
    if ask_yes_no("\nWould you like to order something?") == "y":
        order = Order()
        while True:
            restaurant_menu.show_menu()

            while True:
                dish_name = input("\nEnter the name of the dish you wish to order: ")

                selected_dish = restaurant_menu.find_dish_by_name(dish_name)

                if selected_dish:
                    ask_quantity_and_add_to_order(order, selected_dish)
                    break
                else:
                    selected_dish = closest_match(dish_name)

                    if selected_dish:
                        ask_quantity_and_add_to_order(order, selected_dish)
                        break
                    else:
                        print(f"The dish '{dish_name}' is not on the menu. Please try again.")

            if ask_yes_no("\nWould you like to order something else?") == "n":
                break
        order.generate_receipt()
    else:
        print("Alright, no orders at the moment! ")


def greetings():
    print("\nThank you for visiting our restaurant!")


def main():
    restaurant_description()
    check_out_menu()
    ask_for_dish_suggestions()
    create_order()
    greetings()


if __name__ == "__main__":
    main()
