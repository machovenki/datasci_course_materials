import sys
import json
import re
from collections import Counter


def lines(fp):
    print str(len(fp.readlines()))


def main():
    tweet_file = open(sys.argv[1])
    cnt = Counter()
    for line in tweet_file:
        raw_data = json.loads(line)
        text = raw_data.get('text', "").lower().encode('utf-8')
        new_text=re.findall(r"[\w']+", text)
        for word in new_text:
            cnt[word] += 1

    total_word_count =  float(sum(cnt.values()))

    for k,v in cnt.items():
        old_value = cnt[k]
        cnt[k] =  (old_value/total_word_count)
        if k.isalpha():
            print k,cnt[k]





if __name__ == '__main__':
    main()