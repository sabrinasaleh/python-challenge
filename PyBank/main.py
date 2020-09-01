# dependencies 
import os
import csv

path = os.path.join("Resources", "budget_data.csv")

with open(path, "r") as file:
    csv_reader = csv.reader(file)
    csv_header = next(csv_reader)

months = []
profit_loss = []
change_profit_loss = []

    # get the column-data of months & profit_loss
    for row in csv_reader:
        months.append(row[0])
        profit_loss.append(row[1])
        
    # get the column-data of change_profit_loss
    for i in range(len(profit_loss) - 1):
        monthly_change = int(profit_loss[i+1]) - int(profit_loss[i])
        change_profit_loss.append(monthly_change)
        
    # calculate count_months 
        count_months = len(months)
        
    # calculate total_profit_loss        
        profit_loss_int = map(int, profit_loss)
        total_profit_loss = sum(profit_loss_int)       
        
    # calculate average_change
        average_change = round(sum(change_profit_loss)/len(change_profit_loss), 2)
        
    # calculate greatest_increase & greatest_decrease
        greatest_increase = max(change_profit_loss)
        greatest_decrease = min(change_profit_loss) 
        
    # get index for month_increase & month_decrease
        index_increase = change_profit_loss.index(max(change_profit_loss))+1
        month_increase = months[index_increase]
        index_decrease = change_profit_loss.index(min(change_profit_loss))+1 
        month_decrease = months[index_decrease]

output = ( 
    f"\nFinancial Analysis\n"
    f"-----------------------------\n"
    f"Total Months: {count_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {month_increase} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})\n"
    )
    
print(output)

        
                
       