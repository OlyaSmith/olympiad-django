from django.contrib import admin
from .models import Participant

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'university', 'course', 'registered_at')
    list_filter = ('university', 'course')
    search_fields = ('name', 'email')