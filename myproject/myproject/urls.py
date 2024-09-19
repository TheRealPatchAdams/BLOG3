from django.contrib import admin
from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Connect the view to the homepage
]
