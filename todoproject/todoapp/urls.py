from . import views
from django.urls import path

app_name = 'todoapp'
urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<int:id>/', views.donetask, name="donetask"),
    path('update/<int:id>/', views.edittask, name="edittask"),
]
