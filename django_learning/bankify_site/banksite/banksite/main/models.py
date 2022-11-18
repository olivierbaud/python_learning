from django.db import models

# Create your models here.
class Operations(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10)
    uniqueid = models.IntegerField(unique=True)
    memo = models.CharField(max_length=200)
    amount = models.FloatField()
    category = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.date} {self.memo} {self.amount} '
