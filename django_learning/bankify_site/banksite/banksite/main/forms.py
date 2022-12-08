from django import forms
from .models import Keywords, Categories

categories_=[]
for categorie in Categories.objects.all():
    categories_.append((categorie,categorie))
    
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
    selectcategoryhidden = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    categorie = forms.MultipleChoiceField(
        required=True,
        widget=forms.Select,
        choices=categories_
    )