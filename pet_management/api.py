from django.shortcuts import get_object_or_404
from ninja import Router

from .models import Pet
from .schema import CreatePetSchema, ResponsePetSchema

router = Router()


@router.post('', response=ResponsePetSchema)
def create(request, payload: CreatePetSchema):
    pet = Pet.objects.create(**payload.dict())
    return pet


@router.get('/{pet_id}', response=ResponsePetSchema)
def get_by_id(request, pet_id: int):
    pet = get_object_or_404(Pet, id=pet_id)
    return pet
