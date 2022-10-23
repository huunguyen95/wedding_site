from django.db import models

# Create your models here.
guest_list = ["name","phone","number_of_guest","attending","message","created"]

class Guest(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=500, null=True, blank=True)
    number_of_guest = models.CharField(max_length=200)
    attending = models.TextField(null=True, blank=True)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name