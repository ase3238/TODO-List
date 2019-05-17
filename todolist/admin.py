from django.contrib import admin
from todolist.models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
	list_display = ('title', 'done')
	
admin.site.register(Todo, TodoAdmin)
