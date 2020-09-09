import json

def get_game_date(game_id):
    finished_date = {}
    date = game_id.split('-')
    finished_date['year'] = date[1]
    finished_date['month'] = date[2]
    finished_date['day'] = date[3]
    return finished_date
