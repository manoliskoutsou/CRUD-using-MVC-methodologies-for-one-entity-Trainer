from django.db import models

class Trainer(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)
    

    



