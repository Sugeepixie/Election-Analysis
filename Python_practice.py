# print ("Hello World")
# counties_dict = {}
# counties_dict["Arapahoe"] = 422829
# counties_dict["Denver"] = 463353
# counties_dict["Jefferson"] = 432438
# counties_dict 
# print(len(counties_dict))
# print(counties_dict.items())
# print (counties_dict.keys())
# print (counties_dict.values())
# print(counties_dict.get("Denver"))
# print(counties_dict["Arapahoe"])
# for voters in counties_dict.values():
#     print(voters) 
# for county, voters in counties_dict.items():
# #     print(county +" county has " + str(voters) +" registered voters.")

#  print (f"{county} county has {voters} registered voters.")


#list of dictionaries
voting_data = []
voting_data.append({"county" : "Arapahoe" , "registered_voters" : 422829})
voting_data.append({"county" : "Denver" , "registered_voters" : 463353})
voting_data.append({"county" : "Jefferson" , "registered_voters" : 432438})
# voting_data.insert(1,{"county": "El Paso", "registered_voters": 461149})

# voting_data.pop(0)

# voting_data[2] = {"county" : "Denver" , "registered_voters" : 463353}
# voting_data[1] = {"county" : "Jefferson" , "registered_voters" : 432438}
# voting_data.append({"county" : "Arapahoe" , "registered_voters" : 422829})


# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)
# for county_dict in voting_data:
#       for keys in county_dict.keys():
#         print(keys)


# for county_dict in voting_data:
#  print(county_dict)

# for i in range(len(voting_data)):
#     print (f"{voting_data[i]['county']} county has {voting_data[i]['registered_voters']} registered voters.")

for i in range(len(voting_data)):
    print (f"{voting_data[i]['county']}")

# decision statements
""" y_votes = int(input("How many votesdid u get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
calculate percentage
percantage_votes = (my_votes / total_votes)* 100
print ("I recieved " + str(percantage_votes) + " % of the toatal votes.") """


#IF 
""" counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1]) 
for county in counties:
    print(county)
for i in range(len(counties)):
    print(counties[i])
 """
#while 

""" count = 7

while count < 1:

    print("Hello World") """