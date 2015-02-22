import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def build_dict(sent_file):

    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores [term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    
    return scores

def get_tweet_score(tweet_txt, scores):
    #process the tweet as per scores.
    tweet = json.loads(tweet_txt)

    print tweet["text"].encode('utf8')
    print tweet["user"]["name"].encode('utf8')
    

    return 0

def main():
   # nline = len(d)
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    print "sentiments file " + sys.argv[1]
    print "tweet file " + sys.argv[2]

    #build dict and store in scores.
    scores = build_dict(sent_file)

    print scores["kill"]
    #read line by line output.txt and calculate the score.
    #for tweet in tweet_file:
     #   tweet_score = get_tweet_score(tweet, scores)
      #  print tweet_score
       # print
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
