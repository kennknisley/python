import os
import csv

#import the file
vote_csv=os.path.join('Resources', 'election_data.csv')
file_to_output=os.path.join('Analysis', 'election_analysis.txt')

#list for total votes, canidates, percent of votes, and number of votes per candidate
total_votes = 0

candidates = []

precent_votes = []

candidate_votes = {}

winning_candidate = ""

winning_vote_count = 0

#read the csv
with open(vote_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)

#add to total count
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

#for new candidate, add their name to our list and start an index for them
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0 

#for listed candidates, add to their index            
        candidate_votes[candidate_name] += 1

with open(file_to_output, "w") as txt_file:
    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)

#Total votes
# print("Final Election Results")
# print(f"Total Votes: {str(total_votes)}")

#calculate percentages
for candidate in candidate_votes:
    votes=candidate_votes.get(candidate)
    vote_percentage = float(votes)/float(total_votes) * 100
    if (votes>winning_vote_count):
        winning_vote_count = votes
        winning_candidate = candidate

    # Print each candidate's voter count and percentage (to terminal)
    voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
    print(voter_output, end="")
    # Save each candidate's voter count and percentage to text file
    txt_file.write(voter_output)

winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
print(winning_candidate_summary)
# Save the winning candidate's name to the text file
txt_file.write(winning_candidate_summary)

#Results
#     print(f"Candidate {candidate}: Votes {votes}: Percentage {vote_precentage:.3f}%")
# print(f"Winner {winning_candidate}")    



