from django.contrib import admin
from .models import MyCar, Comment, Category

admin.site.register(Comment)
admin.site.register(MyCar)
admin.site.register(Category)
# Register your models here.
