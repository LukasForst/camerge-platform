import os

from fastapi import APIRouter, Response

from common import Camerge
from common.storage.static_file import ReadOnlyStaticFileStorage

router = APIRouter()
service = Camerge(
    store=ReadOnlyStaticFileStorage(os.getenv("CALENDAR_FILE", default="./calendars.conf.json"))
)


@router.get("/version")
async def version():
    return {'message': 'hello world!'}


@router.get("/calendar/{key}")
async def get_calendar(key: str):
    """
    This method generates ical data for any calendar app.
    """
    ical, error = service.get_for_key(key)
    return Response(content=ical, media_type='text/calendar')
