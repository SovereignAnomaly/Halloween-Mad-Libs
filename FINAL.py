title = "Halloween Mad Libs"
date = 2021
print("Fill in the blanks to match the category and see what silly story you could put together.")
print("At the end, the story will come together and you can read your master piece!!")

list = ["Place = ", "Adjective = ", "Noun = ", "Color = ", "Animal = ", "Verb = ", "Plural Noun = "]


class Alpha:
    x = "Yesterdays"

Day1 = Alpha()

class Beta:
    x = "Todays"

Day2 = Beta()

class Charlie:
    x = "Tomorrows"

Day3 = Charlie()


print(title, "  ", date)

print("This year __________ is having a ___________ Halloween Costume Contest.")
first = input(list[0])
second = input(list[1])
print("I'm going to dress up as a _________ _________.")
third = input(list[1])
fourth = input(list[2])
print("My best friend is going to be a _________ ___________ __________....")
fifth = input(list[1])
sixth = input(list[3])
seventh = input(list[4])
print("and my cousin is going to be a _________ __________.")
eighth = input(list[1])
ninth = input(list[2])
print("They have a _________ party and everyone in town shows up to __________ all of the ___________ costumes.")
tenth = input(list[1])
eleventh = input(list[5])
twelve = input(list[1])
print("We play games, like bobbing for apples and __________ ___________ and it is so much fun!!")
thirteenth = input(list[5])
fourteenth = input(list[6])

print("This year", first, "is having a", second, "Halloween Costume Contest.")
print("I'm going to dress up as a", third, fourth, ".")
print("My best friend is going to be a", fifth, sixth, seventh, "......")
print("and my cousin is going to be a", eighth, ninth, ".")
print("They have a", tenth, "party and everyone in town shows up to", eleventh, "all of the", twelve, "costumes.")
print("We play games, like bobbing for apples and", thirteenth, fourteenth, "and it is so much fun!!")


print("Try", Day1.x, "Reading!")
print("Take a sneak peak at", Day3.x, "Reading!")