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

#variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
#file_to_load = os.path.join("Resources","election_results.csv'")
# Open the election results and read the file.
election_data =open(file_to_load, 'r')
#with open(file_to_load) as election_data:
# Perform Analysis
 #print(election_data)
# Close the file
#election_data.close()
#Create a filename variable to a direct or indirect path to the file
#file_to_save = 'analysis/election_analysis.txt'
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Use the open statement to open the file as a text file
outfile =open(file_to_save, "w")
with open(file_to_save, "w") as txt_file:
 #Write some data to the file
 #outfile.write("Hello World")
#  txt_file.write("Hello World ")
#  txt_file.write("Arapahoe, ")
#  txt_file.write("Denver, ")
#  txt_file.write("Jefferson.")
#  txt_file.write("Arapahoe, Denver, Jefferson.")
 txt_file.write("Counties in the Election")
 txt_file.write("\n--------------------------------")
 txt_file.write("\nArapahoe\nDenver\nJefferson")
# close the file
outfile.close()


#Read data
#variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
election_data =open(file_to_load, 'r')
# Read the file object with the reader function
file_reader = csv.reader(election_data)
#Print each row in the CSV file
# for row in file_reader:
    #print(row)
   #print(row[0])
# Read and print the header row
headers = next(file_reader)
print(headers)
