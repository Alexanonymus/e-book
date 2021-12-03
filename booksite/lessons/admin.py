from django.contrib import admin
from .models import *

class LessonsAdmin(admin.ModelAdmin):
    list_display = ('id','thema','content','author','date',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id','username','password','email','phone_number',)

class TestsAdmin(admin.ModelAdmin):
   pass
class ResultsAdmin(admin.ModelAdmin):
   pass

class SubCategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Lessons,LessonsAdmin)
admin.site.register(Users,UsersAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tests,TestsAdmin)
admin.site.register(Results,ResultsAdmin)