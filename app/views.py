from flask import jsonify, request, Blueprint
from app.coordenates import get_planet_coord
from utils import get_astro_dict


server_bp = Blueprint('server_dp', __name__)


@server_bp.route('/', methods=['GET'])
def health_check():

    return jsonify(status="Ok"), 200


@server_bp.route('/planets', methods=['GET'])
def get_planet_position():

    json = request.args.to_dict()

    planet = json.get("planet")
    lat = float(json.get("lat"))
    long = float(json.get("long"))

    coord = get_planet_coord(planet, lat, long)

    az = float(coord.az.deg)
    alt = float(coord.alt.deg)

    return jsonify(planet=planet, az=az, alt=alt), 200


@server_bp.route('/astro_list', methods=['GET'])
def get_astro_list():
    astro_dict = get_astro_dict()

    astro_list = []

    json = request.args.to_dict()

    lat = float(json.get("lat"))
    long = float(json.get("long"))

    for astro in astro_dict:
        astro_obj = {"name": astro, "category": astro_dict[astro]}

        coord = get_planet_coord(astro, lat, long)

        az = float(coord.az.deg)
        alt = float(coord.alt.deg)

        astro_obj["az"] = az
        astro_obj["alt"] = alt

        astro_list.append(astro_obj)

    return jsonify(astros=astro_list)
