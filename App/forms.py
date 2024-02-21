from django import forms
from .models import Feedback

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, label='Quantity')

    def __init__(self, *args, **kwargs):
        spare_id = kwargs.pop('spare_id')
        super(AddToCartForm, self).__init__(*args, **kwargs)
        self.fields['spare_id'] = forms.IntegerField(widget=forms.HiddenInput(), initial=spare_id)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
        