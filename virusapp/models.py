from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=30)
    sneezing = models.BooleanField(default=False)
    run_nose = models.BooleanField(default=False)
    fatigue = models.BooleanField(default=False)
    dry_cough = models.BooleanField(default=False)
    fever = models.BooleanField(default=False)
    sour_throat = models.BooleanField(default=False)
    breathing = models.BooleanField(default=False)
    cases_around = models.BooleanField(default=False)
    sick_frequency = models.CharField(max_length=30)
    pneumonia = models.BooleanField(default=False)

    def __str__(self):
        return self.name