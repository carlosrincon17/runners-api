from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Request, UploadFile, Depends, File
from starlette.responses import FileResponse

from app.controllers.event_registration import EventRegistrationController
from app.models.schemas import EventRegistrationSummary, EventRegistrationRow, \
    EventRegistrationFilter, JwtToken, EventRegistrationData
from app.settings import file_settings
from app.utils.decorators import verify_token
from app.utils.file_helper import FileHelper

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


@router.post("/{event_registration_id}/upload-payment", responses={
    HTTPStatus.OK.value: {'model': EventRegistrationData, 'description': 'Event registration data'}
})
async def upload_payment_registration_event(request: Request, event_registration_id: int, file: UploadFile = File(...),
                                            jwt_token: JwtToken = Depends(verify_token)):
    file_path = FileHelper.upload_file(file=file, file_type='payment', object_id=event_registration_id)
    event_registration_controller = EventRegistrationController(request=request)
    await event_registration_controller.upload_payment_to_registration(
        registration_event_id=event_registration_id,
        registration_file=file_path
    )
    return event_registration_controller.get_event_registration_by_id(
        registration_event_id=event_registration_id
    )


@router.put("/{event_registration_id}/approve-payment", responses={
    HTTPStatus.OK.value: {'model': EventRegistrationData, 'description': 'Event registration data'}
})
async def approve_registration_event(request: Request, event_registration_id: int,
                                     jwt_token: JwtToken = Depends(verify_token)):
    event_registration_controller = EventRegistrationController(request=request)
    await event_registration_controller.approve_payment_to_registration(registration_event_id=event_registration_id)
    return event_registration_controller.get_event_registration_by_id(
        registration_event_id=event_registration_id
    )


@router.get("/{event_registration_id}/payment")
async def get_registration_event_payment(request: Request, event_registration_id: int):
    event_registration_controller = EventRegistrationController(request=request)
    event_data = event_registration_controller.get_event_registration_by_id(
        registration_event_id=event_registration_id
    )
    return FileResponse(event_data.payment_file)
