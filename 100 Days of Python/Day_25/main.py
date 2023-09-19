# with open("226 weather_data.csv") as weather_data:
#     weather_list = weather_data.readlines()
#
# print(weather_list)
#
# import csv
# with open("226 weather_data.csv") as weather_data:
#     weather_list = csv.reader(weather_data)
#     temperatures = []
#     for row in weather_list:
#         if row[1] != "temp" :
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas
# data = pandas.read_csv("226 weather_data.csv")
# temp_list = data["temp"].to_list()
# print(round(sum(temp_list)/len(temp_list), 2))
# maxtemp_day = data[data.temp == data.temp.max()]
# print(maxtemp_day.condition)
#
# my_data = {
#     "days": [1, 2, 3, 4],
#     "happiness": [8, 7, 8, 9],
# }
# data = pandas.DataFrame(my_data)
# data.to_csv("new data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
count_gray = len(data[data["Primary Fur Color"] == "Gray"])
count_black = len(data[data["Primary Fur Color"] == "Black"])
count_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
color_table = {
    "Fur color": ["Gray", "Black", "Cinnamon"],
    "count": [count_gray, count_black, count_cinnamon],
}
color_data = pandas.DataFrame(color_table)
color_data.to_csv("Squirrel Fur color count.csv")
