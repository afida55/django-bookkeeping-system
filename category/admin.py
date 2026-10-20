from django.contrib import admin
from .models import MainCategory, SubCategory


class MainCategoryAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # admin sees everything
        if request.user.is_superuser:
            return qs

        # students see only their own data
        return qs.filter(user=request.user)

class SubCategoryAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser or request.user.is_staff:
            return qs

        return qs.filter(user=request.user)


admin.site.register(MainCategory, MainCategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)