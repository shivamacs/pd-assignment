import mmh3
import math
import shelve
from bitarray import bitarray
from collections import defaultdict, OrderedDict

class BloomFilter:
    def __init__(self, N):
        self.capacity = N;
        self.size = self.get_size(50, 0.05);
        self.hash_count = self.get_hash_count(self.size, 100)
        self.bf_array = bitarray(self.size)
        self.bf_array.setall(0)
        self.db = shelve.open("data", writeback=True)
        flag = "data_list" in self.db
        
        if(flag):
            for i in range(len(self.db["data_list"])):
                self.add_in_bit_array(self.db["data_list"][i])    
        else:
            self.db["data_list"] = []

        self.ram = {}
        self.freqs = defaultdict(OrderedDict)
        self.min_freq = 1

    def add(self, item):
        if item in self.ram:
            self.get(item)
            return
        elif len(self.ram) == self.capacity:
            old, v = self.freqs[self.min_freq].popitem(last=False)
            del self.ram[old]
        
        self.min = 1
        self.ram[item] = 1
        self.freqs[1][item] = 0

        self.add_in_bit_array(item)
        self.db["data_list"].append(item)
        self.db.sync()
        
    def add_in_bit_array(self, item):
        for i in range(self.hash_count):
            bit = mmh3.hash(item, i) % self.size
            self.bf_array[bit] = True

    def get(self, item):
        if item in self.ram:
            fr = self.ram[item]
            del self.freqs[fr][item]

            if fr == self.min_freq and not self.freqs[fr]:
                self.min_freq += 1;

            self.freqs[fr + 1][item] = 0
            self.ram[item] = fr + 1

            return True
        
        for i in range(self.hash_count):
            bit = mmh3.hash(item, i) % self.size
            if self.bf_array[bit] == False:
                return False
        
        return True

    def get_size(self, count, fp):
        m = -(count * math.log(fp))/(math.log(2)**2)
        return int(m)

    def get_hash_count(self, m, n):
        k = (m / n) * math.log(2);
        return int(k);

    def update(self, item):
        if(self.get(item) == False):
            self.add(item)
            return item + " added successfully"
        else:
            return item + " is PROBABLY present already"

bf = BloomFilter(10)

animals = ['dog', 'cat', 'giraffe', 'fly', 'mosquito', 'horse', 'eagle',
           'bird', 'bison', 'boar', 'butterfly', 'horse', 'anaconda', 'bear',
           'chicken', 'cat', 'crow', 'crocodile', 'whale', 'dog', 'falcon', 
           'goat', 'cat', 'fox', 'dolphin', 'dog', 'frog', 'crow', 'fly', 
           'dog', 'pig', 'hawk', 'bear']

for animal in animals:
    print(bf.update(animal))