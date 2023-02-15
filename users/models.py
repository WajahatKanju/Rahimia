from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

ADMIN = 'ADMIN'
NAZIM_E_TARBIYAT = 'Nazime-Tarbiyat'
TEACHCER = 'Teacher'
MODERATOR = 'Moderator'
CO_ORDINATOR = 'Class Co-oridnator'
IN_ACTIVE = 'Inactive'

ROLES = [
    (ADMIN, 'Admin'),
    (NAZIM_E_TARBIYAT, 'Nazime-Tarbiyat'),
    (TEACHCER, 'Teacher'),
    (MODERATOR, 'Class Moderator'),
    (CO_ORDINATOR, 'Class Co-ordinator'),
    (IN_ACTIVE, 'Inactive'),
    
]


class User(AbstractUser):
    pass


# class Role(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=40, choices=ROLES, default=IN_ACTIVE)
    
#     def __str__(self) -> str:
#         return f'{self.role}'
