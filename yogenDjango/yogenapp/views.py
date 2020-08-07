from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    my_dict = {'test_var':'This is a test'}
    return render(request,'yogenapp/index.html',context=my_dict)
