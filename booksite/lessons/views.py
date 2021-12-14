from django.shortcuts import render
from django.views.generic import ListView,DetailView

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
    context_object_name = 'categories'

class SubcategoryListViews(DetailView):
    model = SubCategory
    template_name = 'lessons/base2.html'
    context_object_name = 'subcategories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategory'] = SubCategory.objects.all()
        context['categories'] = Category.objects.all()
        return context


class SubcategoryDetailView(DetailView):
    model = SubCategory
    template_name = 'lessons/lesson.html'
    context_object_name = 'lessons'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['subcategory'] = SubCategory.objects.all()
        context['categories'] = Category.objects.all()
        context['lesson'] = Lessons.objects.get(subcategory__id = pk)
        return context