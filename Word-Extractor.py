targets = ["this", "a", "i", "is", "we","he", "she", "it", "they", "his", "her",
           "then", "them", "that", "us", "very", "of", "as", "but",
           "most", "too", "yes", "yeah", "no", "nope", "am", "can", "would" ,"their"]

ltarg = len(targets)

sentence = input("Enter a sentence : ")

#converts to lower case
sentence = sentence.lower()

#creates word List
wordL = sentence.rsplit(" ")

for i in range(ltarg):
    try:
        popLoc = wordL.index(targets[i])
        wordL.pop(popLoc)
    except:
        continue


print("Words found :")
for w in wordL:
    print("\t",w)








#     for i in range(ltarg):
#         if sentence.find(targets[i]) != -1:
#             remvS = sentence.find(targets[i])
#             remvE = len(targets[i])
#             sentence = sentence[:remvS] + sentence[remvE + 1:]





