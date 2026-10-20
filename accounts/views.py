from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import RegisterForm
from category.models import MainCategory
from user_profile.models import Profile   # IMPORTANT (auto profile)
from category.models import MainCategory, SubCategory

# ---------------- REGISTER ----------------
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(form.cleaned_data['password1'])
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')

            user.save()

            # DEFAULT CATEGORIES

            food = MainCategory.objects.create(
                name='Food',
                category_type='Expense',
                user=user
            )
            SubCategory.objects.create(name='Breakfast', main_category=food)
            SubCategory.objects.create(name='Lunch', main_category=food)
            SubCategory.objects.create(name='Dinner', main_category=food)
            SubCategory.objects.create(name='Tea', main_category=food)
            SubCategory.objects.create(name='Coffee', main_category=food)

            transport = MainCategory.objects.create(
                name='Transport',
                category_type='Expense',
                user=user
            )
            SubCategory.objects.create(name='Bus', main_category=transport)
            SubCategory.objects.create(name='Taxi', main_category=transport)
            SubCategory.objects.create(name='Fuel', main_category=transport)

            shopping = MainCategory.objects.create(
                name='Shopping',
                category_type='Expense',
                user=user
            )
            SubCategory.objects.create(name='Clothes', main_category=shopping)
            SubCategory.objects.create(name='Shoes', main_category=shopping)
            SubCategory.objects.create(name='Accessories', main_category=shopping)

            accommodation = MainCategory.objects.create(
                name='Accommodation',
                category_type='Expense',
                user=user
            )
            SubCategory.objects.create(name='Rent', main_category=accommodation)
            SubCategory.objects.create(name='Electricity', main_category=accommodation)
            SubCategory.objects.create(name='Internet', main_category=accommodation)

            medical = MainCategory.objects.create(
                name='Medical',
                category_type='Expense',
                user=user
            )
            SubCategory.objects.create(name='Medicine', main_category=medical)
            SubCategory.objects.create(name='Hospital', main_category=medical)
            SubCategory.objects.create(name='Checkup', main_category=medical)

            education = MainCategory.objects.create(
                name='Education',
                category_type='Expense',
                user=user
            )
            SubCategory.objects.create(name='Books', main_category=education)
            SubCategory.objects.create(name='Course Fee', main_category=education)
            SubCategory.objects.create(name='Stationery', main_category=education)

            salary = MainCategory.objects.create(
                name='Salary',
                category_type='Income',
                user=user
            )
            SubCategory.objects.create(name='Monthly Salary', main_category=salary)
            SubCategory.objects.create(name='Overtime', main_category=salary)

            bonus = MainCategory.objects.create(
                name='Bonus',
                category_type='Income',
                user=user
            )
            SubCategory.objects.create(name='Performance Bonus', main_category=bonus)
            SubCategory.objects.create(name='Festival Bonus', main_category=bonus)

            freelance = MainCategory.objects.create(
                name='Freelance',
                category_type='Income',
                user=user
            )
            SubCategory.objects.create(name='Web Development', main_category=freelance)
            SubCategory.objects.create(name='Mobile App', main_category=freelance)

            business = MainCategory.objects.create(
                name='Business',
                category_type='Income',
                user=user
            )
            SubCategory.objects.create(name='Product Sale', main_category=business)
            SubCategory.objects.create(name='Service Income', main_category=business)

            gift = MainCategory.objects.create(
                name='Gift',
                category_type='Income',
                user=user
            )
            SubCategory.objects.create(name='Family Gift', main_category=gift)
            SubCategory.objects.create(name='Friend Gift', main_category=gift)

            return redirect('login')

        else:
            print(form.errors)

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


# ---------------- LOGIN ----------------
def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('record_list')

    return render(request, 'accounts/login.html')


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect('login')