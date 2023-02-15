import uuid

from django.db import models
from administrative_divisions.models import Halqa
from django.urls import reverse


class Student(models.Model):
    id = models.UUIDField(
        editable=False,
        primary_key=True,
        default=uuid.uuid4
    )
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, default=None, blank=True)
    last_name = models.CharField(max_length=30)

    picture = models.ImageField(
        default="default/blank_profile.webp", upload_to="images/profile", blank=True)

    father_first_name = models.CharField(max_length=30)
    father_middle_name = models.CharField(
        max_length=30, default=None, blank=True)
    father_last_name = models.CharField(max_length=30)

    date_of_birth = models.DateField()
    date_of_registration = models.DateField()

    CNIC = models.CharField(max_length=13)
    CNIC_picture = models.ImageField(
        default="default/blank_cnic.jpg", upload_to="images/CNIC", blank=True)
    phone = models.CharField(max_length=11)

    education = models.CharField(max_length=300)
    occupation = models.CharField(max_length=300)

    current_address = models.CharField(max_length=300)
    permanent_address = models.CharField(max_length=300)

    halqa = models.ForeignKey(Halqa, on_delete=models.CASCADE, default=None)
    

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('student_detail', args=[str(self.id)])
