### PyPoll/main.py ###

## Imports ##
import os
import csv


## CSV reading ##

# We will be using election_data.csv located in ./Resources/
election_path = os.path.join("./", "Resources/", "election_data.csv")

with open(election_path) as election_file:

    # Use csv.reader()
    election_csv = csv.reader(election_file)

    header = next(election_csv) # [Voter ID, County, Candidate]

    # Use dictionary to store values for {Candidate: vote count}

    tally = {}
    tot_votes = 0

    for vote in election_csv:
        candidate = vote[2]

        try:
            tally[candidate] += 1 # Try to update key
        except KeyError:
            tally.update({candidate: 1}) # Update with new candidate with 1 vote

        tot_votes += 1

## Analysis ##

winner = max(tally, key=(lambda can: tally[can]))
candidates = list(tally)
tally_percents = {can:(tally[can]/tot_votes) for can in tally}

## Presentation ##

print("Election Results\n",
    "----------------------------\n",
    f"Total votes: {tot_votes}\n",
    "----------------------------")
for can in candidates:
    print(f"{can}: {tally_percents[can]*100:.2f} ({tally[can]})")
print("----------------------------\n",
    f"Winner: {winner}\n",
    "----------------------------\n")
