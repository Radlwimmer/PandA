# Exercise 5: APIs and IR
# Elisabeth Orion & Irene Radlwimmer WS 2023/34

import requests
import json
from CLASS_Sonnet import Sonnet
from CLASS_Index import Index
from CLASS_Query import Query
# from CLASS_Document import Document

# convert the file & create a dictionary
sonnets_collection = requests.get('https://poetrydb.org/author,title/Shakespeare;Sonnet')
json_data = sonnets_collection.text
sonnet_dict_list = json.loads(json_data)

sonnet_inst_list = []
for sonnet_dict in sonnet_dict_list:  # loop through the json-file/ list of dictionaries (sonnet_dict_list)
    # extract and store the data of all sonnets into a new list (sonnet_inst_list)
    sonnet_instance = Sonnet(sonnet_dict['title'], sonnet_dict['lines'])
    sonnet_inst_list.append(sonnet_instance)

index = Index(sonnet_inst_list)  # Build the index

while True:
    user_query = input("Search for sonnets ('q' to quit): ")
    if user_query == "q":
        print("Search ended.")
        break
    query = Query(user_query)
    matching_sonnets = index.search(query)  # Search the index with the query
    # Print the results
    print(f"Your search for {user_query} matched {len(matching_sonnets)} sonnets (", ", ".join(str(sonnet.id) for sonnet in matching_sonnets), "): ")
    for sonnet in matching_sonnets:
        print(sonnet)
