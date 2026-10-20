from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import MainCategory
from .models import SubCategory

from .forms import MainCategoryForm
from .forms import SubCategoryForm

from django.http import JsonResponse


@login_required
def category_list(request):

    # =========================
    # AUTO CREATE DEFAULT DATA
    # =========================

    if not MainCategory.objects.filter(user=request.user).exists():

        # ---------- EXPENSE ----------

        food = MainCategory.objects.create(
            name='Food',
            category_type='Expense',
            user=request.user
        )

        SubCategory.objects.create(name='Breakfast', main_category=food)
        SubCategory.objects.create(name='Lunch', main_category=food)
        SubCategory.objects.create(name='Dinner', main_category=food)
        SubCategory.objects.create(name='Tea', main_category=food)
        SubCategory.objects.create(name='Coffee', main_category=food)

        transport = MainCategory.objects.create(
            name='Transport',
            category_type='Expense',
            user=request.user
        )

        SubCategory.objects.create(name='Bus', main_category=transport)
        SubCategory.objects.create(name='Taxi', main_category=transport)
        SubCategory.objects.create(name='Fuel', main_category=transport)

        shopping = MainCategory.objects.create(
            name='Shopping',
            category_type='Expense',
            user=request.user
        )

        SubCategory.objects.create(name='Clothes', main_category=shopping)
        SubCategory.objects.create(name='Shoes', main_category=shopping)
        SubCategory.objects.create(name='Accessories', main_category=shopping)

        accommodation = MainCategory.objects.create(
            name='Accommodation',
            category_type='Expense',
            user=request.user
        )

        SubCategory.objects.create(name='Rent', main_category=accommodation)
        SubCategory.objects.create(name='Electricity', main_category=accommodation)
        SubCategory.objects.create(name='Internet', main_category=accommodation)

        medical = MainCategory.objects.create(
            name='Medical',
            category_type='Expense',
            user=request.user
        )

        SubCategory.objects.create(name='Medicine', main_category=medical)
        SubCategory.objects.create(name='Hospital', main_category=medical)
        SubCategory.objects.create(name='Checkup', main_category=medical)

        education = MainCategory.objects.create(
            name='Education',
            category_type='Expense',
            user=request.user
        )

        SubCategory.objects.create(name='Books', main_category=education)
        SubCategory.objects.create(name='Course Fee', main_category=education)
        SubCategory.objects.create(name='Stationery', main_category=education)

        # ---------- INCOME ----------

        salary = MainCategory.objects.create(
            name='Salary',
            category_type='Income',
            user=request.user
        )

        SubCategory.objects.create(name='Monthly Salary', main_category=salary)
        SubCategory.objects.create(name='Overtime', main_category=salary)

        bonus = MainCategory.objects.create(
            name='Bonus',
            category_type='Income',
            user=request.user
        )

        SubCategory.objects.create(name='Performance Bonus', main_category=bonus)
        SubCategory.objects.create(name='Festival Bonus', main_category=bonus)

        freelance = MainCategory.objects.create(
            name='Freelance',
            category_type='Income',
            user=request.user
        )

        SubCategory.objects.create(name='Web Development', main_category=freelance)
        SubCategory.objects.create(name='Mobile App', main_category=freelance)

        business = MainCategory.objects.create(
            name='Business',
            category_type='Income',
            user=request.user
        )

        SubCategory.objects.create(name='Product Sale', main_category=business)
        SubCategory.objects.create(name='Service Income', main_category=business)

        gift = MainCategory.objects.create(
            name='Gift',
            category_type='Income',
            user=request.user
        )

        SubCategory.objects.create(name='Family Gift', main_category=gift)
        SubCategory.objects.create(name='Friend Gift', main_category=gift)

    # =========================
    # LOAD DATA
    # =========================

    if request.user.is_superuser:
        main_categories = MainCategory.objects.all()
    else:
        main_categories = MainCategory.objects.filter(user=request.user)

    return render(
        request,
        'category/category_list.html',
        {
            'main_categories': main_categories,
        }
    )


@login_required
def add_main_category(request):

    if request.method == 'POST':

        form = MainCategoryForm(request.POST)

        if form.is_valid():

            category = form.save(commit=False)
            category.user = request.user
            category.save()

            return redirect('category_list')

    else:
        form = MainCategoryForm()

    return render(
        request,
        'category/add_main_category.html',
        {
            'form': form
        }
    )


@login_required
def edit_main_category(request, pk):

    if request.user.is_superuser:
        category = get_object_or_404(
            MainCategory,
            pk=pk
        )
    else:
        category = get_object_or_404(
            MainCategory,
            pk=pk,
            user=request.user
        )

    if request.method == 'POST':

        form = MainCategoryForm(
            request.POST,
            instance=category
        )

        if form.is_valid():

            form.save()

            return redirect('category_list')

    else:

        form = MainCategoryForm(
            instance=category
        )

    return render(
        request,
        'category/edit_main_category.html',
        {
            'form': form
        }
    )


@login_required
def delete_main_category(request, pk):

    if request.user.is_superuser:
        category = get_object_or_404(
            MainCategory,
            pk=pk
        )
    else:
        category = get_object_or_404(
            MainCategory,
            pk=pk,
            user=request.user
        )

    category.delete()

    return redirect('category_list')


@login_required
def add_sub_category(request):

    if request.method == 'POST':

        form = SubCategoryForm(
            request.POST,
            user=request.user
        )

        if form.is_valid():

            form.save()

            return redirect('category_list')

    else:

        form = SubCategoryForm(
            user=request.user
        )

    return render(
        request,
        'category/add_sub_category.html',
        {
            'form': form
        }
    )


@login_required
def delete_sub_category(request, pk):

    if request.user.is_superuser:
        sub = get_object_or_404(
            SubCategory,
            pk=pk
        )
    else:
        sub = get_object_or_404(
            SubCategory,
            pk=pk,
            main_category__user=request.user
        )

    sub.delete()

    return redirect('category_list')


@login_required
def filter_categories(request):

    category_type = request.GET.get('type')

    if request.user.is_superuser:
        categories = MainCategory.objects.filter(
            category_type=category_type
        )
    else:
        categories = MainCategory.objects.filter(
            user=request.user,
            category_type=category_type
        )

    data = []

    for cat in categories:
        data.append({
            'id': cat.id,
            'name': cat.name,
        })

    return JsonResponse(data, safe=False)