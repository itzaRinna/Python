lucky_number = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Mike", "Jim", "Oscar", "Toby"]
friends_1 = friends.copy()
#1
lucky_number.reverse()
print(lucky_number)
#2
friends.sort()
print(friends)
#3
friends.extend(lucky_number) #add two lists together
print(friends)
#4
friends_1.append("Creed")
print(friends_1)
#5
friends_1.insert(1, "Kelly")
print(friends_1)
#6
friends.remove("Jim")
print(friends)
#7
friends_1.pop()
print(friends_1)
#8
print(friends.index("Mike"))
#9
print(friends.count("Mike"))
