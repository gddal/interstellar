from django import forms
from django.forms import DateTimeInput, NumberInput, EmailInput
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from interstellar.models import Orders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        # fields = 'all'
        exclude = ['created_at', 'updated_at', 'total']
        widgets = {"email": forms.EmailInput(attrs={"type": "email"}),
                   "coordinatesX": forms.NumberInput(attrs={"max": "90", "min": "-90"}),
                   "coordinatesY": forms.NumberInput(attrs={"max": "180", "min": "-180"}),
                   "date_hour_product": DateTimeInput(attrs={"type": "datetime-local"})}

#    email = forms.EmailInput(name="email", label="email", max_length=50)
#    coordinatesX = forms.NumberInput(name="coordinatesX", label="coordinatesX", max_value=90, min_value=0)
#    coordinatesY = forms.NumberInput(name="coordinatesY", label="coordinatesY", max_value=180, min_value=0)
#    date_hour_product = forms.DateTimeField(name="date_hour_product", label="date_hour_product")
#    constellations = forms.BooleanField(name="constellations", label="constellations")




 #       try:
 #           validate_email(email)
 #       except ValidationError as e:
 #           print("bad email, details:", e)
 #       else:
 #           print("good email")
