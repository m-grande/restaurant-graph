import pytest
from restaurant.node import Node


def test_node_creation():
    node = Node("Spaghetti with Clams", 10.0, "Spaghetti with fresh clams", "Seafood")
    assert node.name == "Spaghetti with Clams", "The node name is incorrect"
    assert node.price == 10.0, "The node price is incorrect"
    assert node.description == "Spaghetti with fresh clams", "The node description is incorrect"
    assert node.category == "Seafood", "The node category is incorrect"


def test_add_edge():
    node_1 = Node("Spaghetti with Clams", 10.0, "Spaghetti with fresh clams", "seafood")
    node_2 = Node("White Wine", 7.00, "A crisp white wine with citrus notes", "vegetarian")
    node_1.add_edge(node_2)
    assert node_1 in node_2.reverse_edges, "Node 1 not found in node 2's reverse edges"
    assert node_2 in node_1.edges, "Node 2 not found in node 1's edges"


def test_get_edges():
    node = Node("Pizza", 8.50, "Cheese pizza", "Main Dish")
    assert node.get_edges() == [], "Expected no edges when none are added"


def test_multiple_edges():
    node_1 = Node("Spaghetti with Clams", 10.0, "Spaghetti with fresh clams", "seafood")
    node_2 = Node("White Wine", 7.00, "A crisp and refreshing white wine", "vegetarian")
    node_3 = Node("Tiramisu", 5.00, "Classic Italian dessert", "dessert")

    node_1.add_edge(node_2)
    node_1.add_edge(node_3)

    assert node_2 in node_1.edges, "Node 2 not found in node 1's edges"
    assert node_3 in node_1.edges, "Node 3 not found in node 1's edges"
