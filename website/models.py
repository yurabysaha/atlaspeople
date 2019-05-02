from django.db import models


class ContactUs(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.name
