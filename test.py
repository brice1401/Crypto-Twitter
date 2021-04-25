"""
Code inspired by: https://towardsdatascience.com/extracting-data-from-twitter-using-python-5ab67bff553a
"""

import json
from typing import IO, Optional, List, Any
import logging
import sys

import tweepy

if sys.version_info < (3, 8):
    raise RuntimeError("You have to run this code with at least python3.8")

logging.basicConfig(level="INFO")
log = logging.getLogger(__name__)

with open("credentials.json", "r") as credentials_file:
    credentials = json.load(credentials_file)


def get_twitter_authentication() -> Any:
    log.info("Configuring the twitter authentication")
    twitter_authentication = tweepy.OAuthHandler(credentials["consumer_key"], credentials["consumer_secret"])
    twitter_authentication.set_access_token(credentials["access_token"], credentials["access_token_secret"])
    return twitter_authentication


class MyStreamListener(tweepy.StreamListener):

    def __init__(self, api=None, max_num_status: int = 100, filename_cache: str = "tweet.txt"):
        super(MyStreamListener, self).__init__()
        self.filename_cache = filename_cache
        self.file_cache: Optional[IO] = None
        self.num_tweets = 0
        self.max_num_status = max_num_status

    def on_status(self, status) -> bool:
        tweet = status._json
        self.store_in_cache(tweet=tweet)
        self.num_tweets += 1
        if self.num_tweets < self.max_num_status:
            # While the number of max tweet is not reached, it is not stopped
            return True
        else:
            log.info(f"The maximum number of tweet (statues) {self.max_num_status=} to read has been reached, the StreamListener stops to save the tweets")
            self.file_cache.close()
            return False

    def store_in_cache(self, tweet: dict) -> None:
        if not self.file_cache:
            self.file_cache = open(self.filename_cache, "w")
            self.num_tweets = 0
        self.file_cache.write(json.dumps(tweet) + '\n')


def listen_for_keywords(keywords: List[str], max_num_status: int = 100) -> None:
    twitter_authentication = get_twitter_authentication()
    log.info("Create streaming object and authenticate")
    twitter_listener = MyStreamListener(max_num_status=max_num_status)
    stream = tweepy.Stream(twitter_authentication, twitter_listener)
    log.info(f"Launch the stream processor with the tracker set to follow the {keywords=}")
    stream.filter(track=keywords)
    log.info(f"The stream stopped")


# tweets_data_path = 'tweet.txt'
# tweets_data = []
# tweets_file = open(tweets_data_path, "r")
# # read in tweets and store on list
# for line in tweets_file:
#     tweet = json.loads(line)
#     tweets_data.append(tweet)
# tweets_file.close()
# print(tweets_data[0])

if __name__ == "__main__":
    keywords_to_watch = ['covid', 'corona', 'covid19', 'coronavirus', 'facemask', 'sanitizer', 'social-distancing']
    listen_for_keywords(keywords=keywords_to_watch, max_num_status=100)
    print("done")
