from django import forms
from django.forms import ModelForm
from .models import Inventory


class AddInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = "__all__"


class UpdateInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = "__all__"