from typing import List

from app.controllers.base import BaseController
from app.managers.event_registration import EventRegistrationManager
from app.managers.registration_type import RegistrationTypeManager
from app.models.schemas import EventRegistrationSummary, EventRegistrationRow, EventRegistrationData


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

    def upload_payment_to_registration(self, registration_event_id: int) -> EventRegistrationData:
        event_registration_manager = EventRegistrationManager(self.request)
        return event_registration_manager.update_registration_event_status(
            registration_event_id=registration_event_id,
            new_status="VALIDACIÓN DE PAGO PENDIENTE"
        )

    def approve_payment_to_registration(self, registration_event_id: int) -> EventRegistrationData:
        event_registration_manager = EventRegistrationManager(self.request)
        return event_registration_manager.update_registration_event_status(
            registration_event_id=registration_event_id,
            new_status="INSCRIPCIÓN FINALIZADA"
        )




