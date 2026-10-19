# Simple Expense Tracker
# Created by LCS_Backended

import os

expenses = []
file_name = "expenses_log.txt"

print("--- Expense Tracker System ---")

# Step 1: Main data input loop
while True:
    item = input("\nWhat did you buy? (or type 'exit' to finish): ").strip()
    
    if item.lower() == 'exit':
        break
        
    if not item:
        print("[red]Item name cannot be empty![/red]")
        continue

    # Error handling to prevent the program from crashing if the user types letters in the price
    while True:
        try:
            price = input(f"How much did {item} cost? $ ")
            # Replaces comma with dot just in case the user typed it wrong
            price = float(price.replace(',', '.'))
            if price < 0:
                print("Price cannot be negative!")
                continue
            break
        except ValueError:
            print("Invalid price! Please enter a valid number (e.g., 10.50).")
    
    # Saving data into a dictionary
    current_expense = {"item": item, "price": price}
    expenses.append(current_expense)

# Step 2: Final Summary and Report Generation
if expenses:
    print("\n--- Expense Summary ---")
    total = 0
    
    # Open a text file to save the data permanently
    with open(file_name, "a", encoding="utf-8") as file:
        for e in expenses:
            report_line = f"- {e['item']}: $ {e['price']:.2f}"
            print(report_line)
            
            # Writes each item into the text file
            file.write(report_line + "\n")
            total += e['price']
            
        total_line = f"\nGRAND TOTAL: $ {total:.2f}"
        print(total_line)
        file.write(total_line + "\n" + ("=" * 30) + "\n")

    print(f"\n[green]Success![/green] Your expenses have been saved to '{file_name}'.")
    print("--- End of Report ---")
else:
    print("\nNo expenses were recorded.")
