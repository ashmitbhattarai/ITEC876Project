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
    sentiment_map = {
        "1":"positive",
        "0":"neutral",
        "-1":"negative"
    }
    destination = "../asc/target_data"
    word_list = []
    intent_counter = 0
    sent_counter = 0

    for filetuple in os.walk(folderpath):
        for filename in filetuple[-1]:
            if "readme" in filename:
                continue
            sent_list = []
            filepath = os.path.join(folderpath, filename)
            tweet_data = open(filepath, "r+").read().splitlines()
            for idx, sent in enumerate(tweet_data[::3]):
                sent_dict = {}
                sent_counter += 1
                sent_id = str(sent_counter)

                sent_index = tweet_data.index(sent)
                entity = tweet_data[sent_index+1]
                sentiment = tweet_data[sent_index+2]

                sent_dict["polarity"] = sentiment_map[sentiment]
                sent_dict["term"] = entity
                sent_dict["id"] = sent_id
                sent_dict["sentence"] = sent.replace("$T$", entity)
                sent_list.append(sent_dict)
            random_seq = np.random.permutation(sent_list)
            sent_list = random_seq.tolist()
            if "train" in filename:
                train_test_split = int(0.15 * len(sent_list))

                train_chunk = sent_list[:train_test_split]
                dev_chunk = sent_list[train_test_split:]

                train_chunk = dict((each["id"], each) for each in train_chunk)
                dev_chunk = dict((each["id"], each) for each in dev_chunk)

                train_file = open(os.path.join(destination, 'train.json'), "w")
                dev_file = open(os.path.join(destination, 'dev.json'), "w")

                json.dump(train_chunk, train_file, indent=4)
                json.dump(dev_chunk, dev_file, indent=4)

            elif "test" in filename:
                test_file = open(os.path.join(destination, 'test.json'), "w")
                test_chunk = dict((each["id"], each) for each in sent_list)
                json.dump(test_chunk, test_file, indent=4)


read_file()