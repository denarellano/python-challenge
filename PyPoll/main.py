#create a Python script that analyzes the votes and calculates each of the following:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.


import os
import csv

election_data = os.path.join('election_data.csv')

total_votes = 0
num_votes = {}
candidates = []
percent_vote = 0
winnervalue = 0
winner = ''
candidate = ''

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)
    for row in csvreader:
        total_votes += 1

        candidates = row[2]

        if candidates in num_votes:
            num_votes[candidates] += 1
        else: 
            num_votes[candidates] = 1
        
    for k, v in num_votes.items():
        percent_vote = '{0:3f}%'.format((v/total_votes) * 100)
        candidate = k, (percent_vote), (v)

        if v > winnervalue:
            winnervalue = v
            winner = k

# Set output file
output_file = os.path.join('Election_Results.txt')

# Open ouptut file
with open(output_file, 'w') as data:
    writer = csv.writer(data, delimiter='\n')
    writer.writerow(["Election Results",
                "-" * 20, 
                f"Total Votes: {total_votes}",
                "-" * 20,
                f"{candidate}",
                "-" * 20,
                f"Winner: {winner}",
                "-" * 20,
                ])

with open(output_file, 'r') as dataprint:
    print_data = csv.reader(dataprint, delimiter='\n')
    print('\n')
    for line in print_data:
        print(line[0])
    print('\n')