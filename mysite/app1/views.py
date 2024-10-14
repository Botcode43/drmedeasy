from django.shortcuts import render,HttpResponse ,redirect
from django.contrib.auth.models import User 
# from app1.forms import signup
from django.contrib import messages
from .models import info ,doctor
from django.contrib.auth import authenticate, login as user_login
from django.db import models
from django.views import View

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


# def search_doctors(request):
#     query = request.GET.get('q') 
#     category = request.GET.get('category')  

#     if not query and not category:
#         results = doctor.objects.all()  
#         return render(request, 'doctor_filter.html', {'results': results})
#     redirect_args = {}
#     if query:
#         redirect_args['q'] = query
#     if category:
#         redirect_args['category'] = category
#     return redirect('doctor_result')  


# def doctor_result(request):
#     query = request.GET.get('q') 
#     category = request.GET.get('category')  
#     results = doctor.objects.all()

#     if query:
#         results = results.filter(
#             models.Q(name__icontains=query) |
#             models.Q(specialty__icontains=query)
#         )

#     if category:
#         results = results.filter(specialty__iexact=category)

    
#     return render(request, 'doctor_result.html', {'results': results, 'query': query, 'category': category})





def search_doctors(request):
    query = request.POST.get('q')
    category = request.POST.get('category')

    # Initialize results with an empty QuerySet to avoid overwriting
    results = doctor.objects.none()

    if query:
        results |= doctor.objects.filter(
            models.Q(name__icontains=query) |
            models.Q(specialty__icontains=query)
        )

    if category:
        results |= doctor.objects.filter(specialty__iexact=category)

    # Check if results are empty and provide a suitable message
    if not results:
        messages.info(request, "No doctors found matching your criteria.")
        return redirect('doctor_search')  # Redirect back to search page

    return render(request, 'doctor_result.html', {'results': results, 'query': query, 'category': category})


def doctor_result(request):
    # Handle empty query and category gracefully
    if not request.GET.get('q') and not request.GET.get('category'):
        messages.info(request, "Please enter a search term or select a category.")
        return redirect('doctor_search')

    # Rest of the view logic remains the same
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