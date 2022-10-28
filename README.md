# PyPoll Election Audit Analysis

## Overview of Election Audit
The purpose of this analysis is to complete the following tasks assigned by Tom, a Colorado Board of Elections employee. The data we will be analyzing is an election audit of tabulated results from a US Congressional precinct in Colorado.

1. Calculate the total number of votes cast.
2. Calculate the vote count & percentage of votes of each county in the precinct.
3. Determine the county with the highest vote count turnout.
4. Calculate the total number of votes each candidate received.
5. Calculate the percentage of votes each candidate won.
6. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.72.2

## Election-Audit Results
The election analysis shows that:
* ![image](https://user-images.githubusercontent.com/107401667/198390835-4ac3acfc-f919-4652-9635-3aa01498301b.png) There were 369,711 votes cast in this congressional election.
* ![image](https://user-images.githubusercontent.com/107401667/198390996-0da7dd32-e0ab-4f84-8d3c-11c28590bd92.png) Jefferson county received 10.5% of the votes, which equals 38,855 votes. Denver county received 82.8% of the votes, which equals 306,055 votes. Arapahoe county received 6.7% of the votes, which equals 24,801 votes.
* ![image](https://user-images.githubusercontent.com/107401667/198391467-136b45dd-23ab-4ab1-8ea5-42613066463c.png) Based off the percent of total votes for each county, Denver had the largest county turnout.
* ![image](https://user-images.githubusercontent.com/107401667/198392044-af034bd3-6e28-4954-945f-e07fbb2592e1.png) Candidate Charles Casper Stockham received 23% of the vote and 85,213 number of votes. Candidate Diana DeGette received 73.8% of the vote and 272,892 number of votes. Candidate Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
* ![image](https://user-images.githubusercontent.com/107401667/198392265-d9fbef0b-39b6-470c-8067-a62d20e0a9a0.png) Candidate Diana DeGette, who received 73.8% of the vote and 272,892 number of votes, won the election.

## Election-Audit Summary
After modifying the script, it can be used to compare this precinct's number total number of votes to other precincts' total number of votes. The first modification is creating a new spreadsheet on the CSV with all of Colorado's precincts and their total number of votes. The second modification is loading this file to the script and using a for loop to measure which precinct has the largest total number of votes.
