import openai
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import ChatthreadSerializer, MessageSerializer
from .models import ChatThread, Message

class ChatThreadListCreateView(generics.ListCreateAPIView):
    queryset = ChatThread.objects.all()
    serializer_class = ChatthreadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        thread = serializer.save()
        return Response(self.get_serializer(thread).data, status=status.HTTP_201_CREATED)

class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        # Extract data from the request
        thread_id = request.data.get('thread_id')
        user_message = request.data.get('prompt')

        # Find or create the associated chat thread
        thread = ChatThread.objects.filter(id=thread_id).first() if thread_id else ChatThread.objects.create(title="Default Title")

        try:
            # Call OpenAI's ChatCompletion API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": user_message},  # Current user input
                ],
                temperature=0.5
            )

            # Extract the assistant's response from the API response
            try:
                assistant_response_text = response['choices'][0]['message']['content']
            except (KeyError, IndexError):
                return Response({"error": "Unexpected response from OpenAI API"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            # Save the assistant's response to the database
            assistant_message_obj = Message.objects.create(
                chat_thread=thread,
                prompt=user_message,
                response=assistant_response_text
            )

            # Serialize and return the created message
            serializer = MessageSerializer(instance=assistant_message_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except openai.error.OpenAIError as e:
            # Handle OpenAI API errors
            return Response({"error": f"OpenAI API error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            # Handle any unexpected errors
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
