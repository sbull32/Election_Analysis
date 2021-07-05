# The data we need to retrieve
import csv
import os
# Assign a variable to load a file from a path.
Election_Data= os.path.join('Resources','election_results.csv')
# Assign a variable to save the file to a path.
Election_Analysis = os.path.join('Analysis','election_analysis.txt')

# Initialize a total vote counter
total_votes = 0

# Declare candidate options and votes
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0

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
        
        # Save the results to text file
        with open(Election_Analysis, "w") as txt_file:
            
            # Print the final vote count to the terminal.
            election_results = (
                f"\nElection Results\n"
                f"-------------------------\n"
                f"Total Votes: {total_votes:,}\n"
                f"-------------------------\n")
            print(election_results, end="")
            
            # Save the final vote count to the text file.
            txt_file.write(election_results)
            
            # Determine percentage of votes each canidate won
            for candidate_name in candidate_votes:
                
                # Retrieve vote count and vote percentage for each candidate
                votes = candidate_votes[candidate_name]
                vote_percentage = round((float(votes) / float(total_votes) * 100),1)
                
                # Print results
                candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes})\n')
                #print(candidate_results)
                
                #  Save the candidate results to our text file.
                txt_file.write(candidate_results)
                
                # Determine winning vote count and candidate
                if (votes > winning_count) and (vote_percentage > winning_percentage):
                    winning_count = votes
                    winning_candidate = candidate_name
                    winning_percentage = vote_percentage     
            
            # Print Winning Candidate Summary
            winning_candidate_summary = (
                f'---------------------------\n'
                f'Winner: {winning_candidate}\n'
                f'Winning Vote Count: {winning_count:,}\n'
                f'Winning Percentage: {winning_percentage:.1f}%\n'
                f'---------------------------\n')
            #print(winning_candidate_summary)
            
            # Save the winning candidate's name to the text file.
            txt_file.write(winning_candidate_summary)
            
# Close the file
election_data.close()
