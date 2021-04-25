import json
import logging
from typing import Dict, Any

import tweepy

log = logging.getLogger(__name__)


def get_credentials() -> Dict[str, str]:
    potential_credentials_filenames = ("./credentials.json", "../credentials.json")
    for credential_filename in potential_credentials_filenames:
        log.debug(f"Trying to get credentials from {credential_filename=}")
        try:
            with open(credential_filename, "r") as credentials_file:
                log.info(f"Using the credentials found in {credential_filename=}")
                return json.load(credentials_file)
        except FileNotFoundError as e:
            log.warning(f"{credential_filename=} not found")
            continue
    raise FileNotFoundError(f"No credentials as been found, try setting the credentials file `credentials.json` file at the root of the project")


def get_twitter_authentication() -> Any:
    credentials = get_credentials()
    log.info("Configuring the twitter authentication")
    twitter_authentication = tweepy.OAuthHandler(credentials["consumer_key"], credentials["consumer_secret"])
    twitter_authentication.set_access_token(credentials["access_token"], credentials["access_token_secret"])
    return twitter_authentication