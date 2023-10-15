from django.shortcuts import render


def index(request):
    
    return render(request,'home.html')



def register(request):

    return render(request,'signup.html')



def login(request):

    return render(request, 'login.html')



def orders(request):

    return render(request,'orders.html')



def checkout(request):
    return render(request,'checkout.html')

