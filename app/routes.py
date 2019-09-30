
# 3rd party imports

from flask import request, make_response, jsonify
from flask import current_app as app
import json

# Application imports
from .db_models import db, Marker
from .status_codes import *


@app.route('/markers', methods=['GET', 'POST'])
@app.route('/markers/<id>', methods=['PUT', 'DELETE'])
def markers(id=None):
    """
    API method which handles all GET, POST, PUT and DELETE requests
    :param id: Marker Id
    """
    data ={}
    if request.data:
        data = json.loads(request.data) or {}
    name = data.get('name') or None
    lat = data.get('lat') or None
    long = data.get('long') or None
    print (request.data)
    if id is None:
        if request.method == 'GET':
            data = [marker.serialize for marker in Marker.query.all()]
            return make_response(jsonify(data), STATUS_OK)
        if request.method == 'POST':
            if name and lat and long:
                print(type(lat))
                if (isinstance(lat, float) or isinstance(lat, int)) and \
                        (isinstance(long, float) or isinstance(long, int)):
                    marker = Marker(name=name, latitude=float(lat), longitude=float(long))
                    db.session.add(marker)
                    db.session.commit()
                    return make_response('Marker Created', STATUS_CREATED)
    else:
        if request.method == 'PUT':
            if name and lat and long:
                if (isinstance(lat, float) or isinstance(lat, int)) and \
                        (isinstance(long, float) or isinstance(long, int)):
                    marker = Marker.query.filter_by(id=id).first()
                    marker.name = name
                    marker.latitude = float(lat)
                    marker.longitude = float(long)
                    db.session.commit()
                    return make_response('Marker Updated', STATUS_UPDATED)
        if request.method == 'DELETE':
            marker = Marker.query.filter_by(id=id).first()
            db.session.delete(marker)
            db.session.commit()
            return make_response('Marker Deleted', STATUS_DELETED)
