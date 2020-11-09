from fim import apriori
import pandas as pd
import numpy

dataset = pd.DataFrame([line.strip().split(' ') for line in open('dataset.dat', 'r')]).to_numpy(dtype=float)
data = [list(row[~numpy.isnan(row)]) for row in dataset]

print("Most common triplets that occur together")

# confidence is default for now (80%)
# when supp parameter is reduced, more common triplets can be generated
# zmin and zmax denote the minimum and maximum number of frequent items per item set 
result = apriori(data, supp=0.8, zmin=3, zmax=3)

for tup in result:
    print([int(i) for i in tup[0]])