from django import forms

from .models import Operator

# class OpeatorForm(forms.Form):
#     name = forms.CharField(label='Operator name', max_length=100)
#     mobile = forms.IntegerField(label='Operator Mobile')
#     email = forms.EmailField(label='Operator Email',)
#     city = forms.CharField(label='City',)


class OpeatorForm(forms.ModelForm):
    class Meta:
        model = Operator

        fields = '__all__'

        exclude = ['soft_delete','is_active']
