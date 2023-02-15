from django.contrib import admin
from .models import StudyClass, Participant


class ParticipantInline(admin.TabularInline):
  model = Participant


@admin.register(StudyClass)
class StudentClassAdmin(admin.ModelAdmin):
  inlines = [
    ParticipantInline
  ]