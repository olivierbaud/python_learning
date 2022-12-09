from django import forms
from .models import Categories
    
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
    def __init__(self, keywordmemo, *args, **kwargs):
        #self.keywordmemo=kwargs.pop('keywordmemo')
        super().__init__(*args, **kwargs)
        self.fields['category'] = forms.ChoiceField(
            required=True,
            widget=forms.Select(attrs={'class': 'form-select'}),
            choices=tuple([(cat,cat) for cat in Categories.objects.all()]),
            label="Choose a Category"
        )
        self.fields['keywords'] = forms.ChoiceField(
            required=True, 
            widget=forms.Select(attrs={'class': 'form-select'}), 
            choices=tuple([(word,word) for word in keywordmemo ]),
            label="Choose a relevant Keyword"
            )
    category = forms.ChoiceField()
    keywords = forms.ChoiceField()     
    selectcategoryhidden = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    
        