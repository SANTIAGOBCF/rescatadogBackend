from re import T
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from ninja.security import HttpBearer
from auth.api import router as auth_router
from adoptions.api import router as adoptions_router
from django.contrib.auth.models import User

from auth.token import verify_token
class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        em=verify_token(token)
        user=User.objects.filter(email=em).first()
        if user is not None:
            return token


api = NinjaAPI(version='1.0.0',auth=GlobalAuth())

@api.get("/", summary="Hello api 1.00",description="API 1.00")
def add(request):
    return {"message": "Hello api 1.00"}


api.add_router("/auth/", auth_router,tags=["auth"])
api.add_router("/adoptions/", adoptions_router,tags=["adoptions"])

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
