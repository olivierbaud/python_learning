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
        
class SelectCategoryForm(forms.Form):
    selectcategoryhidden = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    keywordmemo=[('test', 'test')]
    categorie = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'}),
        choices=categories_,
        label=""
    )
    
    keywords = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'}),
        choices=keywordmemo,
        label=""
    )
    def transferkeyword(self, memo):
        keywords_operation=memo.split()
        for key in keywords_operation:
            self.keywordmemo.append((key,key))
        