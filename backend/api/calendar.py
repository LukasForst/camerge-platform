from fastapi import Response, APIRouter

from common.calendar_service import CalendarService

router = APIRouter()
service = CalendarService()


@router.get("/calendar")
async def calendar():
    """
    This method generates ical data for any calendar app.
    """
    ical = service.get_for_key('')
    return Response(content=ical, media_type='text/calendar')
