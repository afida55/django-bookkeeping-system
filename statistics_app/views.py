from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from records.models import Record
from category.models import MainCategory
from category.models import SubCategory
from django.db.models import Sum, Count


@login_required
def dashboard(request):

    records = Record.objects.filter(
        user=request.user
    ).order_by('-date')

    income = records.filter(
        record_type='Income'
    ).aggregate(
        Sum('amount')
    )['amount__sum'] or 0

    expense = records.filter(
        record_type='Expense'
    ).aggregate(
        Sum('amount')
    )['amount__sum'] or 0

    balance = income - expense

    total_records = records.count()

    income_records = records.filter(
        record_type='Income'
    ).count()

    expense_records = records.filter(
        record_type='Expense'
    ).count()

    categories = MainCategory.objects.filter(
        user=request.user
    ).count()

    most_used = records.values(
        'category__name'
    ).annotate(
        total=Count('id')
    ).order_by('-total').first()

    most_used_category = (
        most_used['category__name']
        if most_used else "No Data"
    )

    largest = records.filter(
        record_type='Expense'
    ).order_by('-amount').first()

    largest_expense = (
        largest.category.name
        if largest else "No Data"
    )

    context = {

        'income': income,
        'expense': expense,
        'balance': balance,

        'total_records': total_records,
        'income_records': income_records,
        'expense_records': expense_records,
        'categories': categories,

        'most_used_category': most_used_category,
        'largest_expense': largest_expense,

        'recent_transactions': records[:10],

        # FOR CHARTS
        'chart_income': float(income),
        'chart_expense': float(expense),
    }

    @login_required
    def load_categories(request):

        record_type = request.GET.get('record_type')

        categories = MainCategory.objects.filter(
            user=request.user,
            category_type=record_type
        )

        data = []

        for category in categories:
            data.append({
                'id': category.id,
                'name': category.name
            })

        return JsonResponse(
            data,
            safe=False
        )

    @login_required
    def load_subcategories(request):

        category_id = request.GET.get('category')

        subcategories = SubCategory.objects.filter(
            main_category_id=category_id
        )

        data = []

        for sub in subcategories:
            data.append({
                'id': sub.id,
                'name': sub.name
            })

        return JsonResponse(
            data,
            safe=False
        )

    return render(
        request,
        'statistics/dashboard.html',
        context
    )