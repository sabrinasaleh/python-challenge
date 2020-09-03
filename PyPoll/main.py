# dependencies 
import os
import csv

path_1 = os.path.join("Resources", "election_data.csv")

votes = []
candidates = []
unique_candidate = []
vote_count = []
vote_percent = []


with open(path_1, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    csv_header = next(csv_reader)
        
    for row in csv_reader:
        votes.append(row[0])
        candidates.append(row[2])
        
# total number of votes        
        count_votes = len(votes)        
        
    for x in set(candidates):
        unique_candidate.append(x)
        # y is the total number of votes per candidate
        y = candidates.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y/count_votes)*100
        vote_percent.append(z)
        
# get index for winner        
    winner = unique_candidate[vote_count.index(max(vote_count))]
        
      
    

print(f"Election Results")
print(f"--------------------------")
print(f"Total Votes: {count_votes}")
print(f"--------------------------")

for i in range(len(unique_candidate)):
    print(f"{unique_candidate[i]}: {(vote_percent[i]):.3f}% ({vote_count[i]})")
    
print(f"--------------------------")
print(f"Winner: {winner}")
print(f"--------------------------")
   