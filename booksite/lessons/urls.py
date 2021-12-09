from django.urls import path
from .views import *
urlpatterns = [
    path('', CategoryListViews.as_view(),name='home'),

]