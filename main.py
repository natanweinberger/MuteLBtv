import argparse
from datetime import datetime, timedelta
from time import sleep
from chromecast import get_chromecast
from logger import log
from game import get_feed, is_mid_inning, convert_datetime_to_timecode, get_timestamp_from_feed
from schedule import get_game_pk

# Team IDs: https://statsapi.mlb.com/api/v1/teams?sportId=1&season=2021
DEFAULT_TEAM_ID = 143  # Phillies


def run(game_pk, chromecast, timecode, verbose=False):
    ''' Get the game feed, determine if the game is mid-inning and update the mute state. '''
    feed = get_feed(game_pk, timecode=timecode)
    log.debug(feed['metaData'])

    timestamp = get_timestamp_from_feed(feed)

    log.info(f'Feed timestamp: {timestamp}')

    if is_mid_inning(feed):
        chromecast.set_volume_muted(True)
        if verbose: log.info('Is mid-inning, muting Chromecast\n')
    else:
        chromecast.set_volume_muted(False)
        if verbose: log.info('Is not mid-inning, unmuting Chromecast\n')


def main(game_pk, offset):
    chromecast = get_chromecast()

    if not game_pk:
        log.info('No game_pk provided. Defaulting to default team\'s game.')
        game_pk = get_game_pk(date=datetime.now(), team_id=DEFAULT_TEAM_ID)

    log.info(f'game_pk: {game_pk}')

    while True:
        if offset:
            timestamp = datetime.utcnow() - timedelta(seconds=offset)
            timecode = convert_datetime_to_timecode(timestamp)
        else:
            timecode = None

        run(game_pk, chromecast, timecode, verbose=True)
        sleep(5)


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--game_pk')
    parser.add_argument('--offset', type=int)

    return parser.parse_args()


if __name__ == '__main__':
    ARGS = get_args()
    main(ARGS.game_pk, ARGS.offset)
