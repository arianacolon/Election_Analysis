# Decision Statements
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
        print(counties[1])
# In Python, we can access the items in a list using an index
# Membership Operators
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
#Membership and Logical Operations
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
#Iterate Through Lists and Tuples
for i in range(len(counties)):
    print(counties[i])
#Iterate Through a Dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)
#Three Ways to Get Values in a Dictionary
for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

#Get the Key-Value Pairs of a Dictionary
for county, voters in counties_dict.items():
    print(county, voters)
#Get Each Dictionary in a List of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)
#Use range() fucntion to iterate over the list of dictionaries and print counties in voting_data
for i in range(len(voting_data)):
      print(voting_data[i]['county'])
#Get the Values from a List of Dictionaries - Use a Nested Loop
for county_dict in voting_data: #Retrieve each Dictionary
    for value in county_dict.values(): #Reference the Data to Get Each Loop
        print(value)
#Retrive # of Registered Voters from Each Dictionary
for county_dict in voting_data:
     print(county_dict['registered_voters'])

#Using F-Strings with Dictionaries
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
#Multiline F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)

#Datetime Module to Get Today's Date:
import datetime as dt # Import the datetime class from the datetime module.
now = dt.datetime.now() # Use the now() attribute on the datetime class to get the present time.
print("The time right now is ", now) # Print the present time.