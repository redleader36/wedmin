from django.contrib import admin

from .models import Event, Guest, CodeGuess

admin.site.register(Event)
admin.site.register(Guest)
admin.site.register(CodeGuess)

# Register your models here.
