###dictionaries

human = {
    "sex": "Man",
    "height": 180,
    "hair": "black",
    "age": 25,
    "name": "Garik"
}

var = "salam_voram "

print(f"Andryuha {var}")

print(var + human["name"])
print(var + str(human["age"]))

human["GPU"] = "GTX 1660 Super"###to add new el to dict
del human["hair"]
print(human["GPU"])
print(human)

humans = []

for x in range(0,10):
    humans.append(human.copy())###to deep copy
    print(humans[x])

print("===============")
humans[4]["age"] = 20
print("===============")

for x in humans:
    print(x["name"])