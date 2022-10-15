from django.shortcuts import render
from django.http import HttpResponse
from registration.models import Course,Batch, Student

# Create your views here.

def index(request):
    return HttpResponse("<h1>  wlecome to prime intuit registration page </h1>")
def Home(request):
    #return HttpResponse("<h1>  wlecome to prime intuit Home page </h1>")
   # my_dict = { "insert_me": "i am a text  from registration/views.py now from templates"}
    batch_list = Batch.objects.order_by('batch_ID')
    data_dict={ 'access_record': batch_list,"insert_me": "i am a text  from registration/views.py now from templates"}
    return render(request,'registration/index.html',context=data_dict)




