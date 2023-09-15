from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path(r'chats/<str:id>/', consumers.PrivateChatConsumer.as_asgi()),
    path(r'notify/', consumers.ChatNotificationConsumer.as_asgi()),
]
