from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from django import forms
from .models import Tab_bords



    

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Tab_bords
        fields = '__all__' 