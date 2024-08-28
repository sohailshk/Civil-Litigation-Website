# forms.py
from django import forms
from .models import Enquiry
from .models import info


class EnquiryForm(forms.ModelForm):

    class Meta:
        model = Enquiry
        fields = ['name', 'number', 'email', 'feedback']


class infoForm(forms.ModelForm):

    class Meta:
        model = info
        fields = ['title', 'description', 'image']
