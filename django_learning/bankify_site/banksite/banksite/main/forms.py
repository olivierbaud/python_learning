from django import forms
from .models import Keywords, Categories

categories = Categories.objects.all()
categories_=[('test2','test3')]


class CsvUploadForm(forms.Form):
    file = forms.FileField()
        
class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name']
        widgets = {
            'name': forms.TextInput
        }
        
class AddCategoryOperationForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name']
        
class SelectCategory(forms.Form):
    categorie = forms.MultipleChoiceField(
        required=True,
        widget=forms.Select,
        choices=categories_
    )