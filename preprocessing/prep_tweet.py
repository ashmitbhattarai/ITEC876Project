import spacy
import numpy as np
from collections import defaultdict
import os
import random
import json
random.seed(1337)
np.random.seed(1337)


def read_file(folderpath="../target_data"):
    '''
        reads the file from target tweet do
    '''
    destination = "../asc/target_data"
    for filetuple in os.walk(folderpath):
        for filename in filetuple[-1]:
            sent_list = []
            filepath = os.path.join(folderpath, filename)
            tweet_data = open(filepath, "r+").read().splitlines()
            for idx, sent in enumerate(tweet_data[::3]):
                sent_index = tweet_data.index(sent)
                entity = tweet_data[sent_index+1]
                sentiment = tweet_data[sent_index+2]
                
                sent_list.append(sent)
            random_seq = np.random.permutation(sent_list)
            sent_list = random_seq.tolist()
            if "train" in filename:
                train_test_split = int(0.15 * len(sent_list))

                train_chunk = sent_list[:train_test_split]
                dev_chunk = sent_list[train_test_split:]

                train_file = open(os.path.join(destination, 'train.json'), "w")
                dev_file = open(os.path.join(destination, 'dev.json'), "w")

                json.dump(train_chunk, train_file, indent=4)
                json.dump(dev_chunk, dev_file, indent=4)

            elif "test" in filename:
                test_file = open(os.path.join(destination, 'test.json'), "w")
                json.dump(sent_list, test_file, indent=4)


# read_file()