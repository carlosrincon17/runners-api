from app.controllers.base import BaseController
from app.managers.registration_type import RegistrationTypeManager


class RegistrationTypeController(BaseController):

    def get_registration_types(self):
        registration_type_manager = RegistrationTypeManager(self.request)
        return registration_type_manager.get_registration_types(status='ACTIVE')




