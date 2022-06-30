from enum import unique
import os
import csv

electiondataCSV = os.path.join("python-challenge/PyPoll","Resources","election_data.csv")
outputfile = os.path.join("python-challenge/PyPoll","analysis","PyPoll_analysis.txt")

totalvotes = 0
candidates = []
candidatevotes = {}
winningcount = 0
winningcandidate = ""

with open(electiondataCSV,"r", encoding="utf-8") as sourcefile:
    csvreader = csv.reader(sourcefile)
    header = next(csvreader)
    
    for row in csvreader:
        totalvotes +=1
        
        #check to see if the candidate is in the list of candidates
        if row[2] not in candidates:
            #if it is not in the list, add the candidate
            candidates.append(row[2])
            #add the value to the dictionary as well
            #{"key":value}
            #start the count at 1 for votes
            candidatevotes[row[2]] = 1

        else:
            #the candidate is in the list of candidates
            #add a vote to the condidate's count
            candidatevotes[row[2]] += 1

voteoutput = ""
for candidate in candidatevotes:
    #get the vote count and the percentage of the votes
    votes = candidatevotes.get(candidate)
    votePct = (float(votes)/ float(totalvotes))* 100.00

    voteoutput += f"{candidate}: {votePct:.3f}% ({votes})\n"

    #compare the votes to the winning count
    if votes > winningcount:
        winningcount = votes
        winningcandidate = candidate


output=(
    f"Election Results\n"
    f"-----------------------------\n"
    f"Total Votes: {totalvotes}\n"
    f"-----------------------------\n"
    f"{voteoutput}"
    f"-----------------------------\n"
    f"Winner: {winningcandidate}\n"
    f"-----------------------------"
)

with open(outputfile,"w") as textfile:
    textfile.write(output)

print(output)