import functions_framework
from flask import Request

from common.calendar_service import CalendarService

service = CalendarService()


@functions_framework.http
def app(request: Request):
    if request.path.startswith("/hello"):
        return {'message': 'hello world'}
    else:
        return service.get_for_key('')
