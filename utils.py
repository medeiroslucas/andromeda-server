import json
from settings import ASTROS_JSON_PATH


def get_astro_dict(astro_json_path=ASTROS_JSON_PATH):

    with open(astro_json_path,) as fil:
        astro_json = json.load(fil)

    return astro_json
