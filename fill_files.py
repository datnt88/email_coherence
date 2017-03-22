from BeautifulSoup import BeautifulSoup
import re, string, codecs, os
import nltk
from nltk import tokenize
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')
nbThreads = 8270

def main():
    counter = 0
    listing = os.listdir('dataset/Entity_grid_threads')
    writer_train = open ("list.sample", "w")
    writer_test = open ("list.sample.test", "w")
    writer_dev = open ("list.sample.dev", "w")
    
    for l in listing:
        if counter < 0.7 * nbThreads:
            writer_train.write("./dataset/Entity_grid_threads/" + l + "\n")
        if counter < 0.7 * nbThreads + 0.2 * nbThreads and counter >= 0.7 * nbThreads:
            writer_test.write("./dataset/Entity_grid_threads/" + l + "\n")
        if counter < 0.7 * nbThreads + 0.2 * nbThreads + 0.1 * nbThreads and counter >= 0.7 * nbThreads + 0.2 * nbThreads:
            writer_dev.write("./dataset/Entity_grid_threads/" + l + "\n")
            
        counter += 1
    
    writer_train.close()
    writer_test.close()
    writer_dev.close()
        
if __name__=='__main__':
    main()