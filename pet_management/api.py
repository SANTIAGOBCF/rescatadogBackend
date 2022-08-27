from django.shortcuts import get_object_or_404
from ninja import Router

from .models import Pet, PetCategory, PetProfile
from .schema import (
    CreatePetCategorySchema,
    CreatePetSchema,
    ResponseAllPetSchema,
    ResponsePetCategorySchema,
    ResponsePetSchema,
    ResponsePetSearch,
)

router = Router()


@router.get('', response=list[ResponseAllPetSchema])
def get_pets(request):
    return Pet.objects.all()

@router.get('/notAdopted', response=list[ResponseAllPetSchema])
def get_petsNotAdopted(request):
    return Pet.objects.filter(is_adopted=False)

@router.put('/{pet_id}/adopt', response=ResponseAllPetSchema)
def put_adopt(request, pet_id: int):
    updatePet= Pet.objects.get(id=pet_id)
    updatePet.is_adopted=True
    updatePet.save()
    return updatePet

@router.post('', response=ResponsePetSchema)
def create(request, payload: CreatePetSchema):
    pet_category = PetCategory.objects.get(pk=payload.pet_category)
    pet_profile = PetProfile(
        gender=payload.gender,
        age=payload.age,
        location=payload.location,
        color=payload.color,
        deleted=False,
    )
    pet_profile.save()
    pet = Pet(
        name=payload.name,
        description=payload.description,
        url=payload.url,
        is_adopted=False,
        pet_category=pet_category,
        pet_profile=pet_profile,
        deleted=False,
    )
    pet.save()
    return pet


@router.post('/category', response=ResponsePetCategorySchema)
def create_category(request, payload: CreatePetCategorySchema):
    pet_category = PetCategory(name=payload.name, image=payload.image, deleted=False)
    pet_category.save()
    return pet_category


@router.get('/category', response=list[ResponsePetCategorySchema])
def get_categories(request):
    pet_categories = PetCategory.objects.all()
    return pet_categories


@router.get('/{pet_id}', response=ResponsePetSchema)
def get_by_id(request, pet_id: int):
    if pet_id == 0:
        pet = Pet.objects.latest('id')
        return pet
    pet = get_object_or_404(Pet, id=pet_id)
    return pet


# agregado
@router.get('/pet/search', auth=None, response=list[ResponsePetSearch])
def pet_search(request, name):
    pet = Pet.objects.filter(name__icontains=f'{name}')
    return pet
