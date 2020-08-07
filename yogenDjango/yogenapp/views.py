from django.shortcuts import render
from django.http import HttpResponse
from . import forms
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
