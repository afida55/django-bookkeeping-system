from django import forms
from .models import MainCategory, SubCategory


class MainCategoryForm(forms.ModelForm):
    class Meta:
        model = MainCategory
        fields = ['name', 'category_type']


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name', 'main_category']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            if user.is_superuser:
                self.fields['main_category'].queryset = MainCategory.objects.all()
            else:
                self.fields['main_category'].queryset = MainCategory.objects.filter(user=user)