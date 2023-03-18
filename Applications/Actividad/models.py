from django.db import models

# Create your models here.
class Activity(models.Model):
    group = models.CharField(max_length=30)
    activities = models.CharField(max_length=60)
    date = models.DateField()

    def __str__(self) -> str:
        text = "{0} ({1})"
        return text.format(self.activities, self.date)