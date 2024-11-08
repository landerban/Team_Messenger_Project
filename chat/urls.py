from django.urls import path

from . import views
app_name="chat"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
    path("api/get_chats", views.get_chats, name="get_chat"),
    path("api/create_chat", views.create_chat, name="create_chat"),
]
