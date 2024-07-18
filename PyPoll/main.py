import csv
import os

# Path to the election data CSV file
csv_folder = "resources"  # Assuming the CSV is in a 'resources' folder
election_data_csv = os.path.join(csv_folder, "election_data.csv")

# Initialize variables
total_votes = 0
candidate_votes = {}
candidates = []
winner = ""
winner_votes = 0

# Read the election data CSV file
with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header row
    next(csvreader)

    # Iterate through each row in the CSV
    for row in csvreader:
        # Skip empty rows or rows that don't have enough columns
        if len(row) < 3:
            continue
        
        # Count total number of votes
        total_votes += 1

        # Track votes for each candidate
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
            candidates.append(candidate)  # Track unique candidates

# Determine the winner based on popular vote
for candidate, votes in candidate_votes.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Calculate the percentage of votes each candidate won
candidate_percentages = {}
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    candidate_percentages[candidate] = round(percentage, 3)

# Generate the output summary
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

for candidate in candidates:
    output += f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n"

output += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

# Print the output to the terminal
print(output)

# Write the output to a text file
output_file = os.path.join(".", "election_results.txt")
with open(output_file, "w") as txt_file:
    txt_file.write(output)

print(f"Results have been exported to: {output_file}")
