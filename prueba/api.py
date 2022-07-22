import os
import shutil
from typing import List

import cloudinary
import cloudinary.api
from cloudinary.uploader import upload
from django.contrib.auth.models import User
from ninja import Router
from ninja.files import UploadedFile

from .models import ProfileUser
from .schema import GetProfileSchema, MessageSchema

cloudinary.config(
    cloud_name='ded9hy8uj',
    api_key='713916638845124',
    api_secret='byA-BG2F6ugDBqNRbQpwBG4FwXo',
)

router = Router()


@router.get('/', auth=None, response=List[GetProfileSchema])
def get_all(request):
    profile = ProfileUser.objects.all()
    if len(profile) == 0:
        return MessageSchema
    else:
        return profile


@router.get('/{id}', auth=None, response={200: GetProfileSchema, 404: MessageSchema})
def get_one(request, id: int):
    try:
        profile = ProfileUser.objects.get(pk=id)
        return 200, profile
    except ProfileUser.DoesNotExist:
        return 404, {'message': 'Datos no encontrados'}


@router.post('/{id}', auth=None)
def post_file(request, id: int, file: UploadedFile):
    user = User.objects.get(pk=id)
    file_location = f'photos/{file.name}'
    with open(file_location, 'wb+') as file_object:
        shutil.copyfileobj(file.file, file_object)
    upload(f'{file_location}', folder='img', public_id=f'{user.first_name}{user.last_name}')
    os.remove(f'{file_location}')
    return {'info': f'file "{file.name}" saved at "{file_location}"'}


# @router.put('/{id}', auth=None, response={200: ResponsePutSchema, 404: MessageSchema})
# def put_one_one(request, id: int, data: ProfileUserPutSchema):
#     try:
#         profile = ProfileUser.objects.get(pk=id)
#         profile.phone = data.phone
#         profile.address = data.address
#         profile.about = data.about
#         new_img = cloudinary.api.resources_by_ids(
#             f'img/{profile.user.first_name}{profile.user.last_name}'
#         )['resources'][0]
#         profile.image = new_img['url']
#         profile.save()
#         return 200, profile
#     except ProfileUser.DoesNotExist:
#         return 404, {'message': 'Datos no encontrados'}
