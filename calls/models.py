from django.db import models

# Create your models here.

class Call(models.Model):
    calling_number = models.BigIntegerField()
    called_number = models.BigIntegerField()
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.calling_number} → {self.called_number} ({self.date})"


