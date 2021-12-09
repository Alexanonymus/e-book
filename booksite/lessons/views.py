from django.shortcuts import render
from django.views.generic import ListView

from .models import *
# # Create your views here.
# from django.views.generic import ListView,DetailView
#
#
# class LessonsViews(ListView):
#     model = Lessons
#     template_name = 'lessons/index.html'
#     context_object_name = 'lessons'
#
# class CategoryViews(ListView):
#     model = Category
#     template_name = 'lessons/index.html'
#
#
# class SubCategoryViews(ListView):
#     model = SubCategory
#     template_name = 'lessons/index.html'
#
# class LessonBySubCategory(DetailView):
#     model = Lessons
#     template_name = 'lessons/lessonbysubcat.html'
#     context_object_name = 'lesson'
#     paginate_by = 1
class CategoryListViews(ListView):
    model = Category
    template_name = 'lessons/base.html'
    context_object_name =
