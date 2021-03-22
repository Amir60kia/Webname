
from django.contrib import admin
from django.urls import path , include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('', views.home),
    path('articles/',include('articles.urls')),
    path('free/',include('free.urls')),
    path('accounts/',include ('accounts.urls')),
    path('rezome/',views.rezome),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
