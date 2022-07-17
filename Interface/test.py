with open('directory.txt', 'r') as file:
    directory = file.read()

stoplist = []

print(directory)

stopwords_path = directory + "/stopwords/stopwords.txt"

with open(stopwords_path,encoding="utf-8") as f:
  contents = f.read()
  stoplist = "haha"

print(stoplist)