from django.urls import path
from .views import *
urlpatterns = [
    path('',LessonsViews.as_view(),name='home')
]