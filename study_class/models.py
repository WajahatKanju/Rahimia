import uuid
from django.db import models
from students.models import Student
from teachers.models import Teacher

class StudyClass(models.Model):
  id  = models.UUIDField(
    default=uuid.uuid4,
    primary_key=True,
    editable=False
  )
  no = models.IntegerField(name='class no')
  name = models.CharField(max_length=60)
  title = models.CharField(max_length=256)
  semester = models.IntegerField(name='Semester no',)
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  moderator = models.CharField(max_length=60,)  
  
  

class Participant(models.Model):
  id  = models.UUIDField(
    default=uuid.uuid4,
    primary_key=True,
    editable=False
  )
  study_class = models.ForeignKey(StudyClass, on_delete=models.CASCADE, blank=True)
  participant = models.ForeignKey(Student, on_delete=models.CASCADE)
  was_preasent = models.BooleanField()
  
  def __str__(self) -> str:
    return f"{self.participant.first_name} {self.participant.last_name}"
  