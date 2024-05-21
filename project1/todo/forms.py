from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    # Define choices for the status field
    TIER_CHOICES = [
        ('To Do', 'To Do'),
        ('Doing', 'Doing'),
        ('Done', 'Done'),
    ]

    # Add status field with dropdown choices
    status = forms.ChoiceField(choices=TIER_CHOICES, label='Tier')

    class Meta:
        model = Tarea
        fields = ['tarea', 'status']
