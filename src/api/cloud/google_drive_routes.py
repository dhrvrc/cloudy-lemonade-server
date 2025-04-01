from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from services.google_drive_service import GoogleDriveService
from cloud.google_drive_interface import GoogleDriveInterface


router = APIRouter()

@router.post("/upload")
async def upload_file():
    return GoogleDriveService.upload_blob(db, filename, file_path, metadata, secure_group_id)


@router.get("/drive-all")
async def get_all_drive_files():
    return {"message": "Google Drive interface"}

@router.get("/drive/{file_id}")
async def get_specific_drive_file():
    return {"message": "Google Drive interface"} 

