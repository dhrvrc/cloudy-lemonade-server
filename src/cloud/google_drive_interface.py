import os

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


class GoogleDriveInterface:
    def __init__(self):
        self.service = self.authenticate()

    def authenticate(self):
        creds, _ = google.auth.default()
        return build('drive', 'v3', credentials=creds)

    def upload_file(self, file_path, mime_type='application/octet-stream'):
        file_metadata = {'name': os.path.basename(file_path)}
        media = MediaFileUpload(file_path, mimetype=mime_type)
        try:
            file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print(f'File ID: {file.get("id")}')
            return file.get('id')
        except HttpError as error:
            print(f'An error occurred: {error}')
            return None