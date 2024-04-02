from django.shortcuts import render,HttpResponse ,redirect
from django.contrib.auth.models import User 
# from app1.forms import signup
from django.contrib import messages
from .models import info
from django.contrib.auth import authenticate, login as user_login


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
    


