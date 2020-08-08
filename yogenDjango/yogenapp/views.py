from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    my_dict = {'test_var':'This is a test'}
    print('Index')
    return render(request,'yogenapp/index.html',context=my_dict)

def form_page_view(request):
    form = forms.FormView()
    if request.method == 'POST':
        form = forms.FormView(request.POST)
        if form.is_valid() :
            print("NAME "+form.cleaned_data['name'])
            print("EMAIL "+form.cleaned_data['email'])
            print("TEXT "+form.cleaned_data['text'])
    return render(request,'yogenapp/formview.html',{'form':form})

def signup_view(request):
    form = forms.NewUserForm()
    if request.method == 'POST':
        form = forms.NewUserForm(request.POST)
        if form.is_valid() :
            form.save(commit=True)
            return index(request)
            
    return render(request,'yogenapp/signupform.html',{'form':form})

def register_view(request):
    registered = False
    
    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)    
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()
            
    return render(request,'yogenapp/registration.html',{'registered':registered,'user_form':user_form,'user_info_profile':profile_form,})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT Active")
        else:
            print("Login failed for user {}".format(username))
            return HttpResponse("Invalid Login")
    else:
        return render(request,'yogenapp/login.html',{})

@login_required        
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))