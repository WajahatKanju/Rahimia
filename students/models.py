import uuid

from django.db import models
from administrative_divisions.models import Halqa, Responsibility
from django.utils.translation import gettext_lazy as _

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
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('student_detail', args=[str(self.id)])



class Evaluation_A(models.Model):
    student = models.OneToOneField(Student, verbose_name=_("فارم الیف"), on_delete=models.CASCADE)
    interest_study = models.CharField(max_length=100)
    hold_of_ideology = models.CharField(max_length=100)
    punctuality = models.CharField(max_length=100)
    questioning = models.CharField(max_length=100)
    understanding_stubborn = models.CharField(max_length=100)
    ability_to_expression_of_thoughts = models.CharField(max_length=100)
    social_behaviour = models.CharField(max_length=100)
    discussion = models.CharField(max_length=500)

class Evaluation_B(models.Model):
    student = models.OneToOneField(Student, verbose_name=_("فارم ب"), on_delete=models.CASCADE)
    responsibility = models.ForeignKey(Responsibility, on_delete=models.SET_NULL, null=True)
    management_performance=models.CharField(max_length=100)
    project=models.CharField(max_length=100) # update Foreign
    discussion = models.CharField(max_length=500)

class Evaluation_C(models.Model):
    student = models.OneToOneField(Student, verbose_name=_("فارم ج"), on_delete=models.CASCADE)
    interest_study = models.CharField(max_length=100)
    social_behaviour = models.CharField(max_length=100)
    general_behaviour = models.CharField(max_length=100)
    participation_in_preaching = models.CharField(max_length=100)
    project=models.CharField(max_length=100)    # update Foreign
    resullt = models.BooleanField(default=True)
