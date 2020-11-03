import argparse
import json
import logging
import sys

import redis
import requests
from slpp import slpp

from facutils import constants

logging.basicConfig(level=logging.INFO)
parser = argparse.ArgumentParser("Update Redis")

parser.add_argument(
    "--use_cache",
    action="store_true",
    default=False,
    help="If present, load the data from the json path",
)


def get_raw_data_as_dict():
    response = requests.get(constants.RAW_URL)
    response.raise_for_status()
    i = response.text.find("{")
    return slpp.decode(response.text[i:])


def main(args):
    if args.use_cache:
        logging.info("Using cached data")
        with open(constants.JSON_OUT, "r") as f:
            d = json.load(f)
    else:
        logging.info("Getting raw data from web")
        d = get_raw_data_as_dict()
        with open(constants.JSON_OUT, "w+") as f:
            json.dump(d, f)

    recipe_dict = d["recipe"]
    redis_client = redis.StrictRedis(
        host="localhost", port=constants.REDIS_PORT, password="", decode_responses=True
    )
    redis_client.flushdb()
    for k, v in recipe_dict.items():
        redis_client.set(k, json.dumps(v))


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
