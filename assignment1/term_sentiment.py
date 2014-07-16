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
    new_scores = {}
    tweet_to_score = {}
    for line in sent_file:
    	term,score = line.split("\t")
    	scores[term] = int(score)

    for line in tweet_file:
        tweet_raw_data = json.loads(line)
        if 'text' in tweet_raw_data.keys():
            tweet_text = tweet_raw_data.get('text').lower().encode('utf-8')
            final_tweet_text=re.findall(r"[\w']+", tweet_text)
            sentient_score = 0
            for word in final_tweet_text:
                if word in scores:
                    sentient_score += scores[word]
                tweet_to_score[tweet_text]=sentient_score

    for k,v in tweet_to_score.items():
        text= re.findall(r"[\w']+", k)
        for word in text:
            if word not in scores:
                new_scores[word]= tweet_to_score[k]


    for k,v in new_scores.items():
        print("%s  %d" % (k.decode("utf-8"), v))
if __name__ == '__main__':
    main()
