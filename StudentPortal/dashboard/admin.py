from django.contrib import admin
from . models import *

# Register your models here.
# admin.site.register(Notes)
# admin.site.register(Homework)
# admin.site.register(Todo)

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "date")

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ("subject", "title", "description", "date", "is_finished")


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "is_finished")
