from django.urls import path, re_path

from . import consumers

websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]
# websocket_urlpatterns = [
#    re_path(r'^ws/(?P<room_name>[^/]+)/$', consumers.ChatConsumer.as_asgi()),
# ]