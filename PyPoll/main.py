
# I: Import modules os and csv.

import os
import csv

# II: Set  path for the reference .csv file in 'poll_data_csv'.

os.chdir(os.path.dirname(__file__))
poll_data_csv = os.path.join("Resources","election_data.csv")

# III: Create lists to store data.

count = 0
candidate_list = []
candidate = []
votes = []
vote_percent = []

# IV: Open 'poll_data_csv' and perform calculations.

with open(poll_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Ask
    for row in csvreader:
        # Count total votes
        count = count + 1
        # Append candidate names to candidate_list
        candidate_list.append(row[2])
        # Set candidatelist for unique candidate names
    for x in set(candidate_list):
        candidate.append(x)
        # y = total number of votes/candidate
        y = candidate_list.count(x)
        votes.append(y)
        # z = % of total votes/candidate
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(votes)
    winrar = candidate[votes.index(winning_vote_count)]

# Printing time.

print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(candidate)):
            print(candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(votes[i])+ ")")
print("-------------------------")
print("The winner is: " + winrar)
print("-------------------------")

# Output as a .txt.

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(candidate))):
        text.write(candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(votes[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winrar + "\n")
    text.write("---------------------------------------\n")