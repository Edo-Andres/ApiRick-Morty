from django.contrib import admin
from django.urls import path

from api.views import verCharacteres, getApi

urlpatterns = [
    path('char/', verCharacteres, name='char'),
    path('', getApi, name='api'),
]
