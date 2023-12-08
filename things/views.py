from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def renderHomePage(request):
    #response = HttpResponse('hope')
    #return response
    return render(request,'home.html')