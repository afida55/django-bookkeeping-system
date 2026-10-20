from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from records.models import Record
from .models import Profile, BankCard, SavingsGoal
from .forms import ProfileForm, UserForm, BankCardForm, SavingsGoalForm


@login_required
def profile_detail(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    income = Record.objects.filter(user=request.user, record_type='Income')
    expense = Record.objects.filter(user=request.user, record_type='Expense')

    total_income = sum(i.amount for i in income)
    total_expense = sum(e.amount for e in expense)

    balance = total_income - total_expense

    recent_transactions = Record.objects.filter(
        user=request.user
    ).order_by('-id')[:5]

    bank_card = BankCard.objects.filter(
        user=request.user,
        is_default=True
    ).first()

    if not bank_card:
        bank_card = BankCard.objects.filter(user=request.user).first()

    savings_goal = SavingsGoal.objects.filter(
        user=request.user
    ).first()

    progress = 0
    if savings_goal and savings_goal.target_amount > 0:
        progress = min(100, (balance / savings_goal.target_amount) * 100)

    return render(request, 'profile/profile_detail.html', {
        'profile': profile,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'recent_transactions': recent_transactions,
        'bank_card': bank_card,
        'savings_goal': savings_goal,
        'progress': progress,
    })


@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    bank_card, created = BankCard.objects.get_or_create(
        user=request.user,
        defaults={
            'bank_name': '',
            'card_holder': '',
            'card_number': '',
            'expiry_date': '',
        }
    )

    savings_goal, created = SavingsGoal.objects.get_or_create(
        user=request.user,
        defaults={
            'goal_name': '',
            'target_amount': 0,
        }
    )

    form_error = False

    if request.method == "POST":

        u_form = UserForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES, instance=profile)
        card_form = BankCardForm(request.POST, instance=bank_card)
        goal_form = SavingsGoalForm(request.POST, instance=savings_goal)

        if (
            u_form.is_valid() and
            p_form.is_valid() and
            card_form.is_valid() and
            goal_form.is_valid()
        ):
            u_form.save()
            p_form.save()

            card = card_form.save(commit=False)
            card.user = request.user
            card.save()

            goal = goal_form.save(commit=False)
            goal.user = request.user
            goal.save()

            return redirect("profile_detail")

        else:
            form_error = False

            # DEBUG (optional, remove later)
            print("User Errors:", u_form.errors)
            print("Profile Errors:", p_form.errors)
            print("Card Errors:", card_form.errors)
            print("Goal Errors:", goal_form.errors)

    else:
        u_form = UserForm(instance=request.user)
        p_form = ProfileForm(instance=profile)
        card_form = BankCardForm(instance=bank_card)
        goal_form = SavingsGoalForm(instance=savings_goal)

    return render(request, "profile/profile_edit.html", {
        "profile": profile,
        "u_form": u_form,
        "p_form": p_form,
        "card_form": card_form,
        "goal_form": goal_form,
        "form_error": form_error,
    })