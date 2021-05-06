from django.contrib import admin
from Testapp.models import Movie

# Register your models here.
class MovieReg(admin.ModelAdmin):
    list_display=['name','date','hero','heroine','ratings']
admin.site.register(Movie,MovieReg)
