from django import forms
from sacco.models import Sacco, Super_list

class SaccoForm(forms.ModelForm):
    name = forms.CharField(help_text="Please enter your name")
    phone_no = forms.CharField(help_text="Enter your phone number")
    office_location = forms.CharField(help_text="Please enter a detail description of whwre your offices are located")
    office_telephone = forms.CharField(help_text="Please enter the telephone contacts")
    office_email = forms.EmailField(help_text="Please enter your official email address")
    
    details = forms.CharField(help_text="Please enter all relevant details for your organization(Eg. Number of people, additional phone number)")

    class Meta:
        model = Sacco
        fields = ('name', 'phone_no',
                  'office_location', 'office_telephone', 'office_email', 'details')

class Super_listForm(forms.ModelForm):
    class Meta:
        model = Super_list
        fields = ('full_name', 'id_number','phone_number', 'email')


class EditProfile(forms.ModelForm):
    class Meta:
        model = Sacco
        fields = ('name', 'phone_no', 'office_location', 'office_telephone', 'office_email', 'details')


class EditSupervisor(forms.ModelForm):
    class Meta:
        model = Super_list
        fields = ('full_name', 'id_number')
