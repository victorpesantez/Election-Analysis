# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("..", "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
###VPC##county list.-Initialize a county list, like the candidate_options list, that will hold the names of the counties.
candidate_options = ["Arapahoe","Denver","Jefferson"]
candidate_options
###VPC## county votes dictionary.-Initialize a dictionary, like the candidate_votes dictionary, that will hold the county as the key and the votes cast for each county as the values.
candidaste_votes = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
###Initialize an empty string, like winning_candidate, that will hold the county name for the county with the largest turnout.
###Initialize a variable, like the winning_count variable, that will hold the number of votes of the county that had the largest turnout.
largest_turnout = ""
county_turnout = 0
turnout_percentage = 0


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        #####While reading the election results from each row inside the for loop, write a script that gets the county name from each row.
        county_name = row[2]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.

            # 4b: Add the existing county to the list of counties.

            # 4c: Begin tracking the county's vote count.

   






