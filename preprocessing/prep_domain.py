import spacy
import numpy as np
from collections import defaultdict
import os
import random
import json, csv
random.seed(1337)
np.random.seed(1337)


def read_file(folderpath="../asc/sentihood"):
    '''
        reads the file from target tweet do
    '''
    sentiment_map = {
        "1":"positive",
        "0":"neutral",
        "-1":"negative"
    }
    destination = "../domain_corpus/raw"
    word_list = []
    intent_counter = 0
    sent_counter = 0
    with open(destination+"/rest.txt","a") as filewrite:
        for filetuple in os.walk(folderpath):
            for filename in filetuple[-1]:
                if "readme" in filename:
                    continue
                sent_list = []
                filepath = os.path.join(folderpath, filename)
                tweet_data = []
                
                tweet_data = open(filepath, mode="r+",encoding="utf-8",errors="ignore").read().splitlines()
                
                for sent in tweet_data:
                    try:
                        sent = sent.split('","')
                        filewrite.write(sent[-1].lstrip('"').replace('"',"").strip()+"\n")
                    except:
                        print ("Continue")


read_file()
