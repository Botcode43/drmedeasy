from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class ProfileManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super(ProfileManager, self).get_queryset(*args, **kwargs).filter()

   
    def create_info(self, user, **kwargs):
        return self.model.objects.create(user=user, **kwargs)

class info(models.Model):
    user=models.OneToOneField (User, on_delete=models.CASCADE, default=None)
    
    phonenumber = models.CharField(max_length=15)
    objects = ProfileManager()
  
    # Add any other fields you need

    def __str__(self):
        return self.user.username



class doctor(models.Model):
    def generate_category():
        cat = [
            ('CARDIOLOGIST', 'cardiologist'),
            ('DERMATOLOGIST', 'dermatologist'),
            ('ENDOCRINOLOGIST', 'endocrinologist'),
            ('GASTROENTEROLOGIST', 'gastroenterologist'),
            ('HEMATOLOGIST', 'hematologist'),
            ('NEUROLOGIST', 'neurologist'),
            ('OBSTETRICIAN-GYNECOLOGIST', 'obstetrician-gynecologist'),
            ('ONCOLOGIST', 'oncologist'),
            ('OPHTHALMOLOGIST', 'ophthalmologist'),
            ('ORTHOPEDIC SURGEON', 'orthopedic surgeon'),
            ('PEDIATRICIAN', 'pediatrician'),
            ('PULMONOLOGIST', 'pulmonologist'),
            ('PSYCHIATRIST', 'psychiatrist'),
            ('RADIOLOGIST', 'radiologist'),
            ('RHEUMATOLOGIST', 'rheumatologist'),
            ('UROLOGIST', 'urologist')
        ]
        choices = []
        for value, label in cat:
            choices.append((value, label))
            
            choices.append((value.lower(), label.lower()))
            
            choices.append((value.upper(), label.upper()))
        return choices

    pf_choice = generate_category()
    

    name = models.CharField(
        max_length=100, 
        validators=[RegexValidator(regex=r'^Dr\.', message="Name should start with 'Dr.'")]
    )
    email = models.EmailField(unique=True)
    qualification = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Enter a valid phone number.")]
    )
    category = models.CharField(max_length=100, choices=pf_choice, blank=False)
    
    def __str__(self):
        return self.name

    
       
