from managers.base import BaseManager
from models.models import RegistrationType


class RegistrationTypeManager(BaseManager):

    def get_registration_types(self, **args):
        registration_types = self.db.query(RegistrationType).filter_by(**args).all()
        return registration_types
