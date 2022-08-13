from django import forms
from DentalApp.models import Appointment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AppointmentForm(forms.ModelForm):
    
    def clean(self):
        # Get the user submitted names from the cleaned_data dictionary
        cleaned_data = super().clean()
        return cleaned_data
    
    class Meta:
        model = Appointment
        fields ='__all__'
        
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]
        
        