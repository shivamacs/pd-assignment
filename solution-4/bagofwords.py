import numpy

class BagOfWords:
    def __init__(self):
        self.idx = 0
        self.word2index = {}
        self.index2word = {}

    def add(self, word):
        if word not in self.word2index.keys():
            self.word2index[word] = [self.idx, 1]
            self.index2word[self.idx] = word
            self.idx += 1
        else:
            self.word2index[word][1] += 1   

    def getcountvector(self, index):
        if index not in self.index2word:
            return "Not a valid index"

        word = self.index2word[index]
        vector = numpy.zeros(len(self.word2index), dtype=int)         

        for i, item in enumerate(self.word2index.keys()):
            if item == word:
                vector[i] += self.word2index[item][1]

        return list(vector)

    def getvectors(self, words):
        vectors = []

        for word in words:
            vector = numpy.zeros(len(self.word2index), dtype=int)

            for i, item in enumerate(self.word2index.keys()):
                if item == word:
                    vector[i] += 1

            vectors.append(list(vector))

        return vectors

bow = BagOfWords()

bow.add("John")
bow.add("likes")
bow.add("to")
bow.add("watch")
bow.add("movies")
bow.add("Mary")
bow.add("likes")
bow.add("to")
bow.add("watch")
bow.add("movies")
bow.add("too")

print(bow.getcountvector(2))
print(bow.getvectors(["movies", "John"]))