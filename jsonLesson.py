###json manual

import json

filename = "user_settings.txt"
myfile = open(filename,mode="w",encoding="utf-8")

player1 = {
    "name": "Daniel",
    "score": 125,
    "ability": ["black_hole","fire_blast","tallon"]
}

player2 = {
    "name": "John",
    "score": 500,
    "ability": ["crime","fury","insane"]
}

""" Save by JSON to file """

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

json.dump(myplayers,myfile)### to pack data to user_settings.txt
myfile.close()

"""UPLOAD DATA FROM JSON"""

myfile = open(filename, mode="r", encoding="utf-8")
json_data = json.load(myfile)###to load data from JSON to json_data

for user in json_data:
    print(f"Player Name is: {user['name']}")