from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Request
from fastapi.params import Depends

from app.controllers.event_registration import EventRegistrationController
from app.controllers.registration_type import RegistrationTypeController
from app.models.schemas import RegistrationTypeBase, EventRegistrationSummary, EventRegistrationRow, \
    EventRegistrationFilter, JwtToken, EventRegistrationData
from app.utils.decorators import verify_token

router = APIRouter()


@router.get("/summary", responses={
    HTTPStatus.OK.value: {'model': List[EventRegistrationSummary], 'description': 'Event registration summary data'}
})
async def get_event_registration(request: Request):
    event_registration_controller = EventRegistrationController(request=request)
    return event_registration_controller.get_summary()


@router.post("/filter", responses={
    HTTPStatus.OK.value: {'model': List[EventRegistrationRow], 'description': 'Event registration row data'}
})
async def get_event_registration(request: Request, event_registration_filter: EventRegistrationFilter):
    event_registration_controller = EventRegistrationController(request=request)
    return event_registration_controller.get_event_registration_by_status(
        status=event_registration_filter.status
    )


@router.get("/", responses={
    HTTPStatus.OK.value: {'model': EventRegistrationData, 'description': 'Event registration data'}
})
async def get_event_registration(request: Request, jwt_token: JwtToken = Depends(verify_token)):
    event_registration_controller = EventRegistrationController(request=request)
    return event_registration_controller.get_event_registration_by_user(
        user_id=jwt_token.user_id
    )


@router.put("{event_registration_id}/upload-payment", responses={
    HTTPStatus.OK.value: {'model': EventRegistrationData, 'description': 'Event registration data'}
})
async def upload_payment_registration_event(request: Request, event_registration_id: int,
                                            jwt_token: JwtToken = Depends(verify_token)):
    event_registration_controller = EventRegistrationController(request=request)
    event_registration_controller.get_event_registration_by_id(
        registration_event_id=event_registration_id
    )


@router.put("{event_registration_id}/approve-payment", responses={
    HTTPStatus.OK.value: {'model': EventRegistrationData, 'description': 'Event registration data'}
})
async def upload_payment_registration_event(request: Request, event_registration_id: int,
                                            jwt_token: JwtToken = Depends(verify_token)):
    event_registration_controller = EventRegistrationController(request=request)
    return event_registration_controller.get_event_registration_by_id(
        registration_event_id=event_registration_id
    )
