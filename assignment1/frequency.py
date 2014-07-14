import sys

def lines(fp):
    print str(len(fp.readlines()))

def main():
	tweet_file = open(sys.argv[1])
	lines(tweet_file)


if __name__ == '__main__':
    main()