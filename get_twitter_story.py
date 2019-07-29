# -*- coding: utf-8 -*-
from datetime import datetime
#from googletrans import Translator
from translate import Translator
from TwitterSearch import *

import configparser
import random
import re
import io

weather = [u"Sunny", u"Rainy", u"Cloudy"]
weather_tw = [u"晴天",u"雨天", u"陰天"]

translator= Translator(to_lang='zh-TW')
#translator= Translator()

cf = configparser.ConfigParser()
cf.read('janediary.conf')

#consumer_key = cf.get('twitter', 'consumer_key')
#consumer_secret = cf.get('twitter', 'consumer_secret')
#access_token = cf.get('twitter', 'access_token')
#access_token_secret = cf.get('twitter', 'access_token_secret')

ts = TwitterSearch(
    consumer_key = cf.get('twitter', 'consumer_key'),
    consumer_secret = cf.get('twitter', 'consumer_secret'),
    access_token = cf.get('twitter', 'access_token'),
    access_token_secret = cf.get('twitter', 'access_token_secret')
)
data_path = cf.get('data', 'data_path')

tso = TwitterSearchOrder()

def get_tweets(keyword_list, num=20, lang='en'):
    tweets = []
    try:
        tso.set_keywords(keyword_list)
        tso.set_language(lang)
        i = 0
        for tweet in ts.search_tweets_iterable(tso):
            if i == num:  break
            if tweet['retweeted']: continue
            tweets.append(tweet)
            i = i+1

    except TwitterSearchException as e:
        print(e)

    return tweets

def generate_jane_story(num=20, lang='en'):
    tweets = get_tweets(['jane'], num, lang)
    story = ""
    for tweet in tweets:
        story = u"%s %s" % (story, tweet['text'])

    return story

def clear_up_text(text):
    text = re.sub(r'RT @\S+: ', '', text)
    clear_text = re.sub(r'http\S+', '', text)
    clear_text = remove_emoji(clear_text)

    return clear_text.strip()

def remove_emoji(text):
    emoji_pattern = re.compile(
        u"(\ud83d[\ude00-\ude4f])|"  # emoticons
        u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
        u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
        u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
        u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
        "+", flags=re.UNICODE)

    return emoji_pattern.sub(r'', text)

def get_translation(input_text, lang='zh-TW'):
    output = ""
    try:
        #output = translator.translate(input_text, dest=lang)
        output = translator.translate(input_text)

    except Exception as e:
        print(e)
        return ""

    return output

def save_story(filename, text):
    with io.open(filename,'w',encoding='utf8') as f:
        f.write(text)
        f.close()

if __name__ == '__main__':
    jane_story_en = ""
    clear_story = ""
    translated_story = ""
    
    jane_story_en = generate_jane_story(10, 'en')
    clear_story = clear_up_text(jane_story_en)
    print("---")
    print(clear_story)
    translated_story = get_translation(clear_story[:500])
    print("----")
    print(translated_story)
    current_time = datetime.now()
    weather_idx = random.randrange(3)
    y, m, d, h = current_time.year, current_time.month, current_time.day, current_time.hour
    clear_story = u"%s %s\n%s" % (current_time.strftime('%Y-%m-%d %H:00'), weather[weather_idx], clear_story)
    translated_story = u"%d年%d月%d日%d時 %s\n%s" % (y, m, d, h, weather_tw[weather_idx], translated_story)

    print(clear_story)
    print("\n")
    print(translated_story)
    print("save file")
    save_story("%s/%s.txt" %(data_path, current_time.strftime("%Y%m%d")), clear_story+"\n\n"+translated_story)
    #save_story("%s/%s_en.txt" % (data_path, current_time.strftime("%Y%m%d")), clear_story)
    #save_story("%s/%s_tw.txt" % (data_path, current_time.strftime("%Y%m%d")), translated_story)

