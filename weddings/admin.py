from django.contrib import admin

from .models import Event, Guest, CodeGuess, GuestEvent
from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin

class GuestResource(ModelResource):

    class Meta:
        model = Guest

class InviteInline(admin.TabularInline):
    model = Guest.events.through
    extra = 2

class GuestAdmin(ImportMixin, admin.ModelAdmin):
    # filter_horizontal = ('invites',)
    inlines = [InviteInline,]
    list_display = ('full_name', 'full_name_2', 'side', 'relation', 'get_events' )
    list_filter = ['side', 'relation', 'events']
    ordering = ('last_name',)

    def get_events(self, obj):
        return ", ".join([e.short for e in obj.events.all()])
    pass

admin.site.register(Event)
admin.site.register(Guest, GuestAdmin)
admin.site.register(CodeGuess)

# Register your models here.
