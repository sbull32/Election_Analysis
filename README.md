# **Election Analysis**
*Module 3 Challenge*

## Overview of Election Audit

The purpose of this election audit is to analyze a specific election's data to determine the election's candidates, the counties where the election is taking place, and the final results of the election including the winning candidate and which county had the highest vote turnout.

## Election-Audit Results

1. There were 369,711 total votes cast in this election
2. Vote Breakdown by County
   * Arapahoe County: 24,801 votes (6.7% of total)
   * Denver County: 306,055 votes (82.8% of total)
   * Jefferson County: 38,855 votes (10.5% of total)
3. Denver County had the largest number of total votes with 306,055 votes cast (82.8% of total votes)
4. Vote Breakdown by Candidate
   * Charles Casper Stockham: 85,213 votes (23% of total)
   * Diana DeGette: 272,892 votes (73.8% of total)
   * Raymon Anthony Doane: 11,606 votes (3.1% of total)
5. The winning candidate in this election was **Diana DeGette** who recieved **272,892 votes** which was **73.8% of the total vote count.**

I have included a link to the image of the election analysis output describing the data ablove
![Election Analysis Terminal Output](c:/Users/seanb/OneDrive/Documents/Data Analytics Bootcamp/Module 3/Election Analysis/Analysis/Election Analysis Terminal Output.png)

## Election-Audit Summary

The script we ran to analyze this election's results can be modified to be used in future elections. As long as we provide the link to a specified data file (for this assignment it was the election_results.csv) and the file contains the same information presented in the same format (Ballot ID, County, Candidate Name) this exact code could be used to determine the winner of an election anywhere. For example, if there was another election in the Colorado Springs region, and the election results were stored in the same type of csv file structure, we could simply subsitute the file assigned to the variable Electon_Data to be the new election results file. By doing this we would be able to run the exact same analysis on a new set of election results. In addition, if the election results had additional data (such as house district, voter's registered party, tax class, etc.) we could simply use the code we wrote for our county and candidate breakdowns to analyze these new pieces of information. All we would need to do is create new variables to be substituted in the previous code's equations to define and display the new summarized information. Overall this code can be used to sumarize any election which stores its data in a csv file using a similar structire as this election's results.
