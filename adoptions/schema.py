from ninja import ModelSchema
from adoptions.models import *

class AdoptionAllSchema(ModelSchema):
    class Config:
        model = Adoption
        model_fields ='__all__'
class CreateAdoptionSchema(ModelSchema):
    class Config:
        model = Adoption
        model_fields=    ["adopter_id" ,
                            "pet_id" ,
                            "rescuer_id" ,
                            "created_at",
                            "updated_at",
                            "deleted"]


