travel_log = [
{
"country" : "France",
"visits" : 12,
"cities" : ["marseille","dijon","brest"]
},
{
"country" : "spain",
"visits" : 7,
"cities" : ["madrid","barcelona","alicant"]
},
]
# this one adds a whole country you've never been in.
def add_country (country,visits,cities):
    travel_log.append({
        "country" : country,
        "visits" : visits,
        "cities" : cities,
    })
#this one adds one visit and the name of the city you've been!
#if it can't find the country, it will use the previous function to 
#add it, with 1 visits, and the name of the city in a list.
def add_city (country,city):
    for _ in range(len(travel_log)):
        if travel_log[_]["country"] == country:
            travel_log[_]["visits"] += 1
            if travel_log[_]["cities"].count(city) == 0:
                travel_log[_]["cities"].append(city)
                return
    add_country(country,1,[city])


add_country("germany",5,["hamburg","berlin","kiel"])
print(travel_log[2])
add_city("germany","algeria")
add_city("germany","algeria")
add_city("USA","texas")

print(travel_log)

