from django.contrib import admin
from app01 import models

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "sex", "class_null"]
    list_editable = ["name", "sex", "class_null"]

admin.site.register(models.Student, StudentAdmin)