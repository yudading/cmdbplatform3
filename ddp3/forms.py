from django import forms

from .models import Ddp3

class StudentForm(forms.ModelForm):
    def clean_qq(self):
        cleaned_data = self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字')

        return int(cleaned_data)

    class Meta:
        model = Ddp3
        fields = (
            'name', 'sex', 'profession',
            'email', 'qq', 'phone'
        )