"""
Stock Portfolio Tracker
CodeAlpha Python Programming Internship - Task 2

A simple console-based stock portfolio calculator. Stock prices are
manually defined (hardcoded) sample values, NOT live market prices.
Uses only Python's standard library.
"""

import csv

# Manually defined sample stock prices (NOT live market data)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185,
    "NVDA": 120,
    "META": 500,
    "NFLX": 680,
    "IBM": 190,
    "ORCL": 170
}


def display_welcome():
    """Show a welcome message and explain the sample-data disclaimer."""
    print("=" * 45)
    print("     STOCK PORTFOLIO TRACKER")
    print("=" * 45)
    print("Note: Stock prices below are manually defined")
    print("sample prices, not real-time market prices.\n")


def display_available_stocks(stock_prices):
    """Print every available stock symbol and its sample price."""
    print("Available stocks:")
    for symbol, price in stock_prices.items():
        print(f"  {symbol:<6} - ${price}")
    print()


def get_stock_symbol(stock_prices):
    """
    Ask the user for a stock symbol and validate that it exists
    in the STOCK_PRICES dictionary. Keeps asking until valid.
    """
    while True:
        symbol = input("Enter stock symbol: ").upper().strip()

        if len(symbol) == 0:
            print("Stock symbol cannot be empty. Please try again.")
        elif symbol not in stock_prices:
            print(f"'{symbol}' is not in the available stock list. Please try again.")
        else:
            return symbol


def get_quantity():
    """
    Ask the user for a quantity and validate that it is a positive
    whole number. Keeps asking until valid.
    """
    while True:
        quantity_input = input("Enter quantity: ").strip()

        if len(quantity_input) == 0:
            print("Quantity cannot be empty. Please try again.")
            continue

        if not quantity_input.isdigit():
            print("Quantity must be a positive whole number. Please try again.")
            continue

        quantity = int(quantity_input)

        if quantity <= 0:
            print("Quantity must be greater than zero. Please try again.")
            continue

        return quantity


def calculate_investment(price, quantity):
    """Calculate the investment value for one stock entry."""
    return price * quantity


def ask_add_another():
    """Ask the user if they want to add another stock to the portfolio."""
    while True:
        choice = input("Add another stock? (yes/no): ").lower().strip()
        if choice in ("yes", "y"):
            return True
        elif choice in ("no", "n"):
            return False
        else:
            print("Please answer 'yes' or 'no'.")


def build_portfolio(stock_prices):
    """
    Collect one or more stock entries from the user.
    Returns a list of dictionaries, one per stock entry.
    """
    portfolio = []

    while True:
        symbol = get_stock_symbol(stock_prices)
        quantity = get_quantity()
        price = stock_prices[symbol]
        investment = calculate_investment(price, quantity)

        portfolio.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "investment": investment
        })

        print(f"Added: {quantity} share(s) of {symbol} at ${price} each.\n")

        if not ask_add_another():
            break

    return portfolio


def display_portfolio_summary(portfolio):
    """Print a formatted summary of every stock entry and the grand total."""
    print("\n" + "=" * 45)
    print("     PORTFOLIO SUMMARY")
    print("=" * 45)
    print(f"{'Symbol':<8}{'Quantity':<10}{'Price':<10}{'Investment':<12}")
    print("-" * 45)

    total_investment = 0
    for entry in portfolio:
        print(f"{entry['symbol']:<8}{entry['quantity']:<10}"
              f"${entry['price']:<9}${entry['investment']:<11}")
        total_investment += entry["investment"]

    print("-" * 45)
    print(f"Total Investment Value: ${total_investment}")
    print("=" * 45)

    return total_investment


def ask_save_choice():
    """Ask the user whether they want to save the portfolio to a file."""
    while True:
        choice = input("\nSave portfolio to a file? (yes/no): ").lower().strip()
        if choice in ("yes", "y"):
            return True
        elif choice in ("no", "n"):
            return False
        else:
            print("Please answer 'yes' or 'no'.")


def get_file_format_choice():
    """Ask the user whether to save as .txt or .csv."""
    while True:
        choice = input("Save as (txt/csv): ").lower().strip()
        if choice in ("txt", "csv"):
            return choice
        else:
            print("Please enter 'txt' or 'csv'.")


def save_as_txt(portfolio, total_investment, filename):
    """Save the portfolio summary to a plain text file."""
    with open(filename, "w") as file:
        file.write("STOCK PORTFOLIO SUMMARY\n")
        file.write("=" * 45 + "\n")
        file.write("(Sample stock prices - not live market data)\n\n")
        for entry in portfolio:
            file.write(
                f"Symbol: {entry['symbol']}, "
                f"Quantity: {entry['quantity']}, "
                f"Price: ${entry['price']}, "
                f"Investment: ${entry['investment']}\n"
            )
        file.write("\n" + "-" * 45 + "\n")
        file.write(f"Total Investment Value: ${total_investment}\n")


def save_as_csv(portfolio, total_investment, filename):
    """Save the portfolio summary to a CSV file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Symbol", "Quantity", "Price", "Investment"])
        for entry in portfolio:
            writer.writerow([
                entry["symbol"],
                entry["quantity"],
                entry["price"],
                entry["investment"]
            ])
        writer.writerow([])
        writer.writerow(["Total Investment Value", "", "", total_investment])


def save_portfolio(portfolio, total_investment):
    """Handle the full save flow: ask format, build filename, write file."""
    file_format = get_file_format_choice()
    filename = f"portfolio_result.{file_format}"

    if file_format == "txt":
        save_as_txt(portfolio, total_investment, filename)
    else:
        save_as_csv(portfolio, total_investment, filename)

    print(f"Portfolio saved to '{filename}'.")


def main():
    """Program entry point: welcome, build portfolio, summarize, save."""
    display_welcome()
    display_available_stocks(STOCK_PRICES)

    portfolio = build_portfolio(STOCK_PRICES)
    total_investment = display_portfolio_summary(portfolio)

    if ask_save_choice():
        save_portfolio(portfolio, total_investment)

    print("\nThank you for using Stock Portfolio Tracker. Goodbye!")


if __name__ == "__main__":
    main()
