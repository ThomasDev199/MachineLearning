from django import forms

class PrediccionForm(forms.Form):
    surface = forms.FloatField(
        label="Metros cuadrados (m²)",
        min_value=1,
        widget=forms.NumberInput(attrs={
            "class": "form-control form-control-lg",
            "placeholder": "Ej: 100",
            "step": "any",
        }),
    )