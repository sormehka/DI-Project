import json
import pandas as pd
import matplotlib.pyplot as plt
import re

def word_find(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

path="/Users/sormeh/desktop/uber_lyft.txt"
data_tw=[]
file_tw=open(path,"r")
for line in file_tw:
    try:
        tweet=json.loads(line)
        data_tw.append(tweet)
    except:
        continue
tweets_df=pd.DataFrame()
tweets_df['text']=map(lambda tweet: tweet.get('text',''), data_tw)


tweets_df['promotion'] = tweets_df['text'].apply(lambda tweet: word_text('promotion', tweet))

print tweets_df['promotion'].value_counts()[True]

print tweets_df[tweets_df['promotion'] == True]['uber'].value_counts()[True]
print tweets[tweets['promotion'] == True]['lyft'].value_counts()[True]