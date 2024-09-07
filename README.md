# Restaurant Menu and Ordering System

## Overview

This project is a restaurant menu and ordering system built using Python. It allows customers to browse a menu, make orders, and receive suggestions for dish pairings. The project uses a graph structure to manage relationships between dishes (like suggesting drinks or side dishes with main courses).

The system consists of various components such as nodes (representing dishes), a menu (handling dish listings), and an order system that manages customer orders. The project includes a comprehensive test suite to ensure the functionality of the core components.

## Project Structure


- `node.py` Defines the Node class representing individual dishes
- `menu.py` Defines the Menu class to handle dish listings and relationships
- `order.py` Handles customer orders, adding/removing items, and generating receipts
- `data.py` Initializes the restaurant menu with dishes and suggestions 
- `main.py` Contains the main application logic
- `test_node.py` Tests for the Node class
- `test_menu.py` Tests for the Menu class
- `test_order.py` Tests for the Order class
- `test_main.py` Tests for the main application logic


## Components

- **`data.py`**: Initializes and sets up the menu with dishes, including starters, main dishes, beverages, and desserts. Also defines the relationships between these dishes, such as suggested pairings.

- **`main.py`**: The core logic of the restaurant system. It includes functions for browsing the menu, making orders, and generating receipts. It also interacts with the menu and order systems to process customer inputs.

- **`menu.py`**: Defines the `Menu` class, which manages the listing of all dishes (starters, main dishes, beverages, and desserts) and the connections between dishes (like suggestions).

- **`node.py`**: Defines the `Node` class, which represents a dish in the menu. Each node has a name, price, description, and category. Dishes can also be connected to other dishes (e.g., beverages suggested with meals).

- **`order.py`**: Manages customer orders. The `Order` class allows adding and removing items, calculating totals, and generating receipts for the customer.

## Installation and Setup

1. Clone the repository:

```
git clone https://github.com/m-grande/restaurant-graph.git
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

## Running the Application
To run the main application and test the menu system:

```
python3 restaurant/main.py
```
This will run the interactive menu system where you can browse dishes, place orders, and receive suggestions for pairings.

## Running Tests
The project includes a comprehensive suite of tests using `pytest`. To run all tests:

```
pytest
```
This will execute the test suite located in the `restaurant/tests/` directory, which includes tests for all the main components (Menu, Node, Order, and application logic in `main.py`).