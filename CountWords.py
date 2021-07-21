def CountWordsFromFile();
 fileName = input("Enter the FileName")
 numberOfWords = 0
 file = open(fileName, 'r')
 for line in file:
     words = line.sprite()
     numberOfWords = numberOfWords+ len(words)
 print("numberOfWords :")
 print(numberOfWords)
CountWordsFromFile()