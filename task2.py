
# STOCK PORTFOLIO TRACKER
# A beginner-friendly Python project

import csv
import os

FILE_NAME = "portfolio.csv"

# Load saved stocks from the file
def load_portfolio():
    portfolio = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                portfolio.append({
                    "name": row["name"],
                    "quantity": int(row["quantity"]),
                    "buy_price": float(row["buy_price"]),
                    "current_price": float(row["current_price"])
                })

    return portfolio


# Save stocks to the file
def save_portfolio(portfolio):
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = [
            "name", "quantity",
            "buy_price", "current_price"
        ]

        writer = csv.DictWriter(
            file, fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(portfolio)


# Add a new stock
def add_stock(portfolio):
    print("\n--- ADD STOCK ---")

    name = input("Enter stock name: ").strip()

    if not name:
        print("Stock name cannot be empty.")
        return

    try:
        quantity = int(input("Enter quantity: "))
        buy_price = float(input("Enter purchase price per share: "))
        current_price = float(input("Enter current price per share: "))

        if quantity <= 0 or buy_price <= 0 or current_price < 0:
            print("Enter a positive quantity and purchase price.")
            print("Current price cannot be negative.")
            return

        stock = {
            "name": name,
            "quantity": quantity,
            "buy_price": buy_price,
            "current_price": current_price
        }

        portfolio.append(stock)
        save_portfolio(portfolio)

        print("Stock added successfully!")

    except ValueError:
        print("Invalid input. Please enter numbers for quantity and prices.")


# Display all stocks and calculate profit or loss
def view_portfolio(portfolio):
    print("\n--- YOUR STOCK PORTFOLIO ---")

    if len(portfolio) == 0:
        print("Your portfolio is empty.")
        return

    total_investment = 0
    total_current_value = 0

    print("-" * 90)
    print(
        f"{'No.':<5}{'Stock':<18}{'Qty':<8}"
        f"{'Buy Price':<14}{'Current':<14}"
        f"{'Profit/Loss':<15}"
    )
    print("-" * 90)

    for index, stock in enumerate(portfolio, start=1):
        investment = stock["quantity"] * stock["buy_price"]
        current_value = stock["quantity"] * stock["current_price"]
        profit_loss = current_value - investment

        total_investment += investment
        total_current_value += current_value

        print(
            f"{index:<5}"
            f"{stock['name']:<18}"
            f"{stock['quantity']:<8}"
            f"{stock['buy_price']:<14.2f}"
            f"{stock['current_price']:<14.2f}"
            f"{profit_loss:<15.2f}"
        )

    print("-" * 90)

    total_profit_loss = total_current_value - total_investment

    if total_investment > 0:
        total_return = (total_profit_loss / total_investment) * 100
    else:
        total_return = 0

    print(f"Total Investment : Rs. {total_investment:.2f}")
    print(f"Current Value    : Rs. {total_current_value:.2f}")
    print(f"Total Profit/Loss: Rs. {total_profit_loss:.2f}")
    print(f"Overall Return   : {total_return:.2f}%")


# Update the current price of a stock
def update_price(portfolio):
    print("\n--- UPDATE STOCK PRICE ---")

    if not portfolio:
        print("Your portfolio is empty.")
        return

    view_portfolio(portfolio)

    try:
        number = int(input("\nEnter stock number to update: "))

        if number < 1 or number > len(portfolio):
            print("Invalid stock number.")
            return

        new_price = float(input("Enter the new current price: "))

        if new_price < 0:
            print("Price cannot be negative.")
            return

        portfolio[number - 1]["current_price"] = new_price

        save_portfolio(portfolio)
        print("Stock price updated successfully!")

    except ValueError:
        print("Please enter a valid number.")


# Remove a stock
def remove_stock(portfolio):
    print("\n--- REMOVE STOCK ---")

    if not portfolio:
        print("Your portfolio is empty.")
        return

    view_portfolio(portfolio)

    try:
        number = int(input("\nEnter stock number to remove: "))

        if number < 1 or number > len(portfolio):
            print("Invalid stock number.")
            return

        removed = portfolio.pop(number - 1)

        save_portfolio(portfolio)

        print(removed["name"], "removed successfully!")

    except ValueError:
        print("Please enter a valid number.")


# Main menu
def main():
    portfolio = load_portfolio()

    while True:
        print("\n==============================")
        print("   STOCK PORTFOLIO TRACKER")
        print("==============================")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Update Current Stock Price")
        print("4. Remove Stock")
        print("5. Exit")
        print("==============================")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_stock(portfolio)

        elif choice == "2":
            view_portfolio(portfolio)

        elif choice == "3":
            update_price(portfolio)

        elif choice == "4":
            remove_stock(portfolio)

        elif choice == "5":
            print("Your portfolio has been saved.")
            print("Thank you for using Stock Portfolio Tracker!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


# Start the program
if __name__ == "__main__":
    main()
