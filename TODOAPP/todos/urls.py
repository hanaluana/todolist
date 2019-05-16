from django.urls import path
from . import views

app_name = "todos"

urlpatterns = [
    path('',views.home, name='home'),
    path('check/<int:id>', views.check, name='check'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
]