# Import os and CSV files

import os
import csv

# Read CSV file path
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Define main function and call other functions

profit = []
monthly_changes = []
date = []

count = 0
net_profit = 0
total_change_profits = 0
initial_profit = 0
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
# print(csvreader)
    csv_header = next(csvreader)
    # first_row = next(csvreader)
    # total_change_profits += int(row[1])
# preparing the Ask
    for row in csvreader:
        # Creating count of months
        count += 1
        # Creating list of months for Max and Min
        date.append(row[0])
        #
        profit.append(row[1])
        net_profit = net_profit + int(row[1])
        final_profit = int(row[1])

        monthly_change_profits = final_profit - initial_profit

        # Save list for Min and Max

        total_change_profits+=(monthly_change_profits)

        monthly_changes.append(monthly_change_profits)
        initial_profit = int(row[1])


        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

        max_date = date[monthly_changes.index(greatest_increase_profits)]
        min_date = date[monthly_changes.index(greatest_decrease_profits)]
    average_change_profits = (total_change_profits) / (count)

    print('Financial Analysis')
    print('-' * 32)
    print(f"Total Months: {count}")
    print(f"Total profits: ${net_profit: .2f}")
    print(f"Average Change: ${average_change_profits: .2f}")
    print(f"Greatest Increase in Profits: {max_date} ${greatest_increase_profits: .2f}")
    print(f"Greatest Decrease in Profits: {min_date} ${greatest_decrease_profits: .2f}")
    print("-" * 32)
    with open('financial_analysis.txt', 'w') as text:
        text.write('Financial Analysis\n')

        text.write('-' * 32 + '\n')
        text.write(f"Total Months: {count}\n")
        text.write(f"Total profits: ${net_profit: .2f}\n")
        text.write(f"Average Change: ${average_change_profits: .2f}\n")
        text.write(f"Greatest Increase in Profits: {max_date} ${greatest_increase_profits: .2f}\n")
        text.write(f"Greatest Decrease in Profits: {min_date} ${greatest_decrease_profits: .2f}\n")
        text.write("-" * 32)
