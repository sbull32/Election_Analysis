counties = ["Denver","Arapahoe","Jefferson"]
counties

counties_tuple= ('Arapahoe','Denver','Jefferson')
len(counties_tuple)

counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

if counties[1] == 'Denver':
    print(counties[1])