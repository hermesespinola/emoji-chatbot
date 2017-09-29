#!/usr/bin/python2
from __future__ import division
import nltk
import sys
import random
from sys import exit
import pickle
import json, csv
from emojis import separateTweetEmojis, cleanWord
from math import ceil, floor
import argparse
from pprint import pprint

parser = argparse.ArgumentParser(description='Yuya tweets classifier')
parser.add_argument('--train', '-t', action='store_true',
                    help='Train classifier, if tag is not present start production mode')

train_mode = parser.parse_args().train
stemmer = nltk.SnowballStemmer('spanish')

def tweets_from_csv(path, tweets):
    with open(path) as f:
        all_tweets = csv.DictReader(f)
        for tweet in all_tweets:
            # clean tweet
            emojis, text = separateTweetEmojis(tweet['text'])
            # Separa el tweet solo considerando los espacios
            clean_text = " ".join(text.split('\n'))
            tweets.append((cleanWord(clean_text), tweet['label'].lower()))
        return tweets

def tweets_from_json(path, tweets):
    with open(path) as f:
        all_tweets = json.load(f)
        for tweet in all_tweets:
            # clean tweet
            emojis, text = separateTweetEmojis(tweet['text'])
            # Separa el tweet solo considerando los espacios
            clean_text = " ".join(text.split('\n'))
            tweets.append((cleanWord(clean_text), tweet['label'].lower()))
        return tweets

# for (words, sentiment) in pos_tweets + neg_tweets + neu_tweets:
#     words_filtered = [separateTweetEmojis(e.lower())[1] for e in words.split() if len(e) >= 3]
#     tweets.append((words_filtered, sentiment))

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def get_extract_features_fun(word_features):
    return lambda document: {'contains(%s)' % word: (word in set(document)) for word in word_features}

def train_classifier(classifierAlgorithm, run_validation=True):
    tweets = tweets_from_csv('polaridad.csv', [])
    word_features = get_word_features(get_words_in_tweets(tweets))
    random.shuffle(tweets)
    training_size = len(tweets)
    if run_validation:
        training_size = int(ceil(2 * len(tweets) / 3))
    training_tweets = tweets[:training_size]
    extract_features = get_extract_features_fun(word_features)
    training_set = nltk.classify.apply_features(extract_features, training_tweets)

    print "Training classifier..."
    classifier = classifierAlgorithm.train(training_set)
    print "Done.\n"
    print "labels are:", classifier.labels()

    if run_validation:
        print "\nRunning validation test..."
        validation_tweets = tweets[training_size+1:]
        val = map(lambda pair: pair[0], validation_tweets)
        targets = map(lambda t: t[1], validation_tweets)
        validation_set = nltk.classify.apply_features(extract_features, validation_tweets)
        predictions = [classifier.classify(extract_features(t)) for t in val]
        # predictions = classifier.classify_many(validation_set)
        pairs = zip(targets, predictions)
        true_pos = sum([1 for trgt, pred in pairs if trgt == pred == 'positivo'])
        false_pos =  sum([1 for trgt, pred in pairs if (pred == 'positivo') and trgt == 'negativo'])
        true_neg = sum([1 for trgt, pred in pairs if trgt == pred == 'negativo'])
        false_neg =  sum([1 for trgt, pred in pairs if pred == 'negativo' and (trgt == 'negativo')])
        precision = true_pos / (true_pos + false_pos)
        recall = true_pos / (true_pos + false_neg)
        f1 = 2 * ((precision*recall) / (precision+recall))

        print "True positives:", true_pos
        print "True negatives:", true_neg
        print "False positives:", false_pos
        print "False negatives:", false_neg
        print "Validation precision:", precision
        print "Validation recall:", recall
        print "Validation F1 score:", f1

    return classifier, word_features

if train_mode:
    classifier, word_features = train_classifier(nltk.NaiveBayesClassifier)
    save_classifier = open("classifier.pickle", "wb")
    pickle.dump(classifier, save_classifier)
    save_classifier.close()
    save_features = open("word_features.pickle", "wb")
    pickle.dump(word_features, save_features)
else:
    f = open('classifier.pickle', 'r')
    classifier = pickle.load(f)
    f.close()
    f = open('word_features.pickle', 'r')
    word_features = pickle.load(f)
    tweett = raw_input("tweet: ")
    extract_features = get_extract_features_fun(word_features)
    while tweett:
        # Classify new input
        # clean tweet
        emojis, text = separateTweetEmojis(tweett)
        # Separa el tweet solo considerando los espacios
        clean_text = cleanWord(text)
        dist = classifier.prob_classify(extract_features(clean_text))
        print " ".join(clean_text) + ":", valued
        for label in dist.samples():
            print "%s: %f" % (label, dist.prob(label))
        tweett = raw_input("tweet: ")
