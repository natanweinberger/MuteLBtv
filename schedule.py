''' Functions to access MLB's schedule API. '''
import requests
from logger import log


def get_game_pk(date, team_id):
    ''' Given a date and an MLB team ID, retrieve the game_pk for their game. '''
    formatted_date = date.strftime('%Y-%m-%d')
    url = f'http://statsapi.mlb.com/api/v1/schedule?sportId=1&startDate={formatted_date}&endDate={formatted_date}&teamId={team_id}'

    ret = requests.get(url)

    game_pk = ret.json()['dates'][0]['games'][0]['gamePk']

    return game_pk
