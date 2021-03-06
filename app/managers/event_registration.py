from app.constants.registration_event import RegistrationEventStatus
from datetime import date
from typing import List

from sqlalchemy import func

from app.managers.base import BaseManager
from app.models.models import EventRegistration, User, RegistrationType, Event
from app.models.schemas import EventRegistrationSummary, EventRegistrationRow, EventRegistrationData


class EventRegistrationManager(BaseManager):

    def create_event_registration(self, user_id, registration_type_id, event_id):
        event_registration = EventRegistration(
            user_id=user_id,
            registration_type_id=registration_type_id,
            enrollment_date=date.today(),
            event_id=event_id,
            status=RegistrationEventStatus.PENDING_PAYMENT
        )
        self.db.add(event_registration)
        self.db.flush()

    def get_summaries(self) -> List[EventRegistrationSummary]:
        summary_data = self.db.query(
            EventRegistration.status,
            func.count(EventRegistration.id).label('total')
        ).group_by(
            EventRegistration.status
        ).all()
        return [
            EventRegistrationSummary(
                status=summary_row.status,
                total=summary_row.total
            )
            for summary_row in summary_data
        ]

    def get_by_status(self, status: str) -> List[EventRegistrationRow]:
        query_result = self.db.query(
            EventRegistration,
            User,
            RegistrationType,
            Event
        ).filter(
            EventRegistration.status == status,
            EventRegistration.registration_type_id == RegistrationType.id,
            EventRegistration.user_id == User.id,
            EventRegistration.event_id == Event.id
        ).all()
        event_registration_rows: List[EventRegistrationRow] = []
        for event_registration, user, registration_type, event in query_result:
            event_registration_rows.append(
                EventRegistrationRow(
                    first_name=user.first_name,
                    last_name=user.last_name,
                    user_id=user.id,
                    gender=user.gender,
                    shirt_size=user.shirt_size,
                    event_registration_id=event_registration.id,
                    registration_type_id=registration_type.id,
                    registration_type_amount=registration_type.amount,
                    document_number=user.document_number,
                    distance=event.distance
                )
            )
        return event_registration_rows

    def get_by_user_id(self, user_id: int) -> EventRegistrationData:
        event_registration, registration_type, event = self.db.query(
            EventRegistration,
            RegistrationType,
            Event
        ).filter(
            EventRegistration.user_id == user_id,
            EventRegistration.registration_type_id == RegistrationType.id,
            EventRegistration.user_id == User.id,
            EventRegistration.event_id == Event.id
        ).first()
        return EventRegistrationData(
            distance=event.distance,
            amount=registration_type.amount,
            status=event_registration.status,
            id=event_registration.id,
            registration_type_id=registration_type.id,
        )

    def get_by_id(self, registration_event_id: int) -> EventRegistrationData:
        event_registration, registration_type, event, user = self.db.query(
            EventRegistration,
            RegistrationType,
            Event,
            User
        ).filter(
            EventRegistration.id == registration_event_id,
            EventRegistration.registration_type_id == RegistrationType.id,
            EventRegistration.user_id == User.id,
            EventRegistration.event_id == Event.id
        ).first()
        return EventRegistrationData(
            distance=event.distance,
            amount=registration_type.amount,
            status=event_registration.status,
            id=event_registration.id,
            registration_type_id=registration_type.id,
            payment_file=event_registration.payment_evidence,
            user=user
        )

    def update_registration_event_status(self, registration_event_id: int, new_status: str,
                                         registration_file: str = None):
        event_registration = self.db.query(
            EventRegistration
        ).filter(
            EventRegistration.id == registration_event_id
        ).first()
        event_registration.status = new_status
        if registration_file:
            event_registration.payment_evidence = registration_file
        self.db.flush()
