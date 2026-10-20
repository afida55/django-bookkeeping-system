from django.contrib import admin
from .models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'record_type',
        'category',
        'sub_category',
        'amount',
        'date'
    )

    list_filter = (
        'record_type',
        'category',
        'date'
    )

    search_fields = (
        'description',
        'category__name',
        'sub_category__name',
        'user__username'
    )

    ordering = ('-date',)

    # 🔥 THIS IS YOUR FIX
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs  # admin sees everything

        return qs.filter(user=request.user)  # normal users see only their data