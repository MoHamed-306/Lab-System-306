from django import forms

class NationalIDForm(forms.Form):
    national_id = forms.CharField(
        label='الرقم القومي',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ادخل الرقم القومي'})
    )
