from django.db import models

class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=100, default='Salary')
    date = models.DateField()

    def __str__(self):
        return f"{self.source}: {self.amount}"

class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.category}: {self.amount}"
