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
        return f'{self.date} {self.memo} {self.amount}'
    
    def categorize(self, keywords):
        print(keywords)
        for keyword in keywords:
            if keyword.keyword in self.memo:
                self.category = keyword.category


class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f'{self.name}'
    
    def add_category(self, category):
        self.name = category
        
class Keywords(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.keyword}'
    
    def add_keyword(self, keyword, category):
        self.keyword = keyword