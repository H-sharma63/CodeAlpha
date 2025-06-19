stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "MSFT": 320,
    "AMZN": 135
}

portfolio = {}
total_value = 0

print("📈 Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Enter stock symbol and quantity (type 'done' to finish)\n")

while True:
    stock = input("Enter stock symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Stock not recognized. Try again.\n")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("⚠️ Please enter a valid number.\n")
        continue

    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

print("\n💼 Your Portfolio:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\n💰 Total Investment Value: ${total_value}")

save_option = input("\nWould you like to save this to a file? (y/n): ").lower()

if save_option == 'y':
    file_type = input("Save as .txt or .csv? ").lower()
    filename = "portfolio." + ("csv" if file_type == "csv" else "txt")

    with open(filename, "w") as file:
        if file_type == "csv":
            file.write("Stock,Quantity,Price,Value\n")
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                file.write(f"{stock},{qty},{stock_prices[stock]},{value}\n")
            file.write(f"Total,,,{total_value}\n")
        else:
            file.write("Your Portfolio:\n")
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                file.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}\n")
            file.write(f"\nTotal Investment Value: ${total_value}\n")

    print(f"✅ Portfolio saved to '{filename}'")
