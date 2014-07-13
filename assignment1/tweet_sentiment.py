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
    count = 0
    for line in tweet_file:
    	if count == 10:
    		break
    	else :
    		count = count+1
    		data=json.loads(line)
    		print data
    #print scores.items()	
    # prints keyvalues for all scores


    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
