from django import forms

from .models import SuperCategory, SubCategory


class SubCategoryForm(forms.ModelForm):
    super_category = forms.ModelChoiceField(
        queryset=SuperCategory.objects.all(), empty_label=None,
        label='Надкатегория', required=True,
    )

    class Meta:
        model = SubCategory
        fields = '__all__'
