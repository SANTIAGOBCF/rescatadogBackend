from typing import List

from ninja import Router

from .models import ProfileUser
from .schema import (  # ResponsePutSchema,
    GetProfileSchema,
    MessageSchema,
    ProfileUserPutSchema,
)

# from ninja.files import UploadedFile


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


@router.put('/{id}', response={200: MessageSchema, 404: MessageSchema})
def put_one(request, id: int, data: ProfileUserPutSchema):
    try:
        profile = ProfileUser.objects.get(pk=id)
        profile.phone = data.phone
        profile.address = data.address
        profile.about = data.about
        profile.image = data.image
        profile.save()
        return 200, {'message': 'Datos modificados'}
    except ProfileUser.DoesNotExist:
        return 404, {'message': 'Datos no encontrados'}
