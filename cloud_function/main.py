import os

import functions_framework
from flask import Request, Response

from common import Camerge
from common.storage.static_file import ReadOnlyStaticFileStorage

service = Camerge(
    store=ReadOnlyStaticFileStorage(os.getenv("CALENDAR_FILE", default="./calendars.conf.json"))
)


@functions_framework.http
def app(request: Request):
    # version endpoint
    if request.path.startswith("/version"):
        return {'message': 'hello world'}
    # calendar endpoint
    if request.path.find('/calendar/') != -1:
        key = request.path.lstrip('/calendar/')
        ical, error = service.get_for_key(key)
        return Response(ical, mimetype='text/calendar')
    # not found
    return {'message': 'Not Found.'}, 404
