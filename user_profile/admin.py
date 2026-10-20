from django.contrib import admin
from .models import Profile, BankCard, SavingsGoal

admin.site.register(Profile)
admin.site.register(BankCard)
admin.site.register(SavingsGoal)