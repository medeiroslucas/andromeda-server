from flask import jsonify, request, Blueprint
from app.coordenates import get_planet_coord
from utils import get_astro_dict


server_bp = Blueprint('server_dp', __name__)


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
    return get_astro_dict()
