from django import forms

class MyForm(forms.Form):
    start_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    end_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    called_number=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter the number'}))
    only_called_number=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter the number'}))