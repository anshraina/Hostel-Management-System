from django.contrib import admin
from .models import Student
# Register your models here.


class NewEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'stud_id')


admin.site.register(Student, NewEntryAdmin)
