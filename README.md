# M(ute)LB.tv

MLB.tv commercials are repetitive and annoying. I wrote this so I don't have to hear them any more.

## What does it do?

If you use a Chromecast to stream the game, you can use this package to mute commercials.

It polls the MLB API to determine when the game is between innings.

When a commercial break starts, it mutes your Chromecast. When the commercial break ends, it unmutes your Chromecast.

## How do I run it?

```bash
# Run with defaults
python main.py

# Run with a delay, to match TV delay
python main.py --offset=30  # seconds

# Run with specified Chromecast name
python main.py --chromecast_name="Living Room TV"

# Run for a specific game
python main.py --game_pk=600450
```

## What can I customize?

To change the defaults, take a look at the top of `main.py`:

```python
DEFAULT_TEAM_ID = 143  # Phillies
DEFAULT_CHROMECAST_NAME = 'Living Room TV'
API_POLL_INTERVAL = 5  # seconds
```

For a list of team IDs, use MLB's API: https://statsapi.mlb.com/api/v1/teams?sportId=1&season=2021

The `API_POLL_INTERVAL` represents how frequently the program pings MLB's API, as opposed to the offset, which is how long a delay is baked in so that the TV feed is synced up. You may have to experiment with the offset.

## Notes

When the logger is set to show debug statements (see [logger.py](./logger.py)), you can view the latest state of the game in the console as the API is polled (e.g., the current count). This is a helpful way to determine if the offset is set up right.

For example, you should tweak the offset so that the count changes in sync with the TV feed.
