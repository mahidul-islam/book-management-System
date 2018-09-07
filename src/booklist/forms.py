from django import forms
from .models import BookTransactionModel

class BookTransactionModelForm(forms.ModelForm):
    class Meta:
        model = BookTransactionModel
        fields = ['phone_number','address','message']

    def __init__(self, *args, **kwargs):
        super(BookTransactionModelForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter mobile number'
    })
        self.fields['address'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your address'
    })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your massage for us here. We will get back to you within 2 days. (Optional) '
    })
        """
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })
        """
