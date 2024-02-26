# import the os module
import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

# open the csv file
with open(budget_data, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # print all csv document
    header = next(csvreader)

    # The variables
    count_total_months = 0
    count_totalprofit_losses = 0
    change_profit_losses = []
    previous_profit_losses = 0
    avg_change_profit_losses = 0
    # the dic for the greatest increase and decrease, faster mapping of the values
    greatest_increase = {"date": "", "amount": 0}
    greatest_decrease = {"date": "", "amount": 0}

    # total amount of months
    for row in csvreader:
        count_total_months += 1  # starts at 0

        # total profit losses
        count_totalprofit_losses += int(row[1])

        # change in profit/losses
        if previous_profit_losses != 0:
            change_profit_losses.append({"date": row[0], "amount": int(row[1]) - previous_profit_losses})

        previous_profit_losses = int(row[1])

    # Greatest increase in profits (date and amount)
    for i in range(1, len(change_profit_losses)):
        if change_profit_losses[i]["amount"] > greatest_increase["amount"]:

            greatest_increase = change_profit_losses[i]
            # Greatest decrease in losses (date and amount)
        if change_profit_losses[i]["amount"] < greatest_decrease["amount"]:
            greatest_decrease = change_profit_losses[i]
    # avg change in profit/losses
    avg_change_profit_losses = round(sum(change["amount"] for change in change_profit_losses) / len(change_profit_losses), 2)

    result = []

    # prints
    result.append("Financial Analysis")
    result.append("----------------------------")
    result.append(f"Total Months: {count_total_months}")
    result.append(f"Total: ${count_totalprofit_losses}")
    result.append(f"Average Change: ${avg_change_profit_losses}")
    result.append(f'Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["amount"]})')
    result.append(f'Greatest Decrease in Losses: {greatest_decrease["date"]} (${greatest_decrease["amount"]})')

    # output to a text file
    output_file = os.path.join("PyBank", "Analysis", "financial_analysis.txt")
    with open(output_file, "w") as file:
        for line in result:
            print(line)
            file.write(line + "\n")
