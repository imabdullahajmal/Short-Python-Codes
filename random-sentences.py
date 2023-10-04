#Imports 
import random


#Subjs, Verbs and Objs
subj = ["He", "She", "They"]

verbS = ["Plays", "Likes", "Hits", "Drives", "Punches", "Records"]
verbP = ["Play", "Like", "Hit", "Drive", "Punch", "Record"]

objL = ["Them", "Him", "Her"]
objNL = ["Football", "Car", "House", "Boat", "Cricket", ""]

obj = [random.choice(objL), random.choice(objNL)]

noOfSent = int(input("How much sentences do you want ? :"))

Sentence = ""

#Defining Functions
def spacing(str1,str2,str3):
    return str1+" " + str2 + " " + str3

def generate_sentence():
    s = random.choice(subj)

    if s == 'They':
        Sentence = spacing(s, random.choice(verbP), random.choice(obj))

    else:
        Sentence = spacing(s, random.choice(verbS), random.choice(obj))

    return Sentence

#Printing em out
print("\n")
for i in range(noOfSent):
    print(generate_sentence())