import csv
import os

# Path to the budget data CSV file
csv_folder = "resources"
budget_data_csv = os.path.join(csv_folder, "budget_data.csv")

# Variable Initialization
total_months = 0
net_total = 0
previous_profit_loss = 0
monthly_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the budget data CSV file
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header row
    next(csvreader)

    # Iterate through each row in the CSV
    for row in csvreader:
        # Calculate total number of months
        total_months += 1

        # Calculate net total amount of "Profit/Losses"
        net_total += int(row[1])

        # Calculate change in profit/loss from previous month (skip for the first month)
        if total_months > 1:
            current_change = int(row[1]) - previous_profit_loss
            monthly_changes.append(current_change)

            # Determine greatest increase in profits (date and amount)
            if current_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = current_change

            # Determine greatest decrease in profits (date and amount)
            if current_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = current_change

        # Set previous profit/loss for the next iteration
        previous_profit_loss = int(row[1])

# Calculate the average change in profits/losses
average_change = round(sum(monthly_changes) / len(monthly_changes), 2)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output to the terminal
print(output)

# Write the output to a text file
output_file = os.path.join(".", "financial_analysis.txt")
with open(output_file, "w") as txt_file:
    txt_file.write(output)

print(f"Results have been exported to: {output_file}")
