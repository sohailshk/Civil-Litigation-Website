from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth  import login, logout
from .middlewares import auth, guest
from .forms import EnquiryForm
from .forms import infoForm
from .models import info
# for API
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@guest 
def register_view(request): #we write request so we can get access to all the views info whenever we want
    if request.method == 'POST':  # user has submitted form POST
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)  # yeh django ka bult in login hai
            return redirect('index')
    else:
        initial_data={'username':'','password1':'','password2':""}
        form = UserCreationForm(initial=initial_data)
    return render(request,'auth/register.html',{'form':form}) #first argument mai request that we need
                                                                    # 2 mai joh page url return karna haiwoh 
                                                                    # 3 arg mai dictionary format mai return coz we
                                                                    #want to access it in templeate
def logout_view(request):
    logout(request)
    return redirect('login')

@guest
def login_view(request):
    if request.method == 'POST':  # user has submitted form POST
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user() #server pe jakar user ki details lelo
            login(request,user)  # yeh django ka bult in login hai
            return redirect('index')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html', {'form':form})

@auth
def index_view(request):
    return render(request, 'index.html')

def lawyers_view(request):
    return render(request, 'lawyers.html')


def info_view(request):
    return render(request, 'info.html')


def profile_view(request):
    return render(request, 'profile.html')    

def contact_view(request):
    return render(request, 'contact.html') 


def enquiry_view(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # Replace with your actual success URL
    else:
        form = EnquiryForm()
    return render(request, 'contact.html', {'form': form})

#page for entering info
def create_info(request):
    if request.method == 'POST':
        form = infoForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('info_list')
        else:
            print(form.errors)
    else:
        form = infoForm()
    return render(request, 'create_info.html', {'form': form})


# page for  displaying all entered infos Retrieves all Info objects from the database using the Info model's objects.all() method.
def info_list(request):
    infos = info.objects.all()
    return render(request, 'info_list.html', {'infos': infos}) 

# primary key is explicitly not defined so we used model jha save hua hai database mai uska ek id hohga 
# that id is the primary key for us and it is retrieving that primary key
# Retrieves the Info object with the specified pk from the database using the Info model's objects.get() method.
#Stores the result in the info variable.
def info_detail(request, pk):
    info = info.objects.get(pk=pk)
    return render(request, 'info_detail.html', {'info': info})


def search_info(request):
    query = request.GET.get('q')
    if query:
        results = info.objects.filter(title__icontains=query)
    else:
        results=info.objects.none()
    return render(request, 'search_results.html', {'results': results})


@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        user_input = request.POST.get('message')
        access_token = 'YIHHJ54E7VEUZIY4EDKN6KPSJA7KIFGI'
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(f'https://api.wit.ai/message?v=20230430&q={user_input}', headers=headers)
        data = response.json()
        print(data)

        # extract intent and traits
        intent = data['intents'][0]['name'] if data['intents'] else None
        traits = data.get('traits', {})

        # Generate a response based on the intent
        response_text = generate_response(intent, traits)

        return JsonResponse({"response": response_text})
    return JsonResponse({"response": "Sorry, I didn't understand that."})


def generate_response(intent, traits):
    if intent == 'greeting':
        return "Hello! How can I assist you today?"
    elif intent == 'get_legal_advice':
        return "You can get legal advice from our experienced lawyers. Please visit the 'Lawyers' section."
    # Add more intent-based responses
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"

