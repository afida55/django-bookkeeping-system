from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class BankCard(models.Model):

    CARD_TYPES = (
        ('Visa', 'Visa'),
        ('MasterCard', 'MasterCard'),
        ('UnionPay', 'UnionPay'),
        ('American Express', 'American Express'),
    )

    CARD_COLORS = (
        ('purple', 'Purple'),
        ('blue', 'Blue'),
        ('black', 'Black'),
        ('green', 'Green'),
        ('red', 'Red'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    bank_name = models.CharField(max_length=100)

    card_holder = models.CharField(max_length=100)

    card_number = models.CharField(max_length=19)

    expiry_date = models.CharField(max_length=5)   # Example: 12/28

    card_type = models.CharField(
        max_length=20,
        choices=CARD_TYPES,
        default='Visa'
    )

    card_color = models.CharField(
        max_length=20,
        choices=CARD_COLORS,
        default='purple'
    )

    is_default = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bank_name} - {self.card_holder}"


class SavingsGoal(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    goal_name = models.CharField(max_length=100)

    target_amount = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.goal_name