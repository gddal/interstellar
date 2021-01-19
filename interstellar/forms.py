from django import forms
from django.forms import DateTimeInput

from interstellar.models import Orders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        # fields = 'all'
        exclude = ['created_at', 'updated_at', 'total']
        widgets = {"date_hour_product": DateTimeInput(attrs={"type": "datetime-local"})}
