
from adoptions.models import *
from ninja import Router

from adoptions.schema import AdoptionAllSchema, CreateAdoptionSchema
from django.contrib.auth.models import User
router = Router()

@router.post('/', summary="Register Adoption",description="Fill" )
def registerAdoption(request,payload: CreateAdoptionSchema):
    Adoption.objects.create(**payload.dict())
    return {"message":"Adoption registered"}

@router.get('/', summary="Get all adoptions",description="Just click",response=list[AdoptionAllSchema] )
def getAllAdoptions(request):
    return Adoption.objects.all()

@router.get('/petId/{petId}',response=list[AdoptionAllSchema] )
def getAllAdoptionsByPetId(request, petId: int):
    return Adoption.objects.filter(pet_id=petId)

@router.get('/adopterId/{adopterId}',response=list[AdoptionAllSchema] )
def getAllAdoptionsByAdopterId(request, adopterId: int):
    return Adoption.objects.filter(adopter_id=adopterId)

@router.get('/rescuerId/{rescuerId}',response=list[AdoptionAllSchema] )
def getAllAdoptionsByRescuerId(request, rescuerId: int):
    return Adoption.objects.filter(rescuer_id=rescuerId)

@router.get('/ownerPet/{email}/{petId}',response=AdoptionAllSchema )
def getAllAdoptions(request,email,petId):
    us=User.objects.get(email=email)
    a=Adoption.objects.first(adopter_id=us.id,pet_id=petId)
    if a!=None:
     return a
    else:
     return {"message": "No es dueño de esta mascota"}