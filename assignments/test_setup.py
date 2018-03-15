from collections import defaultdict
import operator
import sys
import nltk
import nilsimsa



def tuple_list_to_string(tl):
    return "\n".join(["{0:>6} {1}".format(v, k)
                      for k,v in tl])


def print_version_info():
    print "Using Python version {}.{}.{}".format(
        *sys.version_info[:3])
    print "Using nltk version {}".format(nltk.__version__)


def name_vs_brown():
    name = raw_input("Please enter your full name: ")
    name_parts = name.lower().split(' ')
    name_frequency = {}

    unigram_frequency = defaultdict(int)
    for word in nltk.corpus.brown.words():
        unigram_frequency[word.lower()] += 1
    for name_part in name_parts:
        if name_part not in unigram_frequency.keys():
            unigram_frequency[name_part] = 0
            name_frequency[name_part] = 0
        else:
            name_frequency[name_part] = unigram_frequency[name_part]

    sorted_unigrams = sorted(unigram_frequency.items(),
                             key=operator.itemgetter(1), reverse=True)

    print nilsimsa.Nilsimsa(name).hexdigest()
    print "-----------------------------"
    print tuple_list_to_string(name_frequency.items())
    print "-----------------------------"
    print tuple_list_to_string(sorted_unigrams[:20]
                               + [(""," .")]*3
                               + sorted_unigrams[-20:])
    print "-----------------------------"


if __name__=="__main__":
    name_vs_brown()
    print_version_info()
