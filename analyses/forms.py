from django import forms
from .models import AnalysisRequest

class AnalysisRequestForm(forms.ModelForm):
    class Meta:
        model = AnalysisRequest
        fields = [
            # استبدل أو أضف الحقول الفعلية لمشروعك إن اختلفت
            'patient', 'test', 'price', 'discount_percent', 'discount_amount', 'total'
        ]
        widgets = {
            'discount_amount': forms.NumberInput(attrs={'readonly': 'readonly'}),
            'total': forms.NumberInput(attrs={'readonly': 'readonly'}),
        }

class NationalIDForm(forms.Form):
    national_id = forms.CharField(
        label='الرقم القومي',
        max_length=32,
        widget=forms.TextInput(attrs={'placeholder': 'الرقم القومي', 'class': 'form-control'})
    )
