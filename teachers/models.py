import uuid

from django.db import models
from django.urls import reverse
from administrative_divisions.models import Halqa


class Teacher(models.Model):
    id = models.UUIDField(
        editable=False,
        primary_key=True,
        default=uuid.uuid4
    )

    registration_no = models.CharField(
        max_length=8,
        unique=True        
    )

    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)

    father_first_name = models.CharField(max_length=30)
    father_middle_name = models.CharField(max_length=30, blank=True)
    father_last_name = models.CharField(max_length=30)
    
    date_of_birth = models.DateField()
    date_of_registration = models.DateField()
    date_of_appointment = models.DateField()


    CNIC = models.CharField(max_length=13)
    halqa = models.ForeignKey(Halqa, on_delete=models.CASCADE)
    quality = models.CharField(max_length=100)


    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('teacher_detail', args=[str(self.id)])
    

class Sectrary(Teacher):
    pass