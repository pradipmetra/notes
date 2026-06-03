from django.http import HttpResponse , JsonResponse
from django.shortcuts import render, redirect
from .models import member ,Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from google import genai

# Create client
client = genai.Client(api_key="AIzaSyD7VzuqoADg78uFXTH6Rq4uqXAD22VYpY0")

def ai_chat(request):

    response_text = ""

    if request.method == "POST":

        user_message = request.POST.get("message")

        # Generate response
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_message
        )

        response_text = response.text

    return render(request, "aii.html", {
        "response": response_text
    })

@csrf_exempt
def reg(request):

    if request.method == "POST":
        data = request.POST
        print(data)
        name = request.POST.get('name','')
        user= User.objects.create_user(username=name,password=request.POST.get('password',''))
        if not name:
            return HttpResponse("NAME is Require")
        return redirect ('dashboard')
    return render (request , 're.html')


@csrf_exempt 
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print('dddddd')
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
         
    return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')


def fpage(request):
    return render(request,'first_page.html')

def logout(request):
    return render(request,'first_page.html')

@csrf_exempt
def contact(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        message = request.POST.get('message','')
        user = Contact.objects.create(name=name,email=email,message=message)
        if not name:
            return HttpResponse("NAME is Require")
        return HttpResponse("message sent")
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def AI(request):
    return render(request,'AI.html')
