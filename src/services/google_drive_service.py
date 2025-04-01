import os
import tempfile

from cloud.google_drive_interface import GoogleDriveInterface


class GoogleDriveService:
    def __init__(self, uploader: GoogleDriveInterface):
        self.uploader = GoogleDriveInterface()
    
    def upload_blob(self, upload_file):
         # Save the uploaded file temporarily
        try:
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                contents = upload_file.file.read()
                tmp.write(contents)
                tmp_path = tmp.name

            # Upload the file using GoogleDriveUploader
            file_id = self.uploader.upload_file(tmp_path, upload_file.filename, upload_file.content_type)
        finally:
            # Ensure the temporary file is removed.
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
        return file_id


    def get_blob(self, blob):
        pass