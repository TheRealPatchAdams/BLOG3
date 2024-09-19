from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# Temporary views directly in urls.py for testing
def home(request):
    return HttpResponse("Hello, welcome to the Home Page!")

def about(request):
    return HttpResponse("About Us Page")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
]
