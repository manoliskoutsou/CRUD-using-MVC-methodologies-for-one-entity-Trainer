from django.forms import ModelForm
from .models import Trainer

class TrainerForm(ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'