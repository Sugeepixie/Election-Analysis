# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidates won
# 5. The winner of the election based on popular vote

# Add dependencies
import csv
from dataclasses import dataclass
import os

""" #variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
#file_to_load = os.path.join("Resources","election_results.csv'")
#Open the election results and read the file.
election_data =open(file_to_load, 'r')
#with open(file_to_load) as election_data:
#Perform Analysis
 #print(election_data)
#Close the file
election_data.close()
#Create a filename variable to a direct or indirect path to the file
file_to_save = 'analysis/election_analysis.txt'
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Use the open statement to open the file as a text file
outfile =open(file_to_save, "w")
with open(file_to_save, "w") as txt_file:
# Write some data to the file
#  outfile.write("Hello World")
#  txt_file.write("Hello World ")
#  txt_file.write("Arapahoe, ")
#  txt_file.write("Denver, ")
#  txt_file.write("Jefferson.")
#  txt_file.write("Arapahoe, Denver, Jefferson.")
 txt_file.write("Counties in the Election")
 txt_file.write("\n--------------------------------")
 txt_file.write("\nArapahoe\nDenver\nJefferson")
#close the file
outfile.close()
 """

#Read data
#variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
#Create a filename variable to save the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initialize vote counter
total_votes = 0
# set candidate list
candidate_options = []
#Declare the empty dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
election_data =open(file_to_load, 'r')
# Read the file object with the reader function
file_reader = csv.reader(election_data)
# Read and print the header row
headers = next(file_reader)
#print(headers)
#Print each row in the CSV file
for row in file_reader:   
# Add the total vote counts
    total_votes +=1
# Print candidate name
    candidate_name = row [2]

    if candidate_name not in candidate_options:
# Add the candidate name to the candidate list
       candidate_options.append(candidate_name)
       candidate_votes[candidate_name] = 0
# Add votes to the candidate count
    candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total votes: {total_votes:,}\n"
        f"--------------------------\n"
    )
    print (election_results, end="")
    # save the final vote count to text file
    txt_file.write(election_results)
    #print candidate vote dictionary
    print(candidate_votes)
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
    #Retrieve vote count of a candidate 
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #print candidate name and percentage of votes
        print(f"{candidate_name}: received {vote_percentage:.2f}% of the rate.")
    # Determine winning vote count, winning percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        candidate_results = (f"{candidate_name}:  {vote_percentage:.1f}% ({votes:,})\n")
# Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
#  Save the candidate results to our text file.
        txt_file.write(candidate_results)
# print the winning candidates' results to the terminal
    winning_candidate_summary = (
    f"-----------------------------\n"
    f" Winner: {winning_candidate}\n"
    f" Winning Vote Count: {winning_count:,}\n"
    f" Winning percentage: {winning_percentage:.1f}%\n"
    f"-----------------------------\n")  
    print(winning_candidate_summary)
# Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)

