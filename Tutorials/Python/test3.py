#use of random.seed
import random

random.seed(3)
print ("first number  - ", random.randint(25,50))  

random.seed(2)
print ("Second number- ", random.randint(25,50))

for i in range(2):
    random.seed(10)
    for i in range(20):
        print(random.random())
    print()

print("---------------------------------------------------------------------")
#random integer
rand = random.randint(40,60)
print(rand)

print("---------------------------------------------------------------------")

#conjoin elements in a list
name=["a","b","c","d"]
print (', '.join(name))
print(*name, sep=", ")
print(", ".join(str(x) for x in name))
#for the number of elements in the list in a variable in prints out that many
for x in name:
    print(name)


print("---------------------------------------------------------------------")
#print the list
a=[1,2,3,4,5]
print(*a, sep =' ')
print("".join(str(a)))
a = str(a)
print(a)

print("---------------------------------------------------------------------")
#make sure to have the txt within your python file and use folder view to open the txt and py file on visual studio 2019
"""
#read external files
random1 = open("random.txt", "r")
#write over external file
random2 = open("random.txt", "w")
#append external files
random3 = open("random.txt", "a")
#read & write over external file
random4 = open("random.txt", "r+")
#how to close the file is to type 
[variable].close()
#how to check a file if  it's readable 
print([variable].readable())
#print out all the information of the external file 
print([variable].read())
#how to read out a line of external file 
print([variable].readline()) #copy and paste in new lines for additional lines
#how to print each line in a single line 
print([variable].readlines())
print([variable].readlines()[1])
"""
#read a file using python
"""
try:
    info_file = open("information.txt", "r")
    for employee in info_file.readlines():
        print(info_file)
    info_file.close()
except:
    print("Invalid")
"""
#append to a file
"""
try:
    file1 = open("information.txt", "a")
    file1.write("\nWADDUP!?")
    file1.close()
except:
    print("Invalid")
"""
#read file
"""
file1 = open("information.txt", "r")
file1.read()
file1.close()
"""
"""
file1 = open("information.txt", "w")
file1.write("\nPoop")
file1.close()
"""
print("----------------------------------------------")
import useful_tool
print(useful_tool.roll_dice(10))
