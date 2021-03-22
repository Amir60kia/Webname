from django.shortcuts import render
from . import models
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def articles_list(request):
    article = models.Articles.objects.all().order_by('-date')
    return render (request , 'articles/articles_list.html',{'articles':article})
def article_detial(request,slug):
    # return HttpResponse(slug)
    article = models.Articles.objects.get(slug=slug)
    return render (request , 'articles/article_detial.html',{'articles':article})
@login_required(login_url = "/accounts/login")
def create_article(request):
    if request.method == 'post':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid:
            #save article
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/create_article.html',{'form':form})
