from datetime import datetime

from managers.base import BaseManager
from models.models import EventRegistration


class EventRegistrationManager(BaseManager):

    def create_event_registration(self, user_id, registration_type_id, event_id):
        event_registration = EventRegistration(
            user_id=user_id,
            registration_type_id=registration_type_id,
            enrollment_date=datetime.utcnow(),
            event_id=event_id,
            status='PAGO PENDIENTE'
        )
        self.db.add(event_registration)
        self.db.flush()
