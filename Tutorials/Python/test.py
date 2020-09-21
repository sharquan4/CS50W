#guess game
word = "Boobs"
guess = ""
limit = 3
count = 0
none = False

while guess != word and not(none):
    if count<limit:
        guess = input("Guess the word: ")
        count = count + 1
    else:
        none = True

if none:
    print("You lose")
else:
    print("You win!")

print("------------------------------------------")

#filling in the blanks
color = input("What color fag?: ")
food = input("What is your favorite food you fuck?: ")
job = input("What is your job dumbfuck?: ")

print("Bob's favorite color is " + color + ", his food is " + food + ", and his job is " + job + ".")

print("------------------------------------------")
#power function
def power(base,exp):
    result = 1
    for index in range(exp):
        result = result * base
    return result
print(power(2,3))
print("------------------------------------------")
#translator
def translate(phrase2):
    empty = ""
    for letter  in phrase2:
        if letter.lower() in "aeiou":
            if letter.isupper():
                empty = empty + "G"
            else:
                empty = empty + "g"
        else:
            empty = empty + letter
    return empty
print(translate(input("Enter a word or phrase for translation: ")))

print("------------------------------------------------------")
#create class & objects to make your custom data
from module1 import Student

student1 = Student("Bob", "CS", 3.3, False)
student2 = Student("Sarah", "Marketing", 3.54, True)
print(student1.name)
print(student1.gpa)
print(student2.major)
print(student1.on_honor_roll())

print("-------------------------------------")
"""
#answers questions (error)
from module1 import Question
try:
    question_prompts = [
        "What colors are apples\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
        "What colors are bananas?\n(a) Teals\n(b) Magenta\n(c) Yellow\n\n",
        "What colors are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
    ]

    questions = [
        Question(question_prompts[0], "a"),
        Question(question_prompts[1], "c"),
        Question(question_prompts[2], "b")
    ]

    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            if answer == question.answer:
                score += 1
        print("You got " + str(score) + "/" + str(len(questions)) + "Correct")

    run_test(questions)

except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")
"""

#print statement using class & inheritance
from module1 import Chef
try:
    myChef = Chef()
    myChef.make_salad()
    myChineseChef = ChineseChef()
    myChineseChef.make_salad()
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")
