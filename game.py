import json
import requests
from logger import log


def get_feed(game_pk, timecode=None):
    url = f'https://statsapi.mlb.com/api/v1.1/game/{game_pk}/feed/live'

    if timecode:
        url += f'?timecode={timecode}'
        log.info(f'Using timecode: {timecode}')

    response = requests.get(url)

    return json.loads(response.text)


def get_timestamp_from_feed(feed):
    return feed['metaData']['timeStamp']


def is_mid_inning(feed):
    return 'midInning' in feed['metaData']['logicalEvents']


def convert_datetime_to_timecode(dt):
    return dt.strftime('%Y%m%d_%H%M%S')


def main(game_pk):
    feed = get_feed(game_pk)
    ret = get_timestamp_from_feed(feed)
    print(ret)


if __name__ == '__main__':
    import sys
    game_pk = sys.argv[1]
    main(game_pk)
