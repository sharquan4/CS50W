print("-------------------single string--------------------")
phrase = "Joe Mama"
print(phrase[2])
print(phrase.index("J"))
print(phrase[1:3])
print(len(phrase))

print("-------------------num_list--------------------")
num = [1, 6, 2, 3, 9]
#sorts the numbers in order from least to greatest
num.sort()
print(num)
#reverse the numbers in order from greatest to least
num.reverse()
print(num)

print("-------------------list--------------------")
list = ["Bob", "Narley", "Boob", "Bob", "Sarah"]
#prints only 'Narley' and 'Boob'
print(list[1:3])
#prints the number of where 'Narley' is placed int he list
print(list.index("Narley"))
#prints the number of times of 'Bob' in the list
print(list.count("Bob"))
#adds an element to the list
list.append("Obama") # or list.add("Obama")
print(list)
#removes an element from the list
list.remove("Bob") # or list.discard("Bob")
print(list)
#this method deletes the element starting from the other end (-1) and can set up parameters
list.pop()
print(list)
list.pop(-2)
print(list)
#adds an element with parameter measures
list.insert(2, "Giselle")
print(list)
#check if a specific element is present in the list
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#replaces an element with another title
fruits[1] = "kiwi"
print(fruits[1])
#combine lists into one
fruits1 = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits1)

print("-----------------------------power-----------------------------")
print(pow(4,2))
print(4**2)

print("-----------------------------tuples-----------------------------")
#cannot be modified
coord = (4, 5)
print(coord[1])
coord[0:1]
print(coord)
coord2 = [(4,3), (2,3)]
print(coord2)
print(coord2[1])

print("-----------------------------dictionary-----------------------------")

dic = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    4: "April"
    }
print(dic["Mar"])
print(dic.get("Feb"))
print(dic.get("Joe"))
print(dic.get("Joe", "not a default key"))
print(dic.get(4))

print("-----------------------------for loop-----------------------------")
#prints out each letter of a string
name = "Alligator"
for letter in name:
    print(letter)
for letter in "poop":
    print(letter)
#prints out each element of the list
friends = ["Joe", "Bob", "Sarah"]
for friend in friends:
    print(friend)
#prints within parameters
for index in range(10):
    print(index)
#prints with a fixed parameter
for index in range(3,10):
    print(index)
#prints the length aka with a fixed parameter
for index in range(len(friends)):
    print(friends[index])
#prints with a fixed parameter
for index in range(4):
    if index == 0:
        print("p3n1s")
    else:
        print("pu$$y")
#2D list
joe = [2,4,5]
#3D list
joe_3d = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
    ]
print(joe_3d[0][0])
#prints rows of 3D list
for row in joe_3d:
    print(row)
#prints each elements within each rows
for row in joe_3d:
    for col in row:
        print(col)

print("-----------------------------Error Handler-----------------------------")
try:
    value = 10/0
    numero = int(input("Type in a number: "))
    print(numero)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")

#prints with no spaces at the beginning and at the end
txt = " Hello World "
x = txt.strip()
print(x)

#replace characters
y = "Hello Bitch"
y=y.replace("H", "J")
print(y)

#change lower or uppercase 
z = "JELLO"
z = z.lower()
print(z)

#paramter placeholder
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)
