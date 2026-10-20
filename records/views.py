from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from category.models import MainCategory, SubCategory

from .models import Record
from .forms import RecordForm


@login_required
def record_list(request):

    # Admin can see all records
    if request.user.is_superuser:
        records = Record.objects.all()
    else:
        records = Record.objects.filter(user=request.user)

    # -----------------------------
    # Filter by User (Admin only)
    # -----------------------------
    selected_user = request.GET.get("user")

    if request.user.is_superuser and selected_user:
        records = records.filter(user_id=selected_user)

    # -----------------------------
    # Filter by Date
    # -----------------------------
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    if start_date:
        records = records.filter(date__gte=start_date)

    if end_date:
        records = records.filter(date__lte=end_date)

    records = records.order_by("-date")

    record_count = records.count()

    return render(
        request,
        "records/record_list.html",
        {
            "records": records,
            "record_count": record_count,
            "users": User.objects.all(),
            "selected_user": selected_user,
            "start_date": start_date,
            "end_date": end_date,
        },
    )


@login_required
def add_record(request):

    if request.method == "POST":

        form = RecordForm(request.POST)

        if form.is_valid():

            record = form.save(commit=False)

            # Always save the logged-in user
            record.user = request.user

            record.save()

            return redirect("record_list")

    else:

        form = RecordForm()

    return render(
        request,
        "records/add_record.html",
        {
            "form": form
        }
    )


@login_required
def edit_record(request, pk):

    # Admin can edit every record
    if request.user.is_superuser:
        record = get_object_or_404(
            Record,
            pk=pk
        )
    else:
        record = get_object_or_404(
            Record,
            pk=pk,
            user=request.user
        )

    if request.method == "POST":

        form = RecordForm(
            request.POST,
            instance=record
        )

        if form.is_valid():

            form.save()

            return redirect("record_list")

    else:

        form = RecordForm(
            instance=record
        )

    return render(
        request,
        "records/edit_record.html",
        {
            "form": form
        }
    )


@login_required
def delete_record(request, pk):

    # Admin can delete every record
    if request.user.is_superuser:
        record = get_object_or_404(
            Record,
            pk=pk
        )
    else:
        record = get_object_or_404(
            Record,
            pk=pk,
            user=request.user
        )

    record.delete()

    return redirect("record_list")


@login_required
def load_categories(request):

    record_type = request.GET.get("record_type")

    # Admin can access all categories
    if request.user.is_superuser:
        categories = MainCategory.objects.filter(
            category_type=record_type
        )
    else:
        categories = MainCategory.objects.filter(
            user=request.user,
            category_type=record_type
        )

    data = []

    for category in categories:

        data.append({
            "id": category.id,
            "name": category.name
        })

    return JsonResponse(data, safe=False)


@login_required
def load_subcategories(request):

    category_id = request.GET.get("category")

    subcategories = SubCategory.objects.filter(
        main_category_id=category_id
    )

    data = []

    for sub in subcategories:

        data.append({
            "id": sub.id,
            "name": sub.name
        })

    return JsonResponse(data, safe=False)