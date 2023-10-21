from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout



# Create your views here.
def login(request):

    return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        register_user_form = UserCreationForm(request.POST)
        if register_user_form.is_valid():
            register_user_form.save()
            username = register_user_form.cleaned_data['username']
            password = register_user_form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            
            login(request,user)
            messages.success(request,("Registration was successful"))
            return redirect('index')
    else:
        register_user_form = UserCreationForm()       
    
    context={
        "form":register_user_form,
    }
    return render(request,'signup.html',context)

