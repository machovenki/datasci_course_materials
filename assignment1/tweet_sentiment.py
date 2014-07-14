import sys
import json

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
        raw_data = json.loads(line)
        text = raw_data.get('text', "").lower().encode('utf-8')
        sentient_score = 0
        for word in text.split():
            if word in scores:
                    sentient_score += scores[term]
        print sentient_score	
    # prints keyvalues for all scores


    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
