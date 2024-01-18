import random

class ShoeShop:
    def __init__(self):
        # Initialize the balance and shoe inventory
        self.balance = 500  # Updated initial balance to $500
        self.shoes = {
            'Sneakers': 0,
            'Boots': 0,
            'Sandals': 0
            # Add more shoes here
        }
        # Price ranges for each shoe
        self.buy_price_ranges = {
            'Sneakers': (0, 100),
            'Boots': (400, 700),
            'Sandals': (100, 200)
            # Add more shoes and price ranges here
        }
        self.sell_price_ranges = {
            'Sneakers': (0, 100),
            'Boots': (400, 700),
            'Sandals': (100, 200)
            # Add more shoes and price ranges here
        }
        # Generate initial prices within the specified ranges
        self.buy_prices = {shoe: random.randint(price_range[0], price_range[1]) for shoe, price_range in self.buy_price_ranges.items()}
        self.sell_prices = {shoe: random.randint(price_range[0], price_range[1]) for shoe, price_range in self.sell_price_ranges.items()}

    def display_shoe_shop_menu(self):
        # Display the menu for The Shoe Shop
        print("\n=== The Shoe Shop ===")
        print("1. Buy Shoes")
        print("2. Quit")
        print(f"Current Balance: ${self.balance}")

    def display_sneaker_con_menu(self):
        # Display the menu for Sneaker Con
        print("\n=== Sneaker Con ===")
        print("1. Sell Shoes")
        print("2. Quit")
        print(f"Current Balance: ${self.balance}")

    def display_inventory_menu(self):
        # Display the menu for viewing the shoe inventory
        print("\n=== View Inventory ===")
        for i, (shoe, quantity) in enumerate(self.shoes.items(), start=1):
            print(f"{i}. {shoe} - Quantity: {quantity}")
        print("======================")

    def display_buy_options(self):
        # Display options to buy shoes
        print("\n=== Buy Options ===")
        for i, (shoe, price) in enumerate(self.buy_prices.items(), start=1):
            print(f"{i}. {shoe} - Price: ${price}")
        print("===================")

    def buy_shoe(self, option, quantity):
        # Buy a shoe from The Shoe Shop based on the selected option number
        if 1 <= option <= len(self.buy_prices):
            shoe = list(self.buy_prices.keys())[option - 1]
            price = self.buy_prices[shoe]

            if self.balance >= quantity * price:
                self.shoes[shoe] += quantity
                self.balance -= quantity * price
                print(f"You bought {quantity} {shoe}(s) for ${quantity * price}.")
            else:
                print("Not enough funds!")
        else:
            print("Invalid option.")

    def display_sell_options(self):
        # Display options to sell shoes at Sneaker Con
        print("\n=== Sell Options ===")
        for i, (shoe, quantity) in enumerate(self.shoes.items(), start=1):
            sell_price = self.sell_prices[shoe]
            print(f"{i}. {shoe} - Quantity: {quantity} - Sell Price: ${sell_price}")
        print("====================")

    def sell_shoe(self, option, quantity):
        # Sell a shoe at Sneaker Con based on the selected option number
        if 1 <= option <= len(self.shoes):
            shoe = list(self.shoes.keys())[option - 1]
            sell_price = self.sell_prices[shoe]

            if self.shoes[shoe] >= quantity:
                earnings = quantity * sell_price
                self.shoes[shoe] -= quantity
                self.balance += earnings
                print(f"You sold {quantity} {shoe}(s) for ${earnings}.")
            else:
                print(f"Not enough {shoe} in inventory!")
        else:
            print("Invalid option!")

# Main game loop
def main():
    shop = ShoeShop()

    while True:
        print("\n=== Game Menu ===")
        print("1. The Shoe Shop")
        print("2. Sneaker Con")
        print("3. View Inventory")
        print("4. Quit")
        print(f"Current Balance: ${shop.balance}")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            shop.display_shoe_shop_menu()
            shop.display_buy_options()
            shop_choice = input("Enter the option number (1-2): ")
            if shop_choice == '1':
                quantity = int(input("Enter the quantity: "))
                shop.buy_shoe(int(input("Enter the option number of the shoe you want to buy: ")), quantity)
        elif choice == '2':
            shop.display_sneaker_con_menu()
            shop.display_sell_options()
            shop_choice = input("Enter the option number (1-2): ")
            if shop_choice == '1':
                quantity = int(input("Enter the quantity: "))
                shop.sell_shoe(int(input("Enter the option number of the shoe you want to sell: ")), quantity)
        elif choice == '3':
            shop.display_inventory_menu()
        elif choice == '4':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == '__main__':
    main()
