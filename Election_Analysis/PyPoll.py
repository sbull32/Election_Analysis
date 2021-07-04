# The data we need to retrieve
import csv
import os
# Assign a variable to load a file from a path.
Election_Data= os.path.join('Resources','election_results.csv')
# Assign a variable to save the file to a path.
Election_Analysis = os.path.join('Analysis','election_analysis.txt')

# Initialize a total vote counter
total_votes = 0

# Declare a new list
candidate_options = []

# Declare an empty dictionary
candidate_votes = {}

# Open the election results and read the file. 
with open(Election_Data) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in CSV file
    for row in file_reader:
        
        # Add to the total vote count
        total_votes += 1
        
        # Print canidate name from each row
        candidate_name=row[2]
        
        # If candidate does not match any existing candidate, add canidate name to the canidate list and count their votes
        if candidate_name not in candidate_options:
            # Add candidate to list
            candidate_options.append(candidate_name)
            # Begin tracking candidate's vote count
            candidate_votes[candidate_name]= 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
            
# Print the candidate vote dictionary
print(candidate_votes)

# Determine percentage of votes each canidate won
for candidate_name in candidate_votes:
    # retrieve vote count for candidate
    votes = candidate_votes[candidate_name]
    # Calculate percentage of votes
    vote_percentage = round((float(votes) / float(total_votes) * 100),1)
    # Print results
    print(f'{candidate_name}: received {vote_percentage}% of the vote.')
    
    # 5) Winner of the election based on popular vote
# Close the file.

