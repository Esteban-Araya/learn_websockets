from django.urls import path
from .consumers import randomNum,ChatConsumer

ws_urlpatterns = [
    path("ws/chat/<str:pk>/",ChatConsumer.as_asgi()),
    path("ws/num/", randomNum.as_asgi()),
]