from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = "users"

    email = models.CharField(max_length=256)
    password = models.CharField(max_length=256)

