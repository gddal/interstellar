from django import forms
from interstellar.models import Orders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        # fields = 'all'
        exclude = ['created_at', 'updated_at', 'total']