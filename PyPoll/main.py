import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join("PyPoll", "Resources", "election_data.csv")
with open(election_data, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    # checking retrieved data
    # for row in csvreader:
    # print(row)
    # print headers

    header = next(csvreader)
    # print("header:", header)

    # Variables
    total_votes = 0
    candidate_list_with_votes = {}
    # total votes
    for row in csvreader:
        total_votes += 1

        # candidate list and votes count
        if row[2] in candidate_list_with_votes:
            candidate_list_with_votes[row[2]] += 1
        else:
            candidate_list_with_votes[row[2]] = 1
    # percentage of vote
    percentage_votes = {}
    for candidate, votes in candidate_list_with_votes.items():
        percent_votes = (votes / total_votes) * 100
        percentage_votes[candidate] = round(percent_votes, 3)

    # the winner
    winner = max(candidate_list_with_votes, key=candidate_list_with_votes.get)

result = []
# prints
result.append("Election Results")
result.append("-" * 30)
result.append(f"Total Votes: {total_votes}")
result.append("-" * 30)
# print list of candidates with votes and percentages
for candidate, votes in candidate_list_with_votes.items():
    result.append(f"{candidate}: {percentage_votes[candidate]}% ({votes})")
result.append("-" * 30)
result.append(f"Winner: {winner}")
result.append("-" * 30)

# output to a text file
output_file = os.path.join("PyPoll", "Analysis", "election_results.txt")
with open(output_file, "w") as file:
    for line in result:
        print(line)
        file.write(line + "\n")
