from django.urls import path
from .views import *
urlpatterns = [
    path('', CategoryListViews.as_view(),name='home'),
    path('<int:pk>', SubcategoryListViews.as_view(),name='category_detail'),
    path('lesson/<int:pk>', SubcategoryDetailView.as_view(),name='subcategory_detail'),

]