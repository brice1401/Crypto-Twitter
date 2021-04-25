import json
import logging
from typing import Optional, IO

import tweepy
from tweepy import Status

log = logging.getLogger(__name__)


class SimpleStatusStreamListener(tweepy.StreamListener):
    def __init__(self, api=None, max_num_status: int = 100, filename_cache: str = "tweet.txt"):
        super(SimpleStatusStreamListener, self).__init__()
        self.filename_cache = filename_cache
        self.file_cache: Optional[IO] = None
        self.num_twitter_status = 0
        self.max_num_status = max_num_status

    def on_status(self, status: Status) -> bool:
        # log.debug(f"Received a status from {status=}")
        tweet = status._json
        self._store_in_cache(tweet=tweet)
        self.num_twitter_status += 1
        if self.num_twitter_status % int(self.max_num_status / 10) == 0:
            log.debug(f"Got {self.num_twitter_status=} and still receiving")

        if self._should_keep_processing():
            # While the number of max tweet is not reached, it is not stopped
            return True
        log.info(f"The maximum number of tweet (status) {self.max_num_status=} to read has been reached, the StreamListener stops to save the tweets")
        self.file_cache.close()
        return False

    def _store_in_cache(self, tweet: dict) -> None:
        if not self.file_cache:
            self.file_cache = open(self.filename_cache, "w")
            self.num_twitter_status = 0
        self.file_cache.write(json.dumps(tweet) + '\n')

    def _should_keep_processing(self):
        return self.num_twitter_status < self.max_num_status
