from django import forms
from django.contrib.auth.models import User
from .models import Profile, BankCard, SavingsGoal


# ---------------- PROFILE ----------------
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'profile_pic', 'bio']

        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


# ---------------- USER ----------------
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


# ---------------- BANK CARD ----------------
class BankCardForm(forms.ModelForm):
    class Meta:
        model = BankCard
        exclude = ['user']
        widgets = {
            'bank_name': forms.TextInput(attrs={'class': 'form-control'}),
            'card_holder': forms.TextInput(attrs={'class': 'form-control'}),
            'card_number': forms.TextInput(attrs={'class': 'form-control'}),
            'expiry_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM/YY'}),
            'card_type': forms.Select(attrs={'class': 'form-control'}),
            'card_color': forms.Select(attrs={'class': 'form-control'}),
        }

# ---------------- SAVINGS GOAL ----------------
class SavingsGoalForm(forms.ModelForm):
    class Meta:
        model = SavingsGoal
        exclude = ['user']
        widgets = {
            'goal_name': forms.TextInput(attrs={'class': 'form-control'}),
            'target_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    # ✅ CORRECT PLACE FOR REQUIRED FIELDS
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.required = True