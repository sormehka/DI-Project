import json
import pandas as pd
import matplotlib.pyplot as plt
import re

path="/Users/sormeh/desktop/DI/uber_lyft.txt"
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

#tweets_df['country']=map(lambda tweet: tweet.get('place','')['country'] if tweet['place'] != None else None, data_tw)

#tweets_country = tweets_df['country'].value_counts()

#fig, ax = plt.subplots()
#ax.tick_params(axis='x', labelsize=10)
#ax.tick_params(axis='y', labelsize=10)
#ax.set_xlabel('Countries', fontsize=10)
#ax.set_ylabel('Number of tweets' , fontsize=10)
#ax.set_title('Top 5 countries', fontsize=10, fontweight='bold')
#tweets_by_country[:5].plot(ax=ax, kind='bar', color='red')
#plt.show()

def word_find(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

tweets_df['uber'] = tweets_df['text'].apply(lambda tweet: word_find('uber', tweet))
tweets_df['lyft'] = tweets_df['text'].apply(lambda tweet: word_find('lyft', tweet))
tweets_df['taxi'] = tweets_df['text'].apply(lambda tweet: word_find('taxi', tweet))

print tweets_df['uber'].value_counts()[True]
print tweets_df['lyft'].value_counts()[True]
print tweets_df['taxi'].value_counts()[True]

transport = ['uber', 'lyft', 'taxi']
tweets_transport = [tweets_df['uber'].value_counts()[True], tweets_df['lyft'].value_counts()[True], tweets_df['taxi'].value_counts()[True]]

x_pos = list(range(len(transport)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_transport, width, alpha=1, color='g')
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: uber vs. lyft vs. taxi', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(transport)
plt.grid()
plt.show()

tweets_df['promo'] = tweets_df['text'].apply(lambda tweet: word_find('[promo]\w+', tweet))

print tweets_df['promo'].value_counts()[True]

print tweets_df[tweets_df['promo'] == True]['uber'].value_counts()[True]
print tweets_df[tweets_df['promo'] == True]['lyft'].value_counts()[True]

tweets_by_promo = [tweets_df[tweets_df['promo'] == True]['uber'].value_counts()[True], 
                      tweets_df[tweets_df['promo'] == True]['lyft'].value_counts()[True]]
x_pos = list(range(2))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_promo, width,alpha=1,color='g')
ax.set_ylabel('Number of tweets', fontsize=10)
ax.set_title('Ranking: uber vs. lyft (promotions)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(['uber','lyft'])
plt.grid()
plt.show()
