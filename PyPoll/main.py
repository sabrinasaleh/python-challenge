# dependencies 
import os
import csv

path_1 = os.path.join("Resources", "election_data.csv")

votes = []
# candidate_list = []
# percent_votes = []
# number_votes = []
# winner = []

with open(path_1, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    csv_header = next(csv_reader)
        
    for row in csv_reader:
        votes.append(row[0])
        count_votes = len(votes)
        
      
    
output = ( 
    f"Election Results\n"
    f"-----------------------------\n"
    f"Total Votes: {count_votes}\n"
#     f"-----------------------------\n"
#     f"Khan: {}\n"
#     f"Correy: {}\n"
#     f"Li: {}\n"
#     f"O'Tooley: {}\n"
#     f"-----------------------------\n"
#     f"Winner: {}\n"
#     f"-----------------------------\n"
    )
 
print(output)
