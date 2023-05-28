# my_list = [1, 2, 3]
#
# my_list = [item+1 for item in my_list]
# print(my_list)


# my_list = [n*2 for n in range(1,5) if (n*2 % 6 != 0)]
# print(my_list)

# names = ["ali", "megha", "angela", "satina"]
# names = [name.upper() for name in names if len(name) > 4]
# print(names)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n**2 for n in numbers]
# print(squared_numbers)
# even_numbers = [n for n in numbers if n%2 == 0]
# print(even_numbers)

# file_1 = open("file1.txt")
# list1 = file_1.readlines()
# list1 = [int(number[0]) for number in list1]
# file_2 = open("file2.txt")
# list2 = file_2.readlines()
# list2 = [int(number[0]) for number in list2]
#
# list3 = [number for number in list1 if number in list2]
# print(list1)
# print(list2)
# print(list3)

# import random
# names = ["alex","sam","clover","john","mercury"]
# student_scores = {student:random.randint(1,100) for student in names}
# print(student_scores)
# passing_students = {student:score for (student,score) in student_scores.items() if score >= 50}
# print(passing_students)
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# sentence = sentence.split()
# sentences = {name:len(name) for name in sentence}
# print(sentences)
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day:((c_temp * 9 / 5) +32) for (day,c_temp) in weather_c.items()}

print(weather_f)