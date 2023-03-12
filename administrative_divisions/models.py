import uuid
from django.db import models

# Create your models here.


class Province(models.Model):
    id = models.UUIDField(
        editable=False,
        primary_key=True,
        default=uuid.uuid4
    )
    name = models.CharField(max_length=30)
    president = models.CharField(max_length=60, default='')

    def __str__(self) -> str:
        return self.name


class Region(models.Model):
    id = models.UUIDField(
        editable=False,
        primary_key=True,
        default=uuid.uuid4
    )
    name = models.CharField(max_length=30)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    president = models.CharField(max_length=60, default='')

    def __str__(self) -> str:
        return self.name


class Zone(models.Model):
    id = models.UUIDField(
        editable=False,
        primary_key=True,
        default=uuid.uuid4
    )
    name = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    president = models.CharField(max_length=60, default='')

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    id = models.UUIDField(
        editable=False,
        primary_key=True,
        default=uuid.uuid4
    )
    name = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    president = models.CharField(max_length=60, default='')

    def __str__(self) -> str:
        return self.name


class Halqa(models.Model):
    id = models.UUIDField(
        editable=False,
        primary_key=True,
        default=uuid.uuid4
    )
    name = models.CharField(max_length=30)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    president = models.CharField(max_length=60, default='')


    def __str__(self) -> str:
        return self.name


class Responsibility(models.Model):
    pass