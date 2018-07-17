import os
import csv

budget_data = os.path.join('budget_data.csv')

# Variables to Hold Data
num_months = 0
profit_total = 0
previous_profit = 0
total_change = 0
change = 0
previous_value = 0
max_increase_profit = 0
max_increase_date = ''
max_decrease_profit = 0
max_decrease_date = ''

# Open File: with open(filename, 'r') as csvfile:
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)
    for row in csvreader:
        num_months += 1
        profit_total = int(row[1])
        change = profit_total - previous_value

        if num_months > 1:
            total_change += change

        if change > max_increase_profit:
            max_increase_date = row[0]
            max_increase_profit = change
        
        if change < max_decrease_profit:
            max_decrease_date = row[0]
            max_decrease_profit = change

    avg_change = total_change /(num_months-1)

# Set output file
output_file = os.path.join('Financial_Analysis.txt')

# Open ouptut file
with open(output_file, 'w') as data:
    writer = csv.writer(data, delimiter='\n')
    writer.writerow(["Financial Analysis",
                "-" * 30, 
                f"Total Months: {num_months}",
                f"Total: ${profit_total}",
                f"Average Change: ${avg_change}",
                f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease_profit})",
                f"Greatest Increase in Profits: {max_increase_date} (${max_increase_profit})",
                ])

with open(output_file, 'r') as dataprint:
    print_data = csv.reader(dataprint, delimiter='\n')
    print('\n')
    for line in print_data:
        print(line[0])
    print('\n')