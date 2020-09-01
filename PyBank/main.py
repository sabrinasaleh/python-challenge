# dependencies 
import os
import csv

path = os.path.join("Resources", "budget_data.csv")

months = []
profit_loss = []
change_profit_loss = []


with open(path, "r") as file:
    csv_reader = csv.reader(file)
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        months.append(row[0])
        profit_loss.append(row[1])
        
    for i in range(len(profit_loss) - 1):
        monthly_change = int(profit_loss[i+1]) - int(profit_loss[i])
        change_profit_loss.append(monthly_change)
        
    # total_months 
        count_months = len(months)
        
    # total_profit_loss        
        profit_loss_int = map(int, profit_loss)
        net_profit_loss = sum(profit_loss_int)  
        
     # average_change
        average_change = sum(change_profit_loss)/len(change_profit_loss)
        
    # greatest_increase & greatest_decrease
        greatest_increase = max(change_profit_loss)
        greatest_decrease = min(change_profit_loss) 
        
                
output = ( 
    f"\nFinancial Analysis\n"
    f"---------------------------\n"
    f"Total Months: {count_months}\n"
    f"Total: ${net_profit_loss}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: ${greatest_increase}\n"
    f"Greatest Decrease in Profits: ${greatest_decrease}\n"
    )
    

print(output)

        
                
       