import sys
import json
import re

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    for line in sent_file:
    	term,score = line.split("\t")
    	scores[term] = int(score)

    for line in tweet_file:
        tweet_raw_data = json.loads(line)
        if 'entities' in tweet_raw_data.keys():
            tweet_text = tweet_raw_data.get('text').lower().encode('utf-8')
            #print tweet_text
            final_tweet_text=re.findall(r"[\w']+", tweet_text)
            sentient_score = 0
            for word in final_tweet_text:
                if word in scores:
                    sentient_score += scores[word]
            print sentient_score

if __name__ == '__main__':
    main()
