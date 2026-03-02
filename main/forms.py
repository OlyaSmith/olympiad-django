from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'university', 'course']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form__input', 'placeholder': 'Иванов Иван Иванович'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form__input', 'placeholder': 'ivan@example.com'}),
            'university': forms.TextInput(attrs={'class': 'form-control form__input', 'placeholder': 'РГЭУ (РИНХ)'}),
            'course': forms.NumberInput(attrs={'class': 'form-control form__input', 'placeholder': '3', 'min': 1, 'max': 5}),
        }