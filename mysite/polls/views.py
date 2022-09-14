import json

from django.http import HttpResponse
from django.shortcuts import render
from polls.models import User
from polls.models import Inscription
from django.contrib import messages


def index(request):
    return HttpResponse("Hello, world. You're at the polls index. im amine")


def afficher(request):
    return HttpResponse("im methode afficher amine")





def CoursPageA1(request):
    return render(request, 'coursPageA1.html')
def CoursPageA2(request):
    return render(request, 'coursPageA2.html')
def CoursPageB1(request):
    return render(request, 'coursPageB1.html')
def CoursPageB2(request):
    return render(request, 'coursPageB2.html')

def GrammatikA1(request):
    return render(request, 'GraA1.html')

def GrammatikA2(request):
    return render(request, 'GraA2.html')

def GrammatikB1(request):
    return render(request, 'GraB1.html')

def GrammatikB2(request):
    return render(request, 'GraB2.html')

def Acceuil(request):
    return render(request, 'home1.html')


def ChoiceA1(request):
    return render(request, 'choiceA1.html')
def ChoiceA2(request):
    return render(request, 'choiceA2.html')
def ChoiceB1(request):
    return render(request, 'choiceB1.html')
def ChoiceB2(request):
    return render(request, 'choiceB2.html')

def HorenA1(request):
    return render(request, 'horenA1.html')
def LesenA1(request):
    return render(request, 'LesenA1.html')
def LesenB2(request):
    return render(request, 'LesenB2.html')

def Signup(request):
    return render(request, 'signup.html')


def Login(request):
    return render(request, 'login.html')


def ModulA1(request):
    return render(request, 'modulA1.html')

def ModulA2(request):
    return render(request, 'modulA2.html')

def ModulB1(request):
    return render(request, 'modulB1.html')

def ModulB2(request):
    return render(request, 'modulB2.html')



def NummerA1(request):
    return render(request, 'NummerA1.html')

def NummerA1(request):
    return render(request, 'NummerA1.html')

def AlphabetA1(request):
    return render(request, 'AlphabetA1.html')

def PronomA1(request):
    return render(request, 'PronomA1.html')
def AdverbA2(request):
    return render(request, 'AdverbA2.html')
def VerbA2(request):
    return render(request, 'VerbA2.html')
def AdjektivA2(request):
    return render(request, 'AdjektivA2.html')
def PrepositionB1(request):
    return render(request, 'PrepositionB1.html')
def SyntaxeB1(request):
    return render(request, 'SyntaxeB1.html')
def VerbB1(request):
    return render(request, 'VerbA2.html')
def SubB2(request):
    return render(request, 'SubB2.html')
def VerneinungB2(request):
    return render(request, 'VerneinungB2.html')















def SchreibenA1(request):
    return render(request, 'SchreibenA1.html')
def SchreibenA2(request):
    return render(request, 'SchreibenA2.html')
def SchreibenB1(request):
    return render(request, 'SchreibenB1.html')
def SchreibenB2(request):
    return render(request, 'SchreibenB2.html')











def SaveUser(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       firstname = request.POST.get('firstname')
       lastname = request.POST.get('lastname')
       password = request.POST.get('password')
       email = request.POST.get('email')


       user = User(username, password, email, firstname, lastname)
       user.save()
       return render(request, 'home1.html')
    return HttpResponse("L'insertion a eté effectuée")


def GetAllUsers(request):
    if request.method == 'POST':
        try:
            User.objects.get(username=request.POST.get('fname')).delete()
        except:
            users = User.objects.all()

            return render(request, 'Admin.html', {'data': users})

    users = User.objects.all()

    return render(request, 'Admin.html', {'data': users})

def deletuser(request):
    if request.method == 'POST':
        User.objects.get(username='sqersgr').delete()
        users = User.objects.all()
        return render(request, 'Admin.html', {'data': users})


def Connexion(request):

    if request.method == 'POST':
       response_data = {}

       username = request.POST.get('username')
       password = request.POST.get('password')

       #user = User(username=username, password=password)
       #result=User.objects.all()
       result = User.objects.filter(username=username , password=password)

       if result.exists():


           response_data['result'] = 'ok'
           response_data['message'] = username

           return HttpResponse(json.dumps(response_data), content_type="application/json")

           return render(request, 'home1.html')
       else:
           response_data['result'] = password
           response_data['message'] = "You should connected"

           return HttpResponse(json.dumps(response_data), content_type="application/json")

           return render(request, 'home1.html')






    # Do that...
   # return render(request, 'choices.html')




def Admin(request):
    return render(request, 'Admin.html')



def SaveMessage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        message1 = Message(1, name, email, phone, message)
        message1.save()
        return render(request, 'home1.html')
        return HttpResponse("L'insertion a eté effectuée")
