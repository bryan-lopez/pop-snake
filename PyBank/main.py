###    PyBank/main.py    ###

## Imports ##
import os
import csv
from statistics import mean

# Opening the csv: budget_data.csv

budget_path = os.path.join("./", "Resources/", "budget_data.csv")

with open(budget_path) as budget_file:

    # open file as csv with csv.reader
    budget_csv = csv.reader(budget_file)

    header = next(budget_csv) # Header = [Month, Profit/Losses]
    # print(f"[{header[0]},{header[1]}]")

    # Month Fomat = MMM-YYYY
    # Profit/Lossess = NUMBER

    # Store data for use later
    dates = []
    profits =[]
    for info in budget_csv:
        dates.append(info[0])
        profits.append(int(info[1]))

    # print(dates[0], profits[0])
    # Close csv and file

## Financial Analysis ##

tot_months = len(dates)
tot_profits = sum(profits)

change = [profits[i] - profits[i-1] for i in range(1, tot_months)]
avg_change = mean(change)

max_change = max(change)
max_index = change.index(max_change)
min_change = min(change)
min_index = change.index(min_change)

## Presentation ##

print("Financial Analysis\n",
    "-----------------------------------------\n",
    f"Total Months: {tot_months}\n",
    f"Total Profits: {tot_profits}\n",
    f"Average Change: ${avg_change: .2f}\n",
    f"Greatest Increase in Profits: {dates[max_index + 1]} (${max_change})\n",
    f"Greatest Decrease in Profits: {dates[min_index + 1]} (${min_change})\n")

## Save Results.txt File ##

results_path = os.path.join("./", "results.txt")

with open(results_path, "w+") as r:
    r.write("Financial Analysis\n")
    r.write("-----------------------------------------\n")
    r.write(f"Total Months: {tot_months}\n")
    r.write(f"Total Profits: {tot_profits}\n")
    r.write(f"Average Change: ${avg_change: .2f}\n")
    r.write(f"Greatest Increase in Profits: {dates[max_index + 1]} (${max_change})\n")
    r.write(f"Greatest Decrease in Profits: {dates[min_index + 1]} (${min_change})\n")
