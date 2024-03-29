'''
MadLib Assignment
Author: Andrew Lancaster
Created on: 10/1/2015
'''

# User prompts
person_one = raw_input("Choose a name:   ")
age = raw_input("And how old is " + str(person_one) + "?   ")
person_two = raw_input("Choose another name:   ")
drink_number_one = raw_input("Choose a number between 1 and 10:   ")
drink_number_two = raw_input("Choose another number between 1 and 10:   ")
adjective_one = raw_input("Choose an adjective:   ")
adjective_two = raw_input("Choose another adjective:   ")
animal = raw_input("Choose an animal(singular):   ")
action = raw_input("Choose an action verb:   ")
animal_two = raw_input("Choose an animal(plural):   ")

# define age in dictionary object
person_one_age = {str(person_one): str(age)}

# Function for displaying person_one drinking their drinks
def drink(initial,drinks):
    for i in range(initial, drinks):
        print str(person_one) + " drinks drink number " + str(i+1) + "."
        i += 1

# get random name from array
import random
random_names = ["John", "Bill", "Caitlyn", "Jessica"]
random_name = random.choice(random_names)

# Start of Madlib output
print "******* ONCE UPON A TIME *******"
print person_one + " walks into a bar and asks the bartender for " + str(drink_number_one) + " drinks."

# If statement to display a response depending on how many drinks person_one orders
if int(drink_number_one) >= 3:
    # If more than 3 drinks are ordered, then...
    print str(person_two) + ' says, "Listen, ' + str(person_one) + ', that is a ' + str(adjective_one) + ' amount of drinks to order!"'
    print str(person_one) + ' replies, "Don\'t be such a ' + str(adjective_two) + ' ' + str(animal) + ', ' + str(person_two) + '. One is for me, and the other ' + str(int(drink_number_one)-1) + ' drinks are for my other personalities."'
    drink(0,int(drink_number_one))
elif int(drink_number_one) == 2:
    # Or else if there is 2 drinks, then...
    print str(person_two) + ' says, "Two drinks? Are you ' + str(adjective_one) + '? I\'m driving!"'
    print str(person_one) + ' replies, "It\'s for my other personality, you ' + str(adjective_two) + ' ' + str(animal) + '."'
    drink(0,int(drink_number_one))
else:
    # Otherwise there must be only 1 drink, so do this:
    print str(person_two) + ' says, "' + str(person_one) + ', what about your other personalities? What will they drink?"'
    print str(person_one) + ' replies, "They\'ve been ' + str(adjective_two) + ' ' + str(animal) + 's lately. They don\'t deserve to drink."'
    print str(person_one) + " drinks the drink."

print str(person_two) + ' says, "Well okay then. When you\'re done, we should ' + str(action) + ' the ' + str(animal_two) + ' while it\'s still early."'
print str(person_one) + ' responds, "You\'re on! Let me just order ' + str(drink_number_two) + ' more drinks and I\'ll be ready to ' + str(action) + '!"'

if int(drink_number_two) > 1:
    # if drink_number_two is more than 1, then...
    print '"Are you kidding? That is ' + str(int(drink_number_one) + int(drink_number_two)) + ' drinks! You\'re going to be sick!" ' + str(person_two) + ' exclaims.'
    print '"My other personalities, man! Don\'t listen to ' + str(person_two) + ', ' + random_name + '. They don\'t mean it. We\'ve known each other since I was ' + person_one_age.get(str(person_one)) + ' years old and they still don\'t know that they don\'t really exist."'
else:
    # if drink_number_two is not more than 1, it must be 1, so do this:
    print '"I guess one more wouldn\'t hurt. Heck, order me one, too!" ' + str(person_two) + ' says.'

print "******* THE END *******"