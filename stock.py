
# Hardcoded stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 300,
    "GOOG": 140
}

# Ask user how many stocks they want to enter
n = int(input("How many different stocks do you want to add? "))

portfolio = {}
total_investment = 0

for i in range(n):
    stock = input(f"Enter stock symbol {i+1}: ").upper()
    qty = int(input(f"Enter quantity of {stock}: "))
    
    if stock in stock_prices:
        value = stock_prices[stock] * qty
        portfolio[stock] = value
        total_investment += value
    else:
        print(f"⚠️ Stock {stock} not found in price list.")

print("\n--- Portfolio Summary ---")
for stock, value in portfolio.items():
    print(f"{stock}: ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to file
save_choice = input("\nDo you want to save the result to a file? (y/n): ").lower()
if save_choice == "y":
    with open("portfolio.txt", "w") as f:
        f.write("--- Portfolio Summary ---\n")
        for stock, value in portfolio.items():
            f.write(f"{stock}: ${value}\n")
        f.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("✅ Portfolio saved to portfolio.txt")