from django.shortcuts import render
from . import models
from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required

def free_list(request):
    free = models.Free.objects.all().order_by('-date')
    return render (request , 'free/free_list.html',{'free_1':free})
def free_detial(request,slug):
    # return HttpResponse(slug)
    free = models.Free.objects.get(slug=slug)
    return render (request,'free/free_detial.html',{"free":free})
@login_required(login_url = "/accounts/login")
def create_free(request):
    return render(request, 'free/create_free.html')
