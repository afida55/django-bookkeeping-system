from django.db import models
from django.contrib.auth.models import User


class MainCategory(models.Model):

    CATEGORY_TYPES = (
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    )

    name = models.CharField(max_length=50)

    category_type = models.CharField(
        max_length=10,
        choices=CATEGORY_TYPES,
        default='Expense'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} ({self.category_type})"

    class Meta:
        verbose_name = "Main Category"
        verbose_name_plural = "Main Categories"

        constraints = [
            models.UniqueConstraint(
                fields=["user", "name", "category_type"],
                name="unique_user_category"
            )
        ]


class SubCategory(models.Model):

    name = models.CharField(max_length=50)

    main_category = models.ForeignKey(
        MainCategory,
        on_delete=models.CASCADE,
        related_name='subcategories'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"