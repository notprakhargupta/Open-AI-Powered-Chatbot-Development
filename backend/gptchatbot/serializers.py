from rest_framework import serializers
from .models import ChatThread, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'prompt', 'response', 'created_at']

class ChatthreadSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatThread
        fields = ['id','created_at', 'messages']
