from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from ninja import Router
from ninja.errors import HttpError

from auth.schema import CreateUserSchema, LoginUserSchema
from auth.token import create_access_token
from prueba.models import ProfileUser

router = Router()


@router.post('/token', summary='Get token', description='Username and password are required')
def token(request, userLogin: LoginUserSchema):
    user = authenticate(username=userLogin.username, password=userLogin.password)
    if user is not None:
        access_token = create_access_token(data={'sub': user.email})
        return {'access_token': access_token, 'token_type': 'bearer'}
    else:
        raise HttpError(404, 'Invalid Credentials')


@router.post('/register', summary='Register user', description='Fill all fields')
def register(request, payload: CreateUserSchema):
    usuario = User.objects.create_user(**payload.dict())
    usuario
    ProfileUser.objects.create(user=usuario)
    return {'message': 'Registered'}
