import json
import os
from pprint import pprint


def read_feed_config():
    feed_file = os.path.dirname(os.path.realpath(__file__)) + "/config/feeds.json"
    with open(feed_file) as config_file:
        config = json.load(config_file)
        return config['feed_url']

if __name__ == '__main__':
    config = read_feed_config()
    for c in config:
        pprint(c)