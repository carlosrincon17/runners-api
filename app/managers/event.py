from managers.base import BaseManager
from models.models import Event


class EventManager(BaseManager):

    def get_event(self, **args):
        events = self.db.query(Event).filter_by(**args).first()
        return events
