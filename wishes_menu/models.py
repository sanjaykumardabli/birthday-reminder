from django.db import models

# Create your models here.

class Birthday(models.Model):
    name = models.CharField(max_length=125)
    nick_name = models.CharField(max_length=125)
    d_o_b = models.DateTimeField()
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    

class EmailBroadcast(models.Model):
    name = models.CharField(max_length=125)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
