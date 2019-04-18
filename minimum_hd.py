import random
import numpy as np
import pandas as pd
from hamming_parctice import hamming

df = pd.read_csv('sample.csv', names=['word', 'bin'])

def solution():
    count = 1
    min = 100000
    for i in range(0, 100):
          for j in range(i+1, 100):
              hd = hamming(df.iloc[i,1], df.iloc[j,1])
              print(count, "(", df.iloc[i,0], df.iloc[j,0],")hamming_distance: ",hd)
              if min >hd:
                  min = hd
              count += 1
    return min

print("min hamming distance", solution())
