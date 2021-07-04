# The data we need to retrieve
import csv
import os

# Assign a variable to load a file from a path.
Election_Data= os.path.join('Resources','election_results.csv')

# Assign a variable to save the file to a path.
Election_Analysis = os.path.join('Analysis','election_analysis.txt')

# Open the election results and read the file. 
with open(Election_Data) as election_data:
    file_reader = csv.reader(election_data)

    # Reade and print the header row.
    headers = next(file_reader)
    print(headers)
    # To do: perform analysis.
    # 1) Total number of votes cast
    # 2) Complete list of canidates who received votes
    # 3) Total number of votes each canidate won
    # 4) Percentage of votes each canidate won
    # 5) Winner of the election based on popular vote
# Close the file.

