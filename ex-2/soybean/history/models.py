from django.db import models

# Create your models here.

"""
Example Soybean Condition Data Row:

Week Ending: 12/07/2020
Condition: Poor
Average Temperature: 22.4
Grade: 5
Inspector: 'Fred Bloggs'

PLEASE NOTE: For 'Condition', choices can be from 'Very Poor', 'Poor', 'Fair',
 'Good', 'Excellent'
"""


class SoybeanCondition(models.Model):
    class Condition(models.TextChoices):
        VERY_POOR = 'Very Poor', 'Very Poor'
        POOR = 'Poor', 'Poor'
        FAIR = 'Fair', 'Fair'

    week_ending = models.DateField()
    condition = models.CharField(choices=Condition.choices, max_length=30)
    average_temperature = models.DecimalField(max_digits=4, decimal_places=1)
    grade = models.IntegerField()
    inspector = models.CharField(max_length=50)
