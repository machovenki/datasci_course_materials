import sys
import json
import re
from collections import Counter
import operator

def lines(fp):
    print str(len(fp.readlines()))


def main():
    tweet_file = open(sys.argv[1])

    cnt = Counter()

    for line in tweet_file:
        tweet_raw_data = json.loads(line)
        if 'entities' in tweet_raw_data.keys():
            hashtags= tweet_raw_data['entities']['hashtags']
            for tag in hashtags:
                if tag != None:
                    tagText= tag['text'].encode("utf8")
                    cnt[tagText] +=1


    outputTagsWithFrequency = dict(sorted(cnt.items(),key=operator.itemgetter(1), reverse=True)[:10])

    for k,v in sorted(outputTagsWithFrequency.items(), key=lambda lkv: (lkv[1],lkv[0]),reverse=True):
        print("%s  %d" % (k.decode("utf-8"), v))






if __name__ == '__main__':
    main()