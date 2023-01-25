from django import forms

from .models import Subscriber


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input callback-form__input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input callback-form__input'}),
        }
