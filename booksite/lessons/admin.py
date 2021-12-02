from django.contrib import admin
from .models import *

class LessonsAdmin(admin.ModelAdmin):
    list_display = ('id','thema','content','author','date','category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id','username','password','email','phone_number',)

class TestsAdmin(admin.ModelAdmin):
    list_display = ('id','question','variant1','variant2','variant3','variant4','lesson')

class ResultsAdmin(admin.ModelAdmin):
    list_display = ('id','all_questions','true_ans','false_ans','test_date',)

admin.site.register(Lessons,LessonsAdmin)
admin.site.register(Users,UsersAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tests,TestsAdmin)
admin.site.register(Results,ResultsAdmin)