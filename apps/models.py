from django.db import models


class Advisor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='advisors/%Y/%m/%d/')
