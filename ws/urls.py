from django.urls import path
from .views import vista, chat

urlpatterns = [
    path("text/", vista),
    path('chat/<str:pk>/', chat),

]
