from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os

import twitter_keys


try:
    os.remove("tweets.json")
except:
    pass

# Criando a lista de palavras-chave que serão rastreadas
tracklist = ['Manchester United', 'Champions League']

with open('tracklist.json', 'w') as tl:
    tl.write(str(tracklist))

# Iniciando as variáveis globais
tweet_count = 0

# Entre com o número de tweets que serão baixados
n_tweets = 100

# Classe que irá possibilitar o streaming de tweets
class StdOutListener(StreamListener):
      
    def on_data(self, data):
        
        global tweet_count
        global n_tweets
        global stream
        
        if tweet_count < n_tweets:
            print(data)
            with open('tweets.json', 'a') as f:
                f.write(data)
            tweet_count += 1
            return True
        else:
            stream.disconnect()

    def on_error(self, status):
        print(status)


# Fazendo a autenticação no Twitter e criando a conexão com o Twitter Streaming API
l = StdOutListener()
auth = OAuthHandler(twitter_keys.CONSUMER_KEY, twitter_keys.CONSUMER_SECRET)
auth.set_access_token(twitter_keys.ACCESS_TOKEN, twitter_keys.ACCESS_TOKEN_SECRET)
stream = Stream(auth, l)
stream.filter(track=tracklist, languages=["en"])
