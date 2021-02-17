from django import forms
from owner.models import Owner, Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('name', 'phone_number')


class EditProfile(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ( 'nat_id', 'telephone')


   
