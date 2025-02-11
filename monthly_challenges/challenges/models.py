from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Month(models.Model):
    MONTH_CHOICES = [
        (1, "January"), (2, "February"), (3, "March"), (4, "April"), (5, "May"), (6, "June"),
        (7, "July"), (8, "August"), (9, "September"), (10, "October"), (11, "November"), (12, "December")
    ]
    month = models.IntegerField(choices=MONTH_CHOICES)
    year = models.IntegerField(default=2025)
    
    class Meta:
        unique_together = ('month', 'year')
        
    def __str__(self) -> str:
        return f"{self.get_month_display()}-{self.year}"
    
    
class Plan(models.Model):
    month = models.ForeignKey('Month', on_delete=models.CASCADE)
    day = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)])
    title = models.CharField(max_length=200)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('month', 'day', 'title')
        
    def __str__(self) -> str:
        return f"{self.title} - {self.day}/{self.month.month}/{self.month.year}"