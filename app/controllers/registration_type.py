from controllers.base import BaseController
from managers.registration_type import RegistrationTypeManager
from models.schemas import UserCreate


class RegistrationTypeController(BaseController):

    def get_registration_types(self):
        registration_type_manager = RegistrationTypeManager(self.request)
        return registration_type_manager.get_registration_types(status='ACTIVE')




