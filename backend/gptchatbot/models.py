from django.db import models

class ChatThread(models.Model):
    title=models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    chat_thread=models.ForeignKey(ChatThread, related_name="messages", on_delete=models.CASCADE)
    prompt=models.TextField()
    response= models.TextField(blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message in {self.chat_thread.title}'