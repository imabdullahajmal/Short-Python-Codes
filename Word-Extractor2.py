targets = ["this", "a", "is", "i", "we","he", "she", "it", "they", "his", "her",
           "then", "them", "that", "us", "very", "of", "as", "but", "what", "which",
           "most", "too", "yes", "yeah", "no", "nope", "am", "can", "would" ,"their",
           "whose", "you", "was"]


sentence = input("Enter a sentence : ")

#converts to lower case
sentence = sentence.lower()

#creates word List
wordL = sentence.rsplit(" ")

#removes dupes
wordL = list(dict.fromkeys(wordL))
print(wordL)
wordL_copy = wordL

for i in wordL:
    if i in targets:
        wordL.remove(i)

print(wordL)
