from django.shortcuts import render,HttpResponse ,redirect
from django.contrib.auth.models import User 
# from app1.forms import signup
from django.contrib import messages
from .models import info ,doctor
from django.contrib.auth import authenticate, login as user_login
from django.db import models
from django.views import View
from django.core.mail import send_mail

from .forms import ExtendedAppointmentForm

# Create your views here.
def signup(request):
    if request.method=='POST':
        
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phonenumber=request.POST['phonenumber']
        
        cpassword=request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
            else:
                user=User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                profile=info.objects.create_info(user=user,phonenumber=phonenumber)
         
   
    return render(request,'Signup.html')

# class LoginView(View):
#     template_name = 'login.html'
#     form_class = CustomAuthenticationForm

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 # Redirect to a success page
#                 return redirect('userpage')
#             else:
#                 # Return an 'invalid login' error message.
#                 form.add_error(None, 'Invalid login credentials.')

#         return render(request, self.template_name, {'form': form})


def login(request):
    if request.method=='POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            user_login(request, user)
            return redirect('userpage')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'login.html')
    

def userpage(request):
     return render(request,'userpage.html')
    
# def filter_results(request):
#     all_categories = doctor.objects.values_list('category', flat=True).distinct()
    
#     if request.method == 'POST':
#         location = request.POST.get('location')
#         category = request.POST.get('category')

#         # Perform filtering based on location and category
#         filtered_doctors = doctor.objects.filter(location=location, category=category)

#         # Redirect to another page to display filtered results
#         return redirect('filtered_results_page')  # Change 'filtered_results_page' to your actual URL name

#     return render(request, 'filter_page.html', {'all_categories': all_categories})


def search_doctors(request):
    query = request.GET.get('q') 
    category = request.GET.get('category')  

    if not query and not category:
        results = doctor.objects.all()  
        return render(request, 'doctor_filter.html', {'results': results})
    redirect_args = {}
    if query:
        redirect_args['q'] = query
    if category:
        redirect_args['category'] = category
    return redirect('doctor_result')  


def doctor_result(request):
    query = request.GET.get('q') 
    category = request.GET.get('category')  
    results = doctor.objects.all()

    if query:
        results = results.filter(
            models.Q(name__icontains=query) |
            models.Q(specialty__icontains=query)
        )

    if category:
        results = results.filter(specialty__iexact=category)

    
    return render(request, 'doctor_result.html', {'results': results, 'query': query, 'category': category})


def home_page(request):
     return render(request,'home_page.html')
    




def book_appointment(request):
    if request.method == 'POST':
        form = ExtendedAppointmentForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            # Collect data from the form
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            address = form.cleaned_data['address']
            symptoms = form.cleaned_data['symptoms']
            date = form.cleaned_data['date']
            session = form.cleaned_data['session']
            report = form.cleaned_data['previous_report']

            # Prepare email content
            subject = f"New Appointment Request from {full_name}"
            message = (
                f"Name: {full_name}\n"
                f"Email: {email}\n"
                f"Phone Number: {phone_number}\n"
                f"Gender: {gender}\n"
                f"Age: {age}\n"
                f"Address: {address}\n"
                f"Symptoms: {symptoms}\n"
                f"Preferred Date: {date}\n"
                f"Preferred Session: {session}\n"
            )

            # Include report info only if a file is uploaded
            if report:
                message += f"Report: {report.name}\n"  # Just include the filename or any other info you want

            # Send the email (make sure to configure EMAIL_BACKEND settings in settings.py)
            send_mail(
                subject,
                message,
                email,  # From email
                ['ajeet1973.at@gmail.com'],  # To email (doctor)
                fail_silently=False,
            )

            return redirect('appointment_success')  # Redirect to success page
    else:
        form = ExtendedAppointmentForm()

    return render(request, 'appointment_form.html', {'form': form})

def appointment_success(request):
    return render(request, 'appointment_success.html')
