import sys
import json
import re
from collections import Counter
import operator

def lines(fp):
    print str(len(fp.readlines()))


def main():

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {}
    for line in sent_file:
    	term,score = line.split("\t")
    	scores[term] = int(score)

    cnt = Counter()
    for line in tweet_file:
        tweet_raw_data = json.loads(line)
        tweet_text = tweet_raw_data.get('text', "").lower().encode('utf-8')
        final_tweet_text=re.findall(r"[\w']+", tweet_text)
        places = tweet_raw_data.get('place',"")
        if places != None:
            if type(places)==type(dict()):
                if places['country'] == 'United States':
                    state_name = places['full_name'].encode('utf8').split(',')[1].strip()
                    if state_name != 'USA':
                        sentient_score = 0
                        for word in final_tweet_text:
                            if word in scores:
                                sentient_score += scores[term]
                        cnt[state_name]+=sentient_score


    outputTagsWithFrequency = dict(sorted(cnt.items(),key=operator.itemgetter(1), reverse=True)[:1])

    for k,v in sorted(outputTagsWithFrequency.items(), key=lambda lkv: (lkv[1],lkv[0]),reverse=True):
        print("%s" % (k.decode("utf-8")))






if __name__ == '__main__':
    main()