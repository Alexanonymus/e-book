from django.db import models

# Create your models here.
# bizda asosan quyidagi modellar bo`ladi
from django.urls import reverse

'''
Users
    username
    password
    email
    phone_number

============   
# Category
    name
=========
#SubCategory
    name
    category
==========
#lessons

    thema
    content
    author
    date
    
    SubCategory
============
# tests
     question
     variant 1
     variant 2
     variant 3
     variant 4
    
     lesson
==========
# results
     
     password
     all_questions
     true_ans
     false_ans
     test_date
     
     username
     test
     
'''
class Users(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,)

    def get_absolute_url2(self):
        return reverse('subcategory',kwargs={'subcategory_id': self.pk})

class Lessons(models.Model):
    thema = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)

    subcategory = models.ForeignKey('SubCategory',on_delete=models.CASCADE,)




    def __str__(self):
        return self.thema

class Tests(models.Model):
    question = models.CharField(max_length=300)
    variant1 = models.CharField(max_length=400)
    variant2 = models.CharField(max_length=400)
    variant3 = models.CharField(max_length=400)
    variant4 = models.CharField(max_length=400)

    lesson = models.ForeignKey('Lessons', on_delete=models.CASCADE,)

    def __str__(self):
        return self.question

class Results(models.Model):
    all_questions = models.IntegerField()
    true_ans = models.IntegerField()
    false_ans = models.IntegerField()
    test_date = models.DateField(auto_now_add=True)

    username = models.ForeignKey('Users', on_delete=models.CASCADE,)
    lesson = models.ForeignKey('Lessons', on_delete=models.CASCADE, blank = True, null=True)

    def __str__(self):
        return self.username

