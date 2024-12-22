from django.urls import path
from .views import ChatThreadListCreateView, MessageCreateView

urlpatterns = [
    path('chat-thread/', ChatThreadListCreateView.as_view(), name='chat-thread-list-create'),
    path('messages/', MessageCreateView.as_view(), name='message-create'),  # Ensure this exists
]
