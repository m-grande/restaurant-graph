from unittest.mock import MagicMock, patch

import pytest
from restaurant.main import ask_for_dish_suggestions, ask_yes_no, closest_match, create_order


def test_ask_yes_no():
    question = "Question"

    # Test case where user inputs 'y' on the first try
    with patch("builtins.input", side_effect=["y"]):
        assert ask_yes_no(question) == "y", "Expected 'y' for user input 'y'"

    # Test case where user inputs 'n' on the first try
    with patch("builtins.input", side_effect=["n"]):
        assert ask_yes_no(question) == "n", "Expected 'n' for user input 'n'"

    # Test case where user inputs invalid data first, then 'n'
    with patch("builtins.input", side_effect=["1234", "n"]):
        assert ask_yes_no(question) == "n", "Expected 'n' after invalid input"


def test_closest_match():
    # Create a Menu object
    restaurant_menu = MagicMock()

    # Add some dishes to the menu
    restaurant_menu.add_starter("Bruschetta", 5.00, "Toasted bread with tomatoes", "Vegetarian")
    restaurant_menu.add_dessert("Tiramisu", 4.50, "Classic Italian dessert", "Vegetarian")
    restaurant_menu.add_beverage("Water", 1.00, "Still water", "Vegan")

    # Case 1: The user confirms they want Bruschetta
    with patch("builtins.input", side_effect=["y"]):
        result_dish = closest_match("brushceta")
        assert result_dish.name == "Bruschetta"

    # Case 2: No valid input (no match found)
    result_dish = closest_match("")
    assert result_dish is None


def test_ask_for_dish_suggestions():
    # Create a mock Menu object
    mock_menu = MagicMock()

    # Create a dish mock object
    mock_dish = MagicMock()
    mock_dish.name = "Bruschetta"
    mock_dish.description = "Toasted bread with tomatoes"
    mock_dish.category = "Vegetarian"

    # Configure the find_dish_by_name mock to return mock_dish
    mock_menu.find_dish_by_name.return_value = mock_dish

    # Simulates the show_menu and show_suggestions method
    mock_menu.show_menu = MagicMock()
    mock_menu.show_suggestions = MagicMock()

    with patch("restaurant.main.restaurant_menu", mock_menu), patch(
        "restaurant.main.ask_yes_no", side_effect=["y", "n"]
    ), patch("builtins.input", side_effect=["Bruschetta", "n"]), patch(
        "restaurant.main.closest_match"
    ) as mock_closest_match:

        # Simulates no fuzzy matching
        mock_closest_match.return_value = None

        ask_for_dish_suggestions()

        # Check that the menu has been shown
        mock_menu.show_menu.assert_called()

        # Check that the suggestions for Bruschetta have been shown
        mock_menu.show_suggestions.assert_called_with("Bruschetta")

        # Checks that closest_match was not called as the dish was found directly
        mock_closest_match.assert_not_called()


def test_create_order():
    # Create a mocked menu and order
    mock_menu = MagicMock()
    mock_order = MagicMock()

    # Create a mocked dish object
    mock_dish = MagicMock()
    mock_dish.name = "Bruschetta"
    mock_dish.description = "Toasted bread with tomatoes"
    mock_dish.category = "Vegetarian"

    # Mock find_dish_by_name to return the dish
    mock_menu.find_dish_by_name.return_value = mock_dish

    # Patch the restaurant_menu and Order
    with patch("restaurant.main.restaurant_menu", mock_menu), patch(
        "restaurant.main.Order", return_value=mock_order
    ), patch("restaurant.main.ask_yes_no", side_effect=["y", "n"]), patch(
        "builtins.input", side_effect=["Bruschetta"]
    ), patch(
        "restaurant.main.closest_match"
    ) as mock_closest_match, patch(
        "restaurant.main.ask_quantity_and_add_to_order"
    ) as mock_ask_quantity:

        # Simulate no fuzzy match
        mock_closest_match.return_value = None

        # Call the function
        create_order()

        # Verify the menu is shown
        mock_menu.show_menu.assert_called()

        # Verify the dish was found and quantity was asked
        mock_menu.find_dish_by_name.assert_called_with("Bruschetta")
        mock_ask_quantity.assert_called_with(mock_order, mock_dish)

        # Verify the receipt was generated
        mock_order.generate_receipt.assert_called_once()

        # Verify closest_match was not called
        mock_closest_match.assert_not_called()
