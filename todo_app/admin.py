from django.contrib import admin
from .models import Todo

class ShowCreated(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo, ShowCreated)
