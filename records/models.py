from django.db import models
from django.contrib.auth.models import User

from category.models import MainCategory
from category.models import SubCategory


class Record(models.Model):

    RECORD_TYPES = (
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    record_type = models.CharField(
        max_length=10,
        choices=RECORD_TYPES
    )

    category = models.ForeignKey(
        MainCategory,
        on_delete=models.CASCADE
    )

    sub_category = models.ForeignKey(
        SubCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.CharField(
        max_length=200,
        blank=True
    )

    date = models.DateField()

    def __str__(self):
        return f"{self.record_type} - {self.amount}"