import csv
import os

# Create variables to get the current directory and the directory to which the output will be saved.
FILE_PATH_INPUT = os.path.join("Resources", "election_data.csv")
FILE_PATH_OUTPUT = os.path.join("analysis", "Results.txt")

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Establish variables
total_votes = 0 #Get the total number of votes
vote_counts = {} #Create a dictionary to hold candidates and number of votes
output = "" #Create a variable to hold output string
candidnate_results = "" #Create empty string for candidnate results

#Initialize csv file for reading
with open(FILE_PATH_INPUT) as csvfile:
    file_reader = csv.reader(csvfile, delimiter=",")
    next(file_reader) #Skip Header
    
    # Loop through each row in the CSV file
    for row in file_reader:
        
        #Increase number of votes by 1
        total_votes += 1 

        # Get the candidate name from the row
        candidate = row[2]

        # If the candidate has not been seen before, add them to the vote_counts dictionary
        if candidate not in vote_counts:
            vote_counts[candidate] = 0 #Add candidate key and set value to 0

        # Increment the candidate's vote count
        vote_counts[candidate] += 1

#Create a string with candidate, % results, total count results
for candidate, count in vote_counts.items():
    candidnate_results += (candidate + ": " + str(round(count/total_votes*100, 2)) + "%" + " (" + str(count)+")\n")

#Find winner by popular vote
winner = max(vote_counts, key = vote_counts.get)

#Create output text
output += "Election Results\n"
output += "-"*40+"\n"
output += "Total Votes: " + str(total_votes) + "\n"
output += "-"*40 + "\n"
output += candidnate_results
output += "-"*40 + "\n"
output += "Winner: " + str(winner) + "\n"
output += "-"*40

#Print output to screen
print(output)

#Create .txt file with output
with open(FILE_PATH_OUTPUT, "w") as results_file:
    results_file.write(output)