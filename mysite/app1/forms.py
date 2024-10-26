
from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime

# Define session choices
SESSION_CHOICES = [
    ('morning', 'Morning'),
    ('afternoon', 'Afternoon'),
    ('evening', 'Evening'),
]

# Define gender choices
GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]

# Define the appointment form
class ExtendedAppointmentForm(forms.Form):
    full_name = forms.CharField(max_length=100, label='Full Name')
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(max_length=15, label='Phone Number')
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender')
    age = forms.IntegerField(min_value=0, max_value=120, label='Age')
    address = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}), 
        max_length=300, 
        label='Address'
    )
    symptoms = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        max_length=500,
        label='Describe your symptoms'
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Appointment Date'
    )
    session = forms.ChoiceField(
        choices=SESSION_CHOICES, 
        label='Preferred Session'
    )
    previous_report = forms.FileField(label='Upload Previous Report', required=False)

    def clean_date(self):
        selected_date = self.cleaned_data.get('date')
        if selected_date < datetime.today().date():
            raise ValidationError("The appointment date cannot be in the past.")
        return selected_date
