import  os

from fastapi import UploadFile
from app.settings import file_settings


class FileHelper:

    @staticmethod
    def upload_file(file: UploadFile, file_type: str, object_id: int):
        folder = '{}/{}/{}'.format(file_settings.path, file_type, str(object_id))
        if not os.path.exists(folder):
            os.makedirs(folder)
        file_location = '{}/{}'.format(folder, file.filename)
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
        return file_location
