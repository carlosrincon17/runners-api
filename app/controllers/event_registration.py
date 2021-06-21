from app.constants.registration_event import RegistrationEventStatus
from typing import List

from app.controllers.base import BaseController
from app.managers.event_registration import EventRegistrationManager
from app.managers.registration_type import RegistrationTypeManager
from app.managers.user import UserManager
from app.models.schemas import EventRegistrationSummary, EventRegistrationRow, EventRegistrationData
from app.utils.mail_helper import MailHelper


class EventRegistrationController(BaseController):

    def get_summary(self) -> List[EventRegistrationSummary]:
        event_registration_manager = EventRegistrationManager(self.request)
        return event_registration_manager.get_summaries()

    def get_event_registration_by_status(self, status: str) -> List[EventRegistrationRow]:
        event_registration_manager = EventRegistrationManager(self.request)
        return event_registration_manager.get_by_status(status=status)

    def get_event_registration_by_user(self, user_id: int) -> EventRegistrationData:
        event_registration_manager = EventRegistrationManager(self.request)
        return event_registration_manager.get_by_user_id(user_id=user_id)

    def get_event_registration_by_id(self, registration_event_id: int) -> EventRegistrationData:
        event_registration_manager = EventRegistrationManager(self.request)
        return event_registration_manager.get_by_id(registration_event_id=registration_event_id)

    async def upload_payment_to_registration(self, registration_event_id: int,
                                             registration_file: str) -> EventRegistrationData:
        event_registration_manager = EventRegistrationManager(self.request)
        return event_registration_manager.update_registration_event_status(
            registration_event_id=registration_event_id,
            registration_file=registration_file,
            new_status=RegistrationEventStatus.PENDING_PAYMENT_VALIDATION
        )

    async def approve_payment_to_registration(self, registration_event_id: int) -> EventRegistrationData:
        event_registration_manager = EventRegistrationManager(self.request)
        user_registration = UserManager(self.request).get_user_by_event_registration_id(
            event_registration_id=registration_event_id
        )
        registration_data = {
            'first_name': user_registration.first_name,
        }
        await MailHelper().send_registration_email(
            registration_data=registration_data,
            user_email=user_registration.email
        )
        return event_registration_manager.update_registration_event_status(
            registration_event_id=registration_event_id,
            new_status=RegistrationEventStatus.REGISTRATION_FINISHED
        )


