from ninja import ModelSchema

from .models import Pet


class CreatePetSchema(ModelSchema):
    class Config:
        model = Pet
        model_fields = ['name', 'description', 'url', 'is_adopted']


class ResponsePetSchema(ModelSchema):
    class Config:
        model = Pet
        model_fields = '__all__'
