from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Request

from app.controllers.registration_type import RegistrationTypeController
from app.models.schemas import RegistrationTypeBase

router = APIRouter()


@router.get("", responses={
    HTTPStatus.OK.value: {'model': List[RegistrationTypeBase],
                          'description': 'List of registration types actived in the system'
                          },
})
async def get_registration_types(request: Request):
    registration_type_controller = RegistrationTypeController(request=request)
    return registration_type_controller.get_registration_types()
