import logging
from typing import Dict

DEFAULT_LOG_LEVEL = logging.DEBUG

MAP_LOGGER_LEVEL: Dict[str, int] = {
    "requests_oauthlib": logging.INFO,
    "oauthlib": logging.INFO,
    "urllib3": logging.INFO,
}


def configure_logging():
    logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(levelname)-7s] %(name)-15s - %(message)s',
                        level=DEFAULT_LOG_LEVEL,
                        datefmt='%Y-%m-%d %H:%M:%S')
    for logger_name, level in MAP_LOGGER_LEVEL.items():
        logging.getLogger(logger_name).setLevel(level)
