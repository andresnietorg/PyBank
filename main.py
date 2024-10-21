#-*- coding: UTF-8 -*-
"""PyBank Homework Solution."""

# Dependencies
import csv
import os

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate up to the main PyBank folder (assuming the script is in PyBank/analysis)
pybank_dir = os.path.dirname(os.path.dirname(script_dir))

# Files to load and output
file_to_load = os.path.join(pybank_dir, "Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join(script_dir, "budget_analysis.txt")  # Output file path

# Print file paths for verification
print(f"Input file path: {file_to_load}")
print(f"Output file path: {file_to_output}")

# Check if the input file exists
if not os.path.exists(file_to_load):
    print(f"Error: Input file not found at {file_to_load}")
    print("Please check the file path and ensure the CSV file is in the correct location.")
    exit()

# Define variables to track the financial data
total_months = 0
total_net = 0
net_change_list = []
greatest_increase = {"date": "", "amount": float("-inf")}
greatest_decrease = {"date": "", "amount": float("inf")}

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    # Process each row of data
    for row in reader:
        # Track the total
        total_months += 1
        total_net += int(row[1])

        # Track the net change
        net_change = int(row[1]) - prev_net
        net_change_list.append(net_change)
        prev_net = int(row[1])

        # Calculate the greatest increase in profits (date and amount)
        if net_change > greatest_increase["amount"]:
            greatest_increase["date"] = row[0]
            greatest_increase["amount"] = net_change

        # Calculate the greatest decrease in profits (date and amount)
        if net_change < greatest_decrease["amount"]:
            greatest_decrease["date"] = row[0]
            greatest_decrease["amount"] = net_change

# Calculate the average net change across the months
average_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["amount"]})
Greatest Decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["amount"]})
"""

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

print(f"Analysis exported to {file_to_output}")

