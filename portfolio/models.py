from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Resume(models.Model):
    education = models.TextField()
    experience = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.education

    def save(self, *args, **kwargs):
        return super(Resume, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def _str_(self):
        return self.bio

    def save(self, *args, **kwargs):
        return super(Resume, self).save(*args, **kwargs)
