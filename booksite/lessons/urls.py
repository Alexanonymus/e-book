from django.urls import path
from .views import *
urlpatterns = [
    path('',LessonsViews.as_view(),name='home'),
    path('category/<int:category_id>/',CategoryViews.as_view(),name='category'),


]