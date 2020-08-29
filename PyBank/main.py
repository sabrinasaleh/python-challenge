# dependencies 
import os
import csv

path = os.path.join("..", "Resources", "budget_data.csv")

months = []
profit_losses = []
average_changes = []
greatest_increase = []
greatest_decrease = []

with open(path, "r") as file:
    csv_reader = csv.reader(file)
    
    for row in csv_reader:
        months.append(row[0])
        profit_losses.append(row[1])
        
        # I need to do calculations on these
        average_changes.append(row[SUBSCRIBER_COUNT_IDX])
        num_reviews.append(row[NUMER_OF_REVIEWS_IDX])