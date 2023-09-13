from django import forms
from .models import ContactModel
from django.core.validators import RegexValidator


class ContactForm(forms.ModelForm):
    phoneRegex = RegexValidator(
        regex=r'\+\d{1,3}-\d{1,15}',
        message='Phone not valid'
    )

    class Meta:
        model = ContactModel
        fields = '__all__'
        widgets = {
            'call': forms.TextInput(attrs={'placeholder': '+62-1234567890',
                                           'class': 'form-group'}),
            'message': forms.Textarea(attrs={'class': 'form-group',
                                             'placeholder': 'Write your message here'})
        }
