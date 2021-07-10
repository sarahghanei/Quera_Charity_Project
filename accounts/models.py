from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER = (
    ('F', 'Female'),
    ('M', 'Male')
)


class User(AbstractUser):
    gender = models.CharField('gender', max_length=1, choices=GENDER, null=True, blank=True)
    phone = models.CharField('phone', max_length=15, null=True, blank=True)
    address = models.TextField('address', null=True, blank=True)
    age = models.PositiveSmallIntegerField('age', null=True, blank=True)
    description = models.TextField('description', null=True, blank=True)


