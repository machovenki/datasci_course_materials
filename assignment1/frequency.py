import sys
import json
import re

def lines(fp):
    print str(len(fp.readlines()))

def main():
	tweet_file = open(sys.argv[1])
	word_frequency_count = {}

	for line in tweet_file:
		raw_data = json.loads(line)
		#print raw_data
		text = raw_data.get('text', "").lower().encode('utf-8')
		new_text=re.findall(r"[\w']+", text)
		print new_text
		#print text
        #for word in text:
        #	if not word.isalpha():
        #		print "BlahKey:"+word
        #		if word in word_frequency_count:
	    #    		oldcount = word_frequency_count[word]
	    #    		word_frequency_count[word] = ++oldcount
        	
    	#		else:
        #			word_frequency_count[word] = 1

        for word in new_text:
        	word_frequency_count[word] = 'Test'

	print word_frequency_count.items()


if __name__ == '__main__':
    main()