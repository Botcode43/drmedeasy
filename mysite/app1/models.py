from django.db import models
from django.contrib.auth.models import User


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
      cat=[('CARDIOLOGIST','cardiologist'),('ENT SPECIALISTS','ent specialists'),('GENERAL MEDICINE','general medicine'),('GYNAECOLOGY','gynaecology'),('OPHTHALMOLOGY','ophthalmology'),('ORTHOPAEDIC SURGEON','orthopaedic surgeon' ),('PEADIATRIC','peadiatric')]
      choices=[]
      for value,label in cat :
        choices.append((value, label))

             # Add lowercase choice
        choices.append((value.lower(), label.lower()))

           
        choices.append((value.upper(), label.upper()))
        return choices
    pf_choice=generate_category()
    category=models.CharField(max_length=100,choices=pf_choice,blank=False)
    
    def __str__(self):
        return self.category
       
