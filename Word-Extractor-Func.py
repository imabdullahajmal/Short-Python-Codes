sentence = input("Enter a sentence : ")

def wExt(sentence):
    targets = ["this", "a", "is", "i", "we", "he", "she", "it", "they", "his", "her",
               "then", "them", "that", "us", "very", "of", "as", "but", "what", "which",
               "most", "too", "yes", "yeah", "no", "nope", "am", "can", "would", "their",
               "whose", "you", "was"]
    sentence = sentence.lower()
    wordLis = sentence.rsplit(" ")
    wordLis = list(dict.fromkeys(wordLis))
    wordLis = [i for i in wordLis if i not in targets]

    return wordLis

list = wExt(sentence)
print(list)