from django import forms

from .models import Record
from category.models import MainCategory
from category.models import SubCategory


class RecordForm(forms.ModelForm):

    class Meta:
        model = Record

        fields = [
            'record_type',
            'category',
            'sub_category',
            'amount',
            'description',
            'date'
        ]

        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date'}
            )
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['category'].queryset = MainCategory.objects.none()

        self.fields['sub_category'].queryset = SubCategory.objects.none()

        if 'record_type' in self.data:

            record_type = self.data.get('record_type')

            self.fields['category'].queryset = (
                MainCategory.objects.filter(
                    category_type=record_type
                )
            )

        if 'category' in self.data:

            try:

                category_id = int(
                    self.data.get('category')
                )

                self.fields['sub_category'].queryset = (
                    SubCategory.objects.filter(
                        main_category_id=category_id
                    )
                )

            except:

                pass

        elif self.instance.pk:

            self.fields['category'].queryset = (
                MainCategory.objects.filter(
                    category_type=self.instance.record_type
                )
            )

            self.fields['sub_category'].queryset = (
                SubCategory.objects.filter(
                    main_category=self.instance.category
                )
            )

            def __init__(self, *args, **kwargs):

                super().__init__(*args, **kwargs)

                for field in self.fields.values():
                    field.widget.attrs.update({
                        'class': 'form-control'
                    })

    widgets = {
        'date': forms.DateInput(attrs={'type': 'date'}),
        'description': forms.Textarea(attrs={'rows': 3}),
    }