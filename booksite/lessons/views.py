from django.shortcuts import render
from .models import *
# Create your views here.
from django.views.generic import ListView


class LessonsViews(ListView):
    model = Lessons
    template_name = 'lessons/index.html'


class CategoryViews(ListView):
    model = Category
    template_name = 'lessons/index.html'


class SubCategoryViews(ListView):
    model = SubCategory
    template_name = 'lessons/index.html'