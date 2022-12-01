from django import forms
from .models import Keywords, Categories

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
        
