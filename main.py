import logging
import sys
from typing import List

import tweepy

from crypto_twitter.authentcation import get_twitter_authentication
from crypto_twitter.logging import configure_logging
from crypto_twitter.streams.listeners.simple_status_stream_listener import SimpleStatusStreamListener

configure_logging()
if sys.version_info < (3, 8):
    raise RuntimeError("You have to run this code with at least python3.8")

log = logging.getLogger(__name__)


def listen_for_keywords(keywords: List[str], max_num_status: int = 100) -> None:
    twitter_authentication = get_twitter_authentication()
    log.info("Create streaming object and authenticate")
    twitter_listener = SimpleStatusStreamListener(max_num_status=max_num_status)
    stream = tweepy.Stream(twitter_authentication, twitter_listener)
    log.info(f"Launch the stream processor with the tracker set to follow the {keywords=}")
    stream.filter(track=keywords)
    log.info(f"The stream stopped")


if __name__ == '__main__':
    listen_for_keywords(keywords=["crypto", "bitcoin", "btc", "ethereum", "eth"])
