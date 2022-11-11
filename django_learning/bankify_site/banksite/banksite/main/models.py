from django.db import models

# Create your models here.
class Operations(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10)
    uniqueid = models.IntegerField()
    memo = models.CharField(max_length=200)
    amount = models.DecimalField(decimal_places=2, max_digits=5)
    category = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.date} {self.memo} {self.amount} '
