from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    email = models.EmailField("correo", unique=True)
    last_name2 = models.CharField(max_length=30)
    es_matrona = models.BooleanField(default=False)
    es_supervisor = models.BooleanField(default=False)

    def __str__(self):
        return self.get_full_name()


    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name} {self.last_name2}"
        return full_name.strip()