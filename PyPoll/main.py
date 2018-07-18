# Dependencies and import csv file
import os
import csv

file_to_load = os.path.join("PyPoll","election_data.csv")


csvpath = "election_data.csv"
with open(csvpath, 'r', newline = '') as csvfile:
    csv_reader = csv.reader(csvfile)

# variables
vc = 0
candidates = {}
candidatespercent = {}
winner = ""
countofwinner = 0

# read that file
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)

    # total vote count and single vote counts
    for row in csvreader:
        vc += 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

# candidate percentages 
for key, value in candidates.items():
    candidatespercent[key] = round((value/vc) * 100, 2)

#  loop to find the winner
for key in candidates.keys():
    if candidates[key] > countofwinner:
        winner = key
        countofwinner = candidates[key]


print("Election Results")
print("-------------------------------------")

print("Total Votes: " + str(vc))
print("-------------------------------------")


for key, value in candidates.items():
    print(key + ": " + str(candidatespercent[key]) + "% (" + str(value) + ")")

print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")


createnewfile = open("PollingResults.txt", "w")

createnewfile.write("Election Results \n")
createnewfile.write("------------------------------------- \n")
createnewfile.write("Total Votes: " + str(vc) + "\n")
createnewfile.write("------------------------------------- \n")
for key, value in candidates.items():
    createnewfile.write(key + ": " + str(candidatespercent[key]) + "% (" + str(value) + ") \n")
createnewfile.write("------------------------------------- \n")
createnewfile.write("Winner: " + winner + "\n")
createnewfile.write("------------------------------------- \n")