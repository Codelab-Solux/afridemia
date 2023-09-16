"""
ASGI config for afridemia project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
# from chats import routing
import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.urls import path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'afridemia.settings')
import django
django.setup()
from chats.consumers import PrivateChatConsumer,ChatNotificationConsumer
#
django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            # URLRouter(routing.websocket_urlpatterns)
            URLRouter(
                [
                    path('chats/<str:id>/', PrivateChatConsumer.as_asgi()),
                    path('notify/', ChatNotificationConsumer.as_asgi()),
                ]
            )
    ))
})

app = get_asgi_application()
