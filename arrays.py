###Arrays in python - Lists

cities = ["New York","Moscow","Kiev","Poznan","Zaporozhye" ]

print(cities)
print(len(cities))

for element in cities:
    print(element)

cities.append("Odessa")###append - will append element to the end of list
cities.insert(0,"Minsk")###insert - will insert element to some pos of the list
print(cities)

del cities[-1] ###will delete element by index
print(cities)

cities.remove("Kiev")
cities.sort()#sort array by alphabet
print(cities)




