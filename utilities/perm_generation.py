#permuation generation

from __future__ import absolute_import
from six.moves import cPickle
import gzip
import random
import numpy as np
import sys

import glob, os, csv, re
from collections import Counter
import pickle

def get_sent_num(filename=""):
	lines = [line.rstrip('\n') for line in open(filename)]
	x = lines[1].split()
	return len(x) - 1


list_of_files = [line.rstrip('\n') for line in open(sys.argv[1])]
for file in list_of_files:
    print(file) 
    sent_num = get_sent_num(file)
    print(sent_num)

    perm = []
    idx = range(0,sent_num)
    for i in range(1,21):
    	np.random.shuffle(idx)
        tmp = idx[:]
    	perm.append(tmp)
        
    print(perm)
    with open(file + ".perm", 'wb') as fp:
        pickle.dump(perm, fp)