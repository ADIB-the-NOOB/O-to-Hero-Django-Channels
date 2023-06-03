"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()


from channels.routing import ProtocolTypeRouter, URLRouter
from base.consumers import TestConsumer
from django.urls import path

ws_pattern = [
    path("ws/test", TestConsumer.as_asgi())    
]

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    "websocket": URLRouter(ws_pattern)
})