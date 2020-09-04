# dependencies 
import os
import csv

path_1 = os.path.join("Resources", "election_data.csv")

voter_id = []
candidates = []
unique_candidate = []
vote_count = []
vote_percent = []

with open(path_1, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    csv_header = next(csv_reader)
        
    for row in csv_reader:
        voter_id.append(row[0])
        candidates.append(row[2])
        
# total number of votes        
        count_votes = len(voter_id)  
    
# vote_count per candidate and vote_percent per candidate        
    for candidate in set(candidates):
        unique_candidate.append(candidate)
        # x is total number of votes per candidate
        x = candidates.count(candidate)
        vote_count.append(x)
        # y is percent of total votes per candidate
        y = (x/count_votes)*100
        vote_percent.append(y)
                
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

# print analysis to text file
path_2 = os.path.join("Analysis", "results.txt")
with open(path_2, "w+") as textfile:
    print(f"Election Results", file = textfile)
    print(f"--------------------------", file = textfile)
    print(f"Total Votes: {count_votes}", file = textfile)
    print(f"--------------------------", file = textfile)

    for i in range(len(unique_candidate)):
        print(f"{unique_candidate[i]}: {(vote_percent[i]):.3f}% ({vote_count[i]})", file = textfile)
    
    print(f"--------------------------", file = textfile)
    print(f"Winner: {winner}", file = textfile)
    print(f"--------------------------", file = textfile)
